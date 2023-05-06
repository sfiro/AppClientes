import click
from tabulate import tabulate

from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n','--name',
              type = str,
              prompt = True,
              help = 'The client name')
@click.option('-c','--company',
              type = str,
              prompt = True,
              help = 'The client company')
@click.option('-e','--email',
              type = str,
              prompt = True,
              help = 'The client email')
@click.option('-p','--position',
              type = str,
              prompt = True,
              help = 'The client position')
@click.pass_context
def create(ctx,name,company,email,position):
    """Create a new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])
    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """list all clients"""
    Client_service = ClientService(ctx.obj['clients_table'])

    client_list =  Client_service.list_clients()
    
    data = []
    data.append(["ID","NAME","COMPANY","EMAIL","POSITION"])
    for client in client_list:
        data.append([client['uid'],client['name'],client['company'],client['email'],client['position']])
    print(tabulate(data,headers='firstrow'))

@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def update(ctx,client_uid):
    """updates a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    #client_list = client_service.list_clients()
    client = [client for client in client_service.list_clients() if client['uid'] == client_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)
        click.echo('client updated')
    else:
        click.echo('client not found')
    

def _update_client_flow(client):
    click.echo('leave empty if you dont want modify the value')

    client.name = click.prompt('New name', type = str, default=client.name)
    client.company = click.prompt('New company', type = str, default=client.company)
    client.email = click.prompt('New email', type = str, default=client.email)
    client.position = click.prompt('New position', type = str, default=client.position)
    return client


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def delete(ctx,client_uid):
    """deletes a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()
    client = [client for client in client_list if client['uid'] == client_uid]
    if client:
        client_service.delete_client(Client(**client[0]))
        click.echo("client was delete")
    else:
        click.echo('client not found')


all = clients