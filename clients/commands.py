import click

@click.group()
def clients():
    """manages the clients lifecycle"""
    pass


@clients.command()
@click.pass_context
def create(ctx,name,company,email,position):
    """Create a new client"""
    pass


@clients.command()
@click.pass_context
def list(ctx):
    """list all clients"""
    pass


@clients.command()
@click.pass_context
def update(ctx,client_uid):
    """updates a client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx,client_uid):
    """deletes a client"""
    pass


all = clients