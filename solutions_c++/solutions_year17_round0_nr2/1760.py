#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<pii> vii;
typedef vector<bool> vb;
typedef vector<string> vs;
const int MOD = 1e9 + 7;
const int di[] = { -1,0,1,0 };
const int dj[] = { 0,1,0,-1 };
#define INF 1000000000
#define mp make_pair
#define x first
#define y second

int main() {
	ios::sync_with_stdio(false), cin.tie(0);
	ifstream cin("B-large.in");
	ofstream cout("output.txt");
	int t, tt = 0; cin >> t;
	while (t--) {
		string s; cin >> s;
		for (int i = 0; i < s.length() - 1; i++)
			if (s[i] > s[i + 1]) {
				s[i]--;
				for (int j = i + 1; j < s.length(); j++)
					s[j] = '9';
				i -= i == 0 ? 1 : 2;
			}

		cout << "Case #" << ++tt << ": ";
		cout << stoll(s) << endl;
	}
	//cin.ignore(), cin.get();
}
