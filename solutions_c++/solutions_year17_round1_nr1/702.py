//
//  main.cpp
//  question 1
//
//  Created by Shuying Sun on 4/14/17.
//  Copyright © 2017 Shuying Sun. All rights reserved.
//

#include <iostream>
using std::cout; using std::endl; using std::cin;
using std::max; using std::min;
using std::string;
using std::ostream;
using std::pair;
using std::make_pair;
#include <fstream>
using std::ofstream;
using std::ifstream;
#include <unordered_map>
using std::unordered_map;
#include <queue>
using std::queue;
#include <stack>
using std::stack;
#include <map>
using std::map;
#include <vector>
using std::vector;
#include <set>
using std::vector;
#include <unordered_set>
using std::unordered_set;
using std::multiset;
using std::unordered_multiset;

using std::priority_queue;






void assign(vector<string>& board){
    vector<int> processed{};
    for (int i = 0; i < board.size(); ++i){
        if (board[i] == string(board[0].size(),'?')) continue;
        processed.push_back(i);
        int index = -1;
        for (int j = 0; j < board[i].size(); ++j){
            if (board[i][j] != '?'){
                if (index+1 < j){
                    for (int k = index+1; k < j; ++k) board[i][k] = board[i][j];
                }
                index = j;
            }
        }
        if (index != board[i].size()-1){
            for (int k = index+1; k < board[i].size(); ++k) board[i][k] = board[i][index];
        }
    }
    int index = -1;
    for (int i = 0; i < processed.size(); ++i){
        if (index + 1 != processed[i]){
            for (int row = index+1; row < processed[i]; ++row) board[row] = board[processed[i]];
        }
        index = processed[i];
    }
    if (index != board.size()-1){
        for (int row = index+1; row < board.size(); ++row){
            board[row] = board[index];
        }
    }
    
}
int main(int argc, const char * argv[]) {
    int T = 0;
    ifstream file;
    file.open("/Users/shuyingsun/Downloads/A-large.in-2.txt");
    file >> T;
    ofstream output;
    output.open("/Users/shuyingsun/Desktop/q1_output.txt");
    for (int i = 1; i <= T; ++i){
        int R, C;
        file >> R >> C;
        vector<string> board{};
        for (int j = 1; j <= R; ++j){
            string temp;
            file >> temp;
            board.push_back(temp);
        }
        assign(board);
        output << "Case #" << i<<":\n";
        for (int j = 1; j <= R; ++j){
            output << board[j-1] << "\n";
        }
    }
    file.close();
    output.close();
    return 0;
    
}
