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

void row_update(string& r){
    int i = 0;
    int n = static_cast<int>(r.size());
    while(i < n && r[i] == '?') ++i;
    if(i == n) return;
    r.replace(0, i, string(i, r[i]));
    while(++i < n){
        if(r[i] == '?') r[i] = r[i-1];
    }
}

void update(vector<string>& record){
    vector<bool> allq(record.size(), true);
    for(int i = 0; i < record.size(); ++i){
        for(char ch : record[i]){
            if(ch != '?'){
                allq[i] = false;
                row_update(record[i]);
            }
        }
    }
    int i = 0;
    while(allq[i]) ++i;
    for(int j = 0; j < i; ++j) record[j] = record[i];
    while(++i < record.size()){
        if(allq[i]) record[i] = record[i-1];
    }
}


int main(){
    int T;
    int row, col;
    string s;
    vector<string> record;
    ifstream file("/Users/kejin/aa.txt");
    file >> T;
    ofstream output("/Users/kejin/output.txt");
    for(int i = 1; i <= T; ++i){
        file >> row >> col;
        for(int j = 0; j < row; ++j){
            file >> s;
            record.push_back(s);
        }
        update(record);
        output << "Case #" << i << ": " << endl;
        for(int j = 0; j < row; ++j){
            output << record[j] << endl;
        }
        record.clear();
    }
    file.close();
    output.close();
    return 0;
}
