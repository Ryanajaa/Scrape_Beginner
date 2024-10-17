import asyncio
import subprocess
import sys
import os

keyword = sys.argv[1]
print(f"start scrape 3 web url: {keyword}")

async def run_script(script_name):
    process = await asyncio.create_subprocess_exec(
        "python", script_name,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    stdout, stderr = await process.communicate()  # Wait for the script to finish
    
    if stdout:
        print(f"{script_name} output:\n{stdout.decode()}")
    if stderr:
        print(f"{script_name} error:\n{stderr.decode()}")

async def run_group(scripts):
    tasks = [run_script(script) for script in scripts]
    await asyncio.gather(*tasks)  # Run all scripts concurrently

async def run_script_input(script_name, *args):
    process = await asyncio.create_subprocess_exec(
        "python", script_name, *args,  # Unpack arguments here
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    stdout, stderr = await process.communicate()  # Wait for the script to finish
    
    if stdout:
        print(f"{script_name} output:\n{stdout.decode()}")
    if stderr:
        print(f"{script_name} error:\n{stderr.decode()}")

async def run_group_input(scripts):
    tasks = [run_script_input(script, keyword) for script in scripts]
    await asyncio.gather(*tasks)  # Run all scripts concurrently

async def main():

    # First group of scripts
    group1 = [
        "1.Amazon_url.py",
        "1.Ebay_url.py",
        "1.Walmart_url.py"
    ]
    await run_group_input(group1)  # Run the first group and wait for them to finish
    print("done scrape urls")

    # Second group of scripts
    group2 = [
        "2.Amazon_data.py",
        "2.Ebay_data.py",
        "2.Walmart_data.py"
    ]
    await run_group(group2)  # Run the second group and wait for them to finish
    print("done list product")
    
    # Run the final scripts
    os.system("python " + "3.algo_sort.py")
    os.system("python " + "3.compro_sort.py")
    os.system("python " + "4.edit_data.py")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
