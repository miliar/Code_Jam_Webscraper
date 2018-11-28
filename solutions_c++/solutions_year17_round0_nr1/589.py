#include <bits/stdc++.h>

using namespace std;

#define ff first
#define ss second
#define pb push_back
#define eb emplace_back
#define fff ff
#define sss ss.ff
#define ttt ss.ss
#define INF (1 << 30)
#define LLF (1ll << 60)


#define FASTIO std::ios::sync_with_stdio(false)

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef unsigned int ui;

ll min(ll a, ll b) {if (a < b) return a; return b;};
ll max(ll a, ll b) {if (a > b) return a; return b;};
ll gcd(ll a, ll b) {return b == 0 ? a : gcd(b, a % b);};

/*-----------------END TEMPLATE-----------------*/

int rec(string s, int t) {

	int flip = 0;
	string k;
	int i = 0, j = s.size()-1;
	int max = j+1;
	while (s[i] == '+') i++;
	while (s[j] == '+') j--;
	if (i == s.size()) return 0;
	if (s.size() < t) return -1;


	for (int m = i; m <= j; m++) k += s[m];

	if (k.size() >= t) {
		flip++;
		for (int m = 0; m < t; m++) {
			if (k[m] == '+') k[m] = '-';
			else k[m] = '+';
		}
	}
	int tt = rec(k, t);
	if (tt == -1) return -1;
	flip += tt;
	return flip;

}

int main() {

	ll n;
	cin >> n;
	string s; ll t;
	for (int i = 1; i <= n; i++) {
		cin >> s >> t;
		int tt = rec(s, t);
		if (tt == -1)
		cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		else
		cout << "Case #" << i << ": " << tt << endl;

	}

}