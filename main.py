import subprocess

def get_merged_branches():
    """Gets all merged branches."""
    try:
        # Get the list of merged branches relative to the active branch (usually 'main' or 'master')
        result = subprocess.check_output(
            ['git', 'branch', '--merged'],
            stderr=subprocess.STDOUT
        ).decode('utf-8')

        # Split the output and remove the active branch (with ' * ' in front) and 'main' or 'master'
        branches = result.split('\n')
        branches = [branch.strip().replace('* ', '') for branch in branches if branch.strip() and branch.strip() not in ['main', 'master']]
        return branches

    except subprocess.CalledProcessError as e:
        print(f"Error fetching merged branches: {e.output.decode('utf-8') if e.output else str(e)}")
        return []

def delete_branch(branch_name):
    """Deletes a specific branch locally."""
    try:
        print(f"Deleting branch: {branch_name}")
        subprocess.check_call(['git', 'branch', '-d', branch_name])  # -d ensures only merged branches are deleted
    except subprocess.CalledProcessError as e:
        print(f"Error deleting branch {branch_name}: {e.output.decode('utf-8') if e.output else str(e)}")

def main():
    # Get the merged branches
    merged_branches = get_merged_branches()

    if not merged_branches:
        print("No merged branches to delete.")
        return

    # Delete the merged branches
    for branch in merged_branches:
        delete_branch(branch)

if __name__ == "__main__":
    main()
