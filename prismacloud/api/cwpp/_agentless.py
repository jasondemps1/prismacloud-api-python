""" Prisma Cloud Compute API Agentless Endpoints Class """

# Containers

class AgentlessPrismaCloudAPICWPPMixin:
    """ Prisma Cloud Compute API Agentless Endpoints Class """

    # Get Agentless Host Statuses
    def host_statuses(self, query_params=None):
        return self.execute_compute('GET', 'api/v1/agentless/hosts-status', query_params=query_params, paginated=True)