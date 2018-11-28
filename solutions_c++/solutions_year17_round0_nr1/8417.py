//
// Created by gopia on 08/04/2017.
//

#include <iostream>
#include <queue>
#include <unordered_map>
#include <fstream>

int main() {
    std::ifstream input_data = std::ifstream("input.txt", std::ifstream::in);
    std::ofstream output_data ("output.txt", std::ofstream::out);

    int T;
    input_data >> T;
    for(int i = 1; i<=T; i++) {
        int result;
        std::string s;
        std::string terminating_condition;
        int K;

        input_data >> s;
        input_data >> K;

        std::queue<std::string> BFS_queue = std::queue<std::string>();

        std::unordered_map<std::string, bool> visited = std::unordered_map<std::string, bool>();
        std::unordered_map<std::string, int> cost = std::unordered_map<std::string, int>();

        visited[s] = true;
        cost[s] = 0;


        BFS_queue.push(s);

        terminating_condition = std::string(s.length(), '+');

        while(!BFS_queue.empty()) {

            // Get the first element.
            std::string state = BFS_queue.front();


            // Check for terminating condition
            if(state == terminating_condition) break;


            // Loop over all possible starting positions to flip from.
            for(int i = 0; i<state.length(); i++) {
                if(i+K <= state.length()){
                    // Make copy of the string
                    std::string obtain = std::string(state);

                    int j;
                    // Construct the new string from flipping all pancakes
                    for(j = i; j<i+K; j++) {
                        if(obtain[j] == '+') obtain[j] = '-';
                        else obtain[j] = '+';
                    }
                    // If the string hasn't been visited, add to queue, and update.
                    if(!visited[obtain]) {
                            BFS_queue.push(obtain);
                            visited[obtain] = true;
                            cost[obtain] = cost[state] + 1;
                    }
                }
            }

            // Having constructed all accessible states, remove the visited state.
            BFS_queue.pop();
        }
        if(BFS_queue.empty()) result = -1;
        else result = cost[BFS_queue.front()];
        output_data << "Case #" << i << ": ";
        if(result == -1)
            output_data << "IMPOSSIBLE" << std::endl;
        else
            output_data << result << std::endl;
    }


}


