import os
import re
import subprocess
import sys

clone_folder = sys.argv[1]
source_filename = sys.argv[2]

with open(source_filename, "r") as file:
    repo_list = [repo.strip() for repo in file.readlines()]

regex = r"/([^/]+)\.git$"

for repo in repo_list:
    folder_name = re.findall(regex, repo)[0]
    os.system(f'git clone {repo} "{clone_folder}/{folder_name}"')

dir_result = subprocess.run(
    ["dir", clone_folder, "/A:D", "/B"],
    shell=True,
    capture_output=True,
    text=True
)
if len(dir_result.stdout.split("\n")) == len(repo_list):
    print(f"[+] Succès : les {len(repo_list)} repositories ont bien été cloné dans le dossier{clone_folder}.")
else:
    print(f"[-] Erreur : une erreur est survenue.")