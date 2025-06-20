import logging
import os
import requests
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    logging.info('Python timer trigger function started.')

    workspace_id = os.environ['workspaceId']
    workspace_key = os.environ['workspaceKey']

    logging.info(f'Workspace ID: {workspace_id}')
    logging.info('Function executed successfully.')
