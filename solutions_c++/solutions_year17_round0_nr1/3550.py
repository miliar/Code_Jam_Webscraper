#include <bits/stdc++.h>
#define rep(i, a, n) for(int i = a; i < n; i++)
#define repb(i, a, b) for(int i = a; i >= b; i--)
#define all(a) a.begin(), a.end()
#define o(a) cout << a << endl
#define int long long
#define fi first
#define se second
using namespace std;
typedef pair<int, int> P;

signed main(){
    int t;
	cin >> t;
	for(int ti = 1; ti <= t; ti++){
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        rep(i, 0, s.size() - k + 1){
            if(s[i] == '-'){
                ans++;
                for(int j = 0; j < k; j++){
                    if(s[i + j] == '-') s[i + j] = '+';
                    else s[i + j] = '-';
                }
            }
        }
        bool f = true;
        rep(i, 0, s.size()){
            if(s[i] == '-') f = false;
        }
        if(f){
		    cout << "Case #" << ti << ": " << ans << endl;
        }else{
		    cout << "Case #" << ti << ": IMPOSSIBLE" << endl;            
        }
	}
}