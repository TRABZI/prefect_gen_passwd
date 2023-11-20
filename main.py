import random
import string
import os
from prefect import flow,task


from prefect.infrastructure.container import DockerContainer
docker_container_block = DockerContainer.load("genpasswdcontainer")


from prefect.filesystems import GitHub
github_block = GitHub.load("genpasswd")


@task
def task_1(length: int):
    # get random password pf length 8 with letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)


@flow
def passwd_flow():
    task_1(10)    

if __name__ == "__main__":
    passwd_flow()
