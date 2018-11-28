//
//  main.cpp
//  codejam
//
//  Created by Noura Ahmed on 4/8/17.
//  Copyright © 2017 Nura Ahmed. All rights reserved.
//
#include <fstream>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include<string>
#include <numeric>
#include <sstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text


void testPancakes(string s, int k, int testCase){
    string lst = s;
    int numberOfFlip =0;
    vector<bool> sequence;
    for (int i = 0 ; i < s.length(); i++) {
        if (lst[i] == '-') {
            sequence.push_back(false);
        }
        else{
            //+
            sequence.push_back(true);
        }
        
    }
    //calculating number of flips
    for (int i = 0 ; i < sequence.size(); i++) {

        if (sequence[i] == true) {
            continue;
        }
        else{
        //toggle k chars
            int tempCounter = i+k;

            //must make sure I dont cross the boundry
            for (int j = i ; j<tempCounter; j++) {
                if (tempCounter > sequence.size()) {
                    break;
                }
                sequence[j] = !sequence[j];
            }
            numberOfFlip++;
        }
        
    }
    int sum_of_elems = std::accumulate(sequence.begin(), sequence.end(), 0);
    if (sum_of_elems == sequence.size()) {
        cout << "Case #" << testCase << ": " << numberOfFlip << endl;
    }
    else{
        cout << "Case #" << testCase << ": " << "IMPOSSIBLE" << endl;
    }
    
        
}
int main(int argc, char* argv[]) {
    int t;

    
    //std::map <int, int> number_list;
    std::ifstream initfile(argv[1]);
    string outputString;
    std::string inputString;

    
    std::getline(initfile, inputString);
    t = std::stoi(inputString);
    //t=2;
    int k = 0;
    for (int i = 1; i <= t; ++i) {
        std::getline(initfile, inputString);
        //cin >> inputString;
        istringstream iss2(inputString);
        
        string temp;
        iss2 >> temp;
        iss2 >> k;
        testPancakes(temp, k, i);

        // cout knows that n + m and n * m are ints, and prints them accordingly.
        // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    }
    
    
    return 0;
}
