from agent_framework import (
    handler, Executor, ChatAgent, WorkflowContext, 
)

from domain.models import (LineComment, 
    SecretsDetectorExecutorResponse
)
from domain.utils import CustomResponseEvent
from domain.settings import settings


class ChunksAgregatorExec(Executor):

    def __init__(self, id, github_mcp_server):
         #TODO: Here comes the code ;)
        return

    async def _call_github_mcp_client(self, detected_secret: SecretsDetectorExecutorResponse, line_comment: LineComment):
        #TODO: Here comes the code ;)
        return

    @handler
    async def run(self, detected_secrets: list[SecretsDetectorExecutorResponse] ,ctx: WorkflowContext[None]) -> None:
        #TODO: Here comes the code ;)
        return