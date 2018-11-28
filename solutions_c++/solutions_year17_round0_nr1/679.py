//
//  main.cpp
//  Oversized Pancake Flipper
//
//  Created by Shuying Sun on 4/7/17.
//  Copyright © 2017 Shuying Sun. All rights reserved.
//

#include <iostream>
using std::cout; using std::endl; using std::cin;
using std::string;
using std::ostream;
using std::pair;
using std::make_pair;
#include <fstream>
using std::ofstream;
using std::ifstream;



int minimum_flip_number(string S, int K){
    bool flipped[S.size()];
    for (int i = 0; i < S.size(); ++i) flipped[i] = false;
    int cnt = 0;
    for (int i = 0; i <= S.size()-K; ++i){
        if ( (S[i] == '+' && !flipped[i])||(S[i] == '-' && flipped[i])) continue;
        cnt++;
        for (int j = 0; j < K; ++j) flipped[i+j] = !flipped[i+j];
    }
    for (int i = S.size()- K; i < S.size(); ++i){
        if ( (S[i] == '+' && !flipped[i]) || (S[i] == '-' && flipped[i])) continue;
        return -1;
    }
    return cnt;
    
}
int main(int argc, const char * argv[]) {
    int T = 0;
    ifstream file;
    file.open("/Users/shuyingsun/Downloads/A-large.in.txt");
    file >> T;
    ofstream output;
    output.open("/Users/shuyingsun/Desktop/flip_output_large.txt");
    for (int i = 1; i <= T; ++i){
        string S;
        int K;
        file >> S >> K;
        int res = minimum_flip_number(S,K);
        output << "Case #" << i<<": ";
        if (res < 0) output << "IMPOSSIBLE\n";
        else output<< res << "\n";
    }
    file.close();
    output.close();
    return 0;
    
}

