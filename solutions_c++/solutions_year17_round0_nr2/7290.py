#include<bits/stdc++.h>
using namespace std;

int main() {
        
    freopen("in.txt", "r", stdin);
    freopen("op.txt", "w", stdout);
    
    int t;
    cin >> t;
    for(int q = 0; q<t; ++q) {
        string s;
        cin >> s;
        
        int l = s.size();
        vector<int> lim(l);
        
        for(int i = 0; i<l; ++i) {
            lim[i] = int(s[i] - '0');
        }
        
        vector<int> num(l);
        int prev = 0;
        int i = 0;
        int v = lim[0], idx = 0;
        while(i<l) {
            if(lim[i] >= prev) {
                num[i] = lim[i];
                prev = lim[i];
                if(v != lim[i]) {
                    v = lim[i];
                    idx = i;
                }
                i++;
            }
            else {
                prev--;
                num[idx] = prev;
                v = prev;
                i = idx+1;
                for(int j = i; j<l; ++j) {
                    lim[j] = 9;
                }
                
            }
        }
        
        cout << "Case #" << q+1 << ": ";
        
        int flag = 0;
        int r = num.size();
        for(int k = 0; k<r; ++k) {
            
            if(num[k] != 0) {
                flag = 1;
            }

            if(flag) {
                cout << num[k];
            }
        }
        cout << endl;
        
    }
    
    return 0;
}