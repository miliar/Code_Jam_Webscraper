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
#include <queue>
#include <map>
#include <list>
#include <set>
#include <string>



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


struct cmp{
    bool operator()(const pair<int, int>& a, const pair<int, int>& b){
        return a.second < b.second;
    }
};

bool compare(const pair<int, int>& a, const pair<int, int>& b){
    return a.second < b.second;
}


double speed(vector<double>& time, int D){
    return D/(*max_element(time.begin(), time.end()));
}

int main(){
    int T, D, N;
    double K, S;
    vector<double> record;
    ifstream file("/Users/kejin/test.txt");
    file >> T;
    ofstream output("/Users/kejin/output.txt");
    output.precision(11);
    for(int i = 1; i <= T; ++i){
        file >> D >> N;
        for(int j = 0; j < N; ++j){
            file >> K >> S;
            record.push_back((D - K)/S);
        }
        output << "Case #" << i << ": "  << speed(record, D)<< endl;
        record.clear();
    }
    file.close();
    output.close();
    return 0;
}
