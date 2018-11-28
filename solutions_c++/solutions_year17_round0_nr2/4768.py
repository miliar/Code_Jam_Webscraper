//
//  main.cpp
//  tidy number
//
//  Created by Zain Sheikh on 08/04/2017.
//  Copyright © 2017 Zain sheikh. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;
#define ll long long

vector<int> parse(ll num) {
    vector<int> list;
    while(num > 0) {
        int d = num%10;
        num /=10;
        list.push_back(d);
    }
    reverse(list.begin(), list.end());
    return list;
}
string ListToString(vector<int> l) {
    string a = "";
    bool nineFlag = false;
    for(int i=0; i<l.size(); i++) {
        if(nineFlag) {
            a+="9";
        }
        
        else if(l[i] > 0) {
            a+=  to_string(l[i]);
        }
        else if(l[i] < 0) {
            nineFlag = true;
            a+= "9";
        }
    }
    return a;
}

string compute(ll next) {
    vector<int> num = parse(next);
    for(int i=(int)num.size()-1; i>0; i--) {
        int t = num[i];
        int p = num[i-1];
        if(p > t) {
            num[i] = -1;
            num[i-1] --;
        }
        
    }
    return ListToString(num);
}

int main(int argc, const char * argv[]) {
    ll cno=0;
    ll tt;
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    fin>>tt;
    while(tt--) {
        cno++;
        ll next;
        
        fin>>next;
        
        fout<<"Case #"<<cno<<": ";
        string res = compute(next);
        fout<<res<<endl;
    }
    
    return 0;
}
