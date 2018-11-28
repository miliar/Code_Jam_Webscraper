//
//  main.cpp
//  AscedingOrderCODEJAM17
//
//  Created by Umair Sheikh on 08/04/2017.
//  Copyright © 2017 White World Tech. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;
#define ll long long

vector<int> NumberToList(ll num) {
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
    for(int i=0; i<l.size(); i++) {
        if(l[i] > 0) {
            a+=  to_string(l[i]);
        }
    }
    return a;
}

string compute(ll next) {
    vector<int> list = NumberToList(next);
    for(int i=(int)list.size()-1; i>0; i--) {
        int t = list[i];
        int p = list[i-1];
        if(p > t) {
            for(int k=i; k<list.size(); k++) {
                list[k] = 9;
            }
            list[i-1] --;
        }
        
    }
    return ListToString(list);
}

int main(int argc, const char * argv[]) {
    // insert code here...
    ll cno=0;
    ll tt;
    ifstream fin("B-large.in.txt");
    ofstream fout("fileLarge.out");
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
