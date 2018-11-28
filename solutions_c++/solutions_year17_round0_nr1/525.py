//
//  main.cpp
//  CodeJam
//
//  Created by Vasja Pavlov on 4/8/17.
//  Copyright © 2017 Vasja Pavlov. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

int main(int argc, const char * argv[]) {
    
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    
    int t;
    
    cin >> t;
    
    string s;
    int k, n;
    int caseNum = 1;
    bool flipped[1001];
    while(t--) {
        
        cin >> s >> k;
        n = (int)s.size();
        int flips = 0;
        int affectedFlips = 0;
        bool ok = true;
        memset(flipped,0,sizeof(flipped));
        
        for(int i = 0; i < n; i++) {
            int x = (s[i] == '+' ? 1 : 0);
            x = (x+affectedFlips)%2;
            s[i] = (x== 1 ? '+' : '-');
            bool didFlip = false;
            
            if(s[i] == '-') {
                if(i+k-1 < n) {
                    s[i] = '+';
                    flips++;
                    affectedFlips++;
                    flipped[i]=true;
                    didFlip = true;
                } else {
                    ok = false;
                    break;
                }
            }
            if(i - k + 1 >= 0 && flipped[i-k+1]) {
                affectedFlips--;
            }
        }
        cout << "Case #"<<caseNum<<": ";
        if(!ok) cout << "IMPOSSIBLE\n";
        else cout << flips << endl;
        caseNum++;
    }
    return 0;
}
