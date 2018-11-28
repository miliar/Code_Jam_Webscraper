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
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

ll n, k;

void go(){
	map<ll, ll> m[100];
	m[0][-n] = 1;
	ll cc = 0;
	while(k){
		for(auto it : m[cc]){
			ll w = -it.fi;
			m[cc+1][-((w-1)/2)] += it.se;
			m[cc+1][-((w)/2)] += it.se;
			k-=it.se;
			//cout << cc << ' ' << m[cc].size() << endl;
			if(k <= 0){
				cout << (w)/2 << ' ' << (w-1)/2 << '\n';
				re;
			}
		}
		cc++;
	}
}

int main(){
	inf("C-large.in");
	ouf("output.txt");
	int t;
	cin >> t;
	f(i, t){
		cout << "Case #" << i+1 << ": ";
		cin >> n >> k;
		go();
	}
}
