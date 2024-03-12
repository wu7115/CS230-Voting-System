import socket
import pickle
import ntplib
from time import ctime
import datetime

def get_ntp_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org', version=3)
    return ctime(response.tx_time)

def send_results(votes):
    current_time = get_ntp_time()
    current_datetime = datetime.datetime.strptime(current_time, "%a %b %d %H:%M:%S %Y")
    host = '172.31.5.39' # master private IP
    port = 15469

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    if end_datetime>current_datetime:
        # List to send to the server
        client_list = (votes)

        # Send the list to the server
        data_to_send = pickle.dumps(client_list)
        client_socket.send(data_to_send)
    else:
        client_list = ('timeover')

        # Send the list to the server
        data_to_send = pickle.dumps(client_list)
        client_socket.send(data_to_send)
        print('timeover')

    # Close the connection
    client_socket.close()

def main():
    # Number of candidates
    num_candidates = 3

    # Initialize vote counts for each candidate
    votes = [0] * num_candidates

    # Get the number of voters
    # num_voters = int(input("Enter the number of voters: "))

    # Get votes from each voter
    for i in range(1):
        while True:
            try:
                # Get the candidate number the voter is voting for
                # vote = int(input(f"Voter {i + 1}, enter the candidate number (1 to {num_candidates}): "))
                vote = int(input(f"Please enter the candidate number (1 to {num_candidates}): "))

                # Validate the candidate number
                if 1 <= vote <= num_candidates:
                    break
                else:
                    print(f"Invalid candidate number. Please enter a number between 1 and {num_candidates}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Count the vote for the chosen candidate
        votes[vote - 1] += 1

    # Display the final vote counts
    print("\nVote counts for each candidate:")
    for i in range(num_candidates):
        print(f"Candidate {i + 1}: {votes[i]} votes")
    print(votes)
    return votes

if __name__ == "__main__":
    end_time = 'Sat Mar  9 22:23:59 2024'
    end_datetime = datetime.datetime.strptime(end_time, "%a %b %d %H:%M:%S %Y")
    current_time = get_ntp_time()
    current_datetime = datetime.datetime.strptime(current_time, "%a %b %d %H:%M:%S %Y")
    
    if current_datetime<end_datetime:
        votes = main()
        send_results(votes)