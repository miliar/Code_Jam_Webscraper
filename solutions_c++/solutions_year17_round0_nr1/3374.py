//
//  main.cpp
//  test
//
//  Created by Ke Jin on 2/25/17.
//  Copyright © 2017 Ke Jin. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <typeinfo>
#include <algorithm>
#include <numeric>
#include <unordered_map>
#include <sstream>
#include <memory>
#include <stack>
#include <fstream>


using namespace std;

void print_v(vector<string>& svec){
    for(string s : svec){
        cout << s << ' ';
    }
    cout << endl;
}

void print_v(vector<int>& ivec){
    for(int i : ivec){
        cout << i << ' ';
    }
    cout << endl;
}

void print_v(vector<double>& ivec){
    for(double d : ivec){
        cout << d << ' ';
    }
    cout << endl;
}

bool is_substr(string s, string t){
    int i = 0;
    for(char c : t){
        while(i < s.size() && s[i] != c) ++i;
        if(i == s.size()) return false;
        ++i;
    }
    return true;
}

string min_flip(string s, int k){
    auto len = s.size();
    vector<int> record(len, 0);
    int flips = 0;
    for(int i = 0; i < len; ++i){
        if(s[i] == '+' && flips % 2 == 1) {record[i] = 1; ++flips;}
        if(s[i] == '-' && flips % 2 == 0) {record[i] = 1; ++flips;}
        if(i + 1 >= k && record[i+1-k]) --flips;
    }
    if(all_of(record.end() - k + 1, record.end(), [](int i){return i == 0;})){
        return to_string(accumulate(record.begin(), record.end(), 0));
    }
    else return "IMPOSSIBLE";
}

int main(){
    int T, k;
    string s;
    ifstream file("/Users/kejin/large.txt");
    file >> T;
    ofstream output("/Users/kejin/output_large.txt");
    for(int i = 1; i <= T; ++i){
        file >> s >> k;
        output << "Case #" << i << ": " << min_flip(s, k) << endl;
    }
    file.close();
    output.close();
    cout << "HaHa" << endl;
    return 0;
}
