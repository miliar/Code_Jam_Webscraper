
//be naame khodaa

#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <cstdio>
#include <algorithm>
#include <set>
#include <cassert>
#include <iomanip>
#include <cstring>
#include <sstream>
#define fi first
#define se second
#define rep(i, x, n) for (int i = x; i < n; i++)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
using namespace std;
typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> VI;

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int it = 1; it <= t; it++){
		string s;
		cin >> s;
		int n = s.length(), k;
		cin >> k;
		int res = 0;
		for (int i = 0; i < n-k+1; i++){
			if (s[i] == '-'){
				res++;
				for (int j = 0; j < k; j++)
					s[i+j] = (s[i+j] == '+' ? '-' : '+');
			}
		}
		cout << "Case #" << it << ": ";
		bool imp = false;
		for (int i = n-k+1; i < n; i++)
			if (s[i] == '-'){
				imp = true;
				break;
			}
		if (imp) cout << "IMPOSSIBLE\n";
		else cout << res << '\n';
	}
	return 0;
}
