
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task(10)
    def applications(self):
        self.client.get("/applications")

    @task(10)
    def loadBalancers(self):
        self.client.get("/loadBalancers?provider=kubernetes")

    @task(10)
    def projects(self):
        self.client.get("/projects")

    @task(10)
    def pipelineConfigs(self):
        self.client.get("/pipelineConfigs")

    @task(10)
    def networks(self):
        self.client.get("/networks")

    @task(10)
    def firewalls(self):
        self.client.get("/firewalls")

    @task(10)
    def credentials(self):
        self.client.get("/credentials")

    @task(10)
    def artifacts_credentials(self):
        self.client.get("/artifacts/credentials")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1
    max_wait = 2
