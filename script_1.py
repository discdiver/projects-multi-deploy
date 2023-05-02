from prefect import flow


@flow(log_prints=True)
def flow_1():
    print("hi")
