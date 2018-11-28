#include <bits/stdc++.h>

#define INF 2139062143
#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i= int(ini); i<(int)lim; ++i)
#define ford(i, ini, lim) for(int i= int(ini); i>=(int)lim; --i)
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;

int main(){
	ios_base::sync_with_stdio(false);
    int t; cin >> t;
    int cases =1 ;
    while(t--){
        ll n; cin >> n;
        string s = to_string(n);
        int f = s.size(); 
        ford(i,s.size()-2,0){
            if(s[i] > s[i+1]){
                s[i+1] = '9';
                s[i] -= 1;
                f = i+1;
            }
        }
        fori(i,1,s.size()) if(s[i] == '0') s[i] = '9';
        fori(i,f+1,s.size()) s[i] = '9';
        cout << "Case #" << cases++ << ": ";
        bool l = true;
        fori(i,0,s.size()){
            if(s[i] != '0') l = false;
            if(l && s[i] == '0') continue;
            cout << s[i];
        }
        cout << endl;
    }

	return 0;
}
