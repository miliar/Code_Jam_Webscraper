#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <iomanip>
#include <set>
#include <map>
#include <queue>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair <int, int> pii;
#define x first
#define y second
#define mp make_pair
#define pb push_back
const int N = (int)1e5 + 5, INF = (int)1e9;
const ld EPS = 1e-9;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	cin >> T;
	for(int z = 1; z <= T; z++){
		string s;
		int k, n, ans = 0;
		cin >> s >> k;
		n = (int)s.size();
		for(int i = 0; i < n - k + 1; i++)
			if(s[i] == '-'){
				ans++;
				for(int j = i; j < i + k; j++){
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
			for(int i = n - k; i < n; i++)
				if(s[i] == '-') {
					ans = -1;
					break;
				}
			cout << "Case #" << z << ": ";
			if(ans < 0)
				cout << "IMPOSSIBLE\n";
			else
				cout << ans << "\n";
	}
	return 0;
}