//
//  main.cpp
//  Codejam2017_Qual
//
//  Created by Kudratillo Ismatov on 4/8/17.
//  Copyright © 2017 Kudratillo Ismatov. All rights reserved.
//

#include <iostream>
#include <cstdio>

using namespace std;

string s;
int k;

void solve() {
    bool cool = true;
    int numberOfFlips = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '-') {
            
            numberOfFlips++;
            
            if (i + k > s.length()) {
                cool = false;
                break;
            }
                
            for (int j = i; j < i + k; j++) {
                s[j] = (s[j] == '-') ? '+' : '-';
            }
        }
    }
    
    if (cool) {
        cout << numberOfFlips << endl;
    }
    else
        cout << "IMPOSSIBLE" << endl;
    
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    
    for (int i = 1; i <= t; i++) {
        
        cin >> s >> k;
        cout << "Case #" << i << ": ";
        solve();
        
    }
    
    return 0;
}
