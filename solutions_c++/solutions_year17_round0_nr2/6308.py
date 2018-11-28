#include <bits/stdc++.h>

#define sz(z) (int)z.size()
#define fo(i,a,b) for (auto (i) = (a); (i) < (b); (i)++)
#define mp make_pair
#define pb push_back

using namespace std;

#define DEBUG

#ifdef DEBUG
#define D(x...) printf(x)
#else
#define D(x...) 
#endif

typedef long long ll;
typedef pair<int,int> ii;

string mi (string s, int k) {
	while (sz(s) && s[0] == '0') {
		s.erase(s.begin());
	}
	if (s[sz(s)-k] == '0') {
		s[sz(s)-k] = '9';
		return mi(s, k+1);
	}
	s[sz(s)-k]--;
	/*
	while (sz(s) && s[0] == '0') {
		s.erase(s.begin());
	}
	*/
	return s;
}	

string go (string s) {
	int i = sz(s) - 1;
	char kek = '9';
	while (i >= 0) {
		if (kek < s[i]) {
			s = mi(s, sz(s)-i);
			i++;
			while (i < sz(s)) s[i] = '9', i++;
			while (sz(s) && s[0] == '0') {
				s.erase(s.begin());
			}
			return go(s);
		}
		kek = s[i];
		i--;
	}
	return s;
}

int main() {
	int t;
	cin >> t;
	for (int _ = 1; _ <= t; _++) {
		printf("Case #%d: ", _);
		int n, k;
		string s;
		cin >> s;
		cout << go(s) << endl;
	}
	
	return 0;
}
