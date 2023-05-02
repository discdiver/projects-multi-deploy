from prefect import flow


@flow(log_prints=True)
def flow_2():
    print("Hey there!")
