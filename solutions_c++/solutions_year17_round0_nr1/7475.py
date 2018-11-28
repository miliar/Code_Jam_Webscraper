//
//  PanCakes.cpp
//  playground
//
//  Created by Divyesh Chandra on 08/04/17.
//  Copyright © 2017 Divyesh Chandra. All rights reserved.
//

#include <iostream>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <string>

using namespace std;
typedef long long LL;

string flips(string s, int k){
    int count = 0;
    int i = 0;
    while(i < s.size()){
        if(s[i] == '-'){
            for(int j=i;j<i+k;j++){
                if(j >= s.size())
                    return "IMPOSSIBLE";
                else if(s[j] == '-')
                    s[j] = '+';
                else
                    s[j] = '-';
            }
            count++;
        }
        i++;
    }
    return to_string(count);
}

int main(){
    FILE *fin = freopen("A-large.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        string s;
        int k;
        string count;
        cin >> s >> k;
        count = flips(s,k);
        cout << "Case #" << t << ": ";
        cout << count << endl;
    }
    return 0;
}
