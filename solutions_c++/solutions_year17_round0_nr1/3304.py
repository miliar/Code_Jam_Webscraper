#include <bits/stdc++.h>

#define INF 2139062143
#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i= int(ini); i<(int)lim; ++i)
#define ford(i, ini, lim) for(int i= int(ini); i>=(int)lim; --i)
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
char inv(char s){
    if(s == '-') return '+';
    else return '-';
}
int main(){
	ios_base::sync_with_stdio(false);

    int t; cin >> t;
    int cases = 1;
    while(t--){
        string s; int k;
        cin >> s >> k;
        int ans = 0;
        fori(i,0,s.size()-k+1){
            if(s[i] == '-'){
                fori(j,0,k){
                    s[i+j] = inv(s[i+j]);
                }
                ans++;
            }
        }
        bool is = false;
        fori(i,0,s.size()){
            if(s[i] == '-') is = true;
        }
        cout << "Case #" << cases++ << ": "; 
        if(is) cout << "IMPOSSIBLE\n";
        else cout << ans << endl; 
    }

	return 0;
}
