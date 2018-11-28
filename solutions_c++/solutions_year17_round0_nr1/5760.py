#include <iostream>
#include <string>
using namespace std;
#define MAX_N 2005
bool lets[MAX_N];
int main() {
    int t;
    cin >> t;
    for(int zz = 1; zz <= t; zz++) {
        string s;
        cin >> s;
        int len = s.length();
        int k;
        cin >> k;
        for(int i = 0; i < len; i++) {
            if(s[i] == '-') {
                lets[i] = false;
            } else {
                lets[i] = true;
            }
        }
        
        int count = 0;
        for(int i = 0; i < len-k+1; i++) {
            if(!lets[i]) {
                count ++;
                for(int j = 0; j < k; j++) {
                    lets[i+j] = !lets[i+j]; 
                }
            }
        }
        bool possible = true;
        for(int i = len-k+1; i < len; i++) {
            if(!lets[i]) possible = false;
        }
        cout << "Case #"<<zz<<": ";
        if(possible) {
            cout <<count<<"\n";
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }
}
