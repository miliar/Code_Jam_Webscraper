#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstdio>


using namespace std;

const int MAXN = 1e3;

int T, ans, k, n;
string s;

int main(){
    freopen("a.in", "r", stdin);
    freopen("a1.out", "w", stdout);
    
    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> s >> k;
        n = s.length();
        ans = 0;
        bool bln = false;
        int revs[MAXN + 10] = {0};

        for(int i = 0; i < n; i++){
            if((s[i] == '-' && revs[i] % 2 == 0) || (s[i]=='+' && revs[i] % 2 == 1)){
                if(n - i < k){
                    bln = true;
                    break;
                }
                for(int j = 0; j < k; j++){
                    revs[i+j]++;
                }
                ans++;
            }
        }
        
        if(bln){
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
            continue;
        }
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}