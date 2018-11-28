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

pair<int, int> stalls(int n, int k){
    if(n == k) return {0, 0};
    priority_queue<pair<int, int>> que;
    que.push({n, 1});
    while(k > que.top().second){
        int cnt = que.top().second;
        k -= cnt;
        n = que.top().first;
        que.pop();
        if(n&1) que.push({n/2, 2*cnt});
        else{
            que.push({n/2, cnt});
            que.push({n/2 - 1, cnt});
        }
    }
    n = que.top().first;
    if(n&1){
        return {n/2, n/2};
    }
    else return {n/2, n/2 - 1};
}

int main(){
    int T;
    int n, k;
    ifstream file("/Users/kejin/test.txt");
    file >> T;
    ofstream output("/Users/kejin/output.txt");
    for(int i = 1; i <= T; ++i){
        file >> n >> k;
        auto p = stalls(n, k);
        output << "Case #" << i << ": " << p.first << ' ' << p.second << endl;
    }
    file.close();
    output.close();
    cout << "HaHa" << endl;
    return 0;
}
