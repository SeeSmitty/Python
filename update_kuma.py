#!/usr/bin/env python3

#import required modules
import subprocess

#define the function to update the Uptime Kuma Docker Compose and launch it
def update_container():
    # Step 1: Change directory to 'mykuma'
    mykuma_directory = "/home/smitty/mykuma"
    subprocess.run(f"cd {mykuma_directory}", shell=True)

    # Step 2: Pull the latest images
    subprocess.run("sudo docker compose -f /home/smitty/mykuma/docker-compose.yml pull", shell=True)

    # Step 3: Recreate and bring up the containers
    subprocess.run("sudo docker compose -f /home/smitty/mykuma/docker-compose.yml up -d --force-recreate", shell=True)

    # Step 4: Display Running Docker Containers
    subprocess.run("docker ps -a", shell=True)

if __name__ == "__main__":
    update_container()

