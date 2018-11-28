#include <bits/stdc++.h>
 
#define gc getchar
#define ii(x) scanf(" %d", &x)
#define ill(x) scanf(" %lld", &x)
#define ll long long
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define all(x) x.begin(),x.end()
#define fill(a,b) memset(a, b, sizeof(a))
#define rep(i,a,b) for(i=a;i<b;i++)
#define per(i,a,b) for(i=a;i>=b;i--)
#define pii pair<int, int>
 
using namespace std;
 
void in(int &x){
    register int c=gc();
    x=0;
    for(;(c<48||c>57);c=gc());
    for(;c>47&&c<58;c=gc()){x=(x<<1)+(x<<3)+c-48;}
}

bool ok(string s){
	int n = s.length(), i;
	rep(i, 1, n) if(s[i] < s[i - 1]) return false;
	return true;
}

string findNext(string s){
	int n = s.length(), i;
	per(i, n - 2, 1) if(s[i] >= s[i + 1] && s[i] > s[i - 1]){
		int j; rep(j, i, n){
			if(i == j) s[i]--;
			else s[j] = '9';
		}
		return s;
	}
	if(s[0] >= s[1] && s[0] != '1'){
		rep(i, 0, n){
			if(i == 0) s[i]--;
			else s[i] = '9';
		}
		return s;
	}
	string ret;
	rep(i, 1, n) ret += '9';
	return ret;
}

string brute(string s){
	ll n = 0, i, j;
	rep(i, 0, s.length()){
		n = n * 10 + (s[i] - '0');
	}
	per(i, n, 1){
		string cur;
		std::vector<ll> v;
		ll temp = i;
		while(temp){
			v.pb(temp % 10);
			temp /= 10;
		}
		reverse(all(v));
		rep(j, 0, v.size()){
			cur += (v[j] + '0');
		}
		if(ok(cur)) return cur;
	}
	return "1";
}

int main()
{
	ll t, i, tt;
	string s;
	cin >> t; rep(tt, 1, t + 1){
		cin >> s;
		string ret;
		//string temp = brute(s);
		if(ok(s)) ret = s;
		else ret = findNext(s);
		//cout << tt << " " << temp << endl;
		cout << "Case #" << tt << ": " << ret << endl;
	}

	return 0;
}