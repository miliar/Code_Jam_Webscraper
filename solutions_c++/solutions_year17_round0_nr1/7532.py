//
//  main.cpp
//  Pancake
//
//  Created by Volodymyr Tkachuk on 4/8/17.
//  Copyright © 2017 Volodymyr Tkachuk. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <queue>

const auto filename = "/Users/volodymyr/Downloads/A-large.in";
const auto outputFile = "/Users/volodymyr/Downloads/out.txt";
using namespace std;
int main() {
    ifstream input(filename);
    ofstream output(outputFile);
    int T;
    input >> T;
    for (auto t = 1; t <= T; ++t) {
        string S;
        int k;
        input >> S >> k;
        auto result = 0;
        queue<int> index;
        bool impossible = false;
        for (int i = 0; i < S.size() && !impossible; ++i) {
            while (!index.empty() && index.front() + k <= i)
                index.pop();
            if (((S[i] == '-') && (index.size()%2 == 0)) || ((S[i] == '+') && (index.size()%2 == 1))) {
                impossible = i+k > S.size();
                index.push(i);
                ++result;
            }
        }
        output << "Case #" << t << ": ";
        if (impossible)
            output << "IMPOSSIBLE";
        else
            output << result;
        output << endl;
    }
    return 0;
}
