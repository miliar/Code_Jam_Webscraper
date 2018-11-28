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

string last;
string ans;
string go(int cur, int len, char prev, string s){
	if(s > last) re "FAIL";
	if(cur == len && s <= last) re s;
	if(cur == len && s > last) re "FAIL";
    for(char i = '9'; i >= prev; i--){
        string t = go(cur+1, len, i, s+i);
        if(t != "FAIL"){
            re t;
        }
    }
    re "FAIL";
}

int main(){
	inf("B-large.in");
	ouf("output.txt");
	int n;
	cin >> n;
	f(i, n){
		cin >> last;
		cout << "Case #" << i+1 << ": ";
		string t = go(0, last.size(), '0', "");
		int j = 0;
		while(t[j] == '0') j++;
		for(; j < t.size(); ++j) cout << t[j];
		cout << '\n';
	}
}
