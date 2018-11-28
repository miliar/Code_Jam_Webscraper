
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

int c[10], d[10], j[10], k[10];

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int it = 1; it <= t; it++){
		int ac, aj;
		cin >> ac >> aj;
		for (int i = 0; i < ac; i++)
			cin >> c[i] >> d[i];
		for (int i = 0; i < aj; i++)
			cin >> j[i] >> k[i];
		if (ac > aj){
			swap (ac, aj);
			swap (c, j);
			swap (d, k);
		}
		int res = 0;
		if (ac == 0){
			if (aj == 0) res = 2;
			else if (aj == 1)
				res = 2;
			else if (aj == 2){
				if (j[0] > j[1]){
					swap(j[0], j[1]);
					swap(k[0], k[1]);
				}
				int have = 720 - (k[0] - j[0]) - (k[1] - j[1]);
				int A = j[0], B = j[1] - k[0], C = 1440 - k[1];
				if (A+B <= have || B+C <= have)
					res = 2;
				else if (B <= have)
					res = 2;
				else if (A+C <= have)
					res = 2;
				else if (A <= have || C <= have)
					res = 4;
				else
					res = 4;
			}
		}
		else
			res = 2;
		cout << "Case #" << it << ": " << res << '\n';
	}
	return 0;
}
