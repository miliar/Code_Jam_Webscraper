#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
#include <cstring>
#include <unordered_set>
#include <cstring>
#include <cstdio>
#include <climits>

using namespace std;
int t, k;
string s;
bool ss[100];
bool flipped[100];
int main() {
    
    ifstream fin("a.in");
    fin >> t;
    for(int tt=0; tt<t; tt++) {
        fin >> s >> k;
        int n = s.length();
        int count = 0;
        bool ans = true;
        bool cur_flip = 0;
        for(int i=0; i<n; i++){
            ss[i] = (s[i] == '+'); // 1 = + is happy
            flipped[i] = 0;
        }
        for(int i=0; i<=n-k; i++){
            if(i-k >= 0){
                cur_flip ^= flipped[i-k];
            }
            if(ss[i]^cur_flip != 1){
                cur_flip ^= 1;
                flipped[i] = 1;
                count++;
            }
            
        }
        for(int i=n-k+1; i<n; i++){
            if(i>=k){
                cur_flip ^= flipped[i-k];
            }
            if(ss[i]^cur_flip != 1) ans = false;
            
        }
        if(ans) {
            cout << "Case #" << (tt+1) << ": " << count << '\n';
        }
        else {
            cout << "Case #" << (tt+1) << ": Impossible\n";
        }
    }
}