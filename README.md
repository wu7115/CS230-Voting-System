Distributed Voting System

CLient nodes are for users to vote. There should be three candidates for users to pick. Users enter 1, 2, or 3 to vote and master node collects all the vote data from clients. 
Clients synchronize their to using NTP. When end of time clients each send a message to master. After master recieves the timeover message from all the clients it returns the result to clients.
