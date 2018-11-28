//----------------include---------------
#include <bits/stdc++.h>
//----------------define----------------
#define f(_i, _n) for (int _i = 0; _i < _n; _i++)
#define fr(_i, _n, _k) for (int _i = _k; _i < _n; _i++)
#define r(_t, _n) \
    _t _n; \
    cin >> _n;
#define ra(_type, _name, _len)\
_type _name[_len]; f(_i, _len)\
    cin >> _name[_len];
#define mp make_pair
#define re return
#define takedown re 0;
#define fi first
#define se second
#define inf(_name) freopen(_name, "r", stdin);
#define ouf(_name) freopen(_name, "w", stdout);
#define pb push_back
#define fill(_a, _n) memset(_a, _n, sizeof(_n))

using namespace std;

int main(){
	inf("A-large.in");
	ouf("output.txt");
	int n;
	cin >> n;
	string s;
	int k;
	f(i, n){
		cin >> s >> k;
		cout << "Case #" << i+1 << ": ";
        int ans = 0;
        int n = s.size();
        for(int i = 0; i+k <= n; i++){
            if(s[i] == '-'){
				ans++;
				for(int j = i; j < i+k; j++) s[j] = s[j]=='-' ? '+' : '-';
            }
        }
        int f = 0;
        f(i, n) if(s[i] == '-') f = 1;
		if(f) cout << "IMPOSSIBLE";
		else cout << ans;
		cout << '\n';
	}
}
