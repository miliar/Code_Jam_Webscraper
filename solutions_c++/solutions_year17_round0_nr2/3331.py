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

long long tidy(long long n){
    vector<int> record;
    long long m = n;
    while(n){
        record.push_back(n%10);
        n /= 10;
    }
    reverse(record.begin(), record.end());
    int i = 0;
    while(i + 1 < record.size() && record[i] <= record[i+1]){
        ++i;
    }
    if(i + 1 == record.size()) return m;
    --record[i];
    while(i > 0 && record[i] < record[i-1]){
        --i;
        --record[i];
    }
    ++record[i];
    long long res = 0;
    for(int j = 0; j <= i; ++j){
        res += record[j] * pow(10LL, record.size() - j - 1);
    }
    return res - 1;
}

int main(){
    int T;
    long long n;
    string s;
    ifstream file("/Users/kejin/large2.txt");
    file >> T;
    ofstream output("/Users/kejin/output_large.txt");
    for(int i = 1; i <= T; ++i){
        file >> n;
        output << "Case #" << i << ": " << tidy(n) << endl;
    }
    file.close();
    output.close();
    cout << "HaHa" << endl;
    return 0;
}
