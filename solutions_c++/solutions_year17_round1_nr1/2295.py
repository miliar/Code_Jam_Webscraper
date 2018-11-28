//AnotherHackyCodeBySmartCoder
//AlphabetCake.cpp
//Apr 14, 2017
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end();i++)
#define present(c,x)  ( (c).find(x) !=(c).end())
#define cpresent(c,x) (find(all(c),x)!= (c).end() )
#define minei(x)  min_element(x.begin(),x.end())-(x).begin()
#define maxei(x)  max_element(x.begin(),x.end())-(x).begin()

#define uns(v)     sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define acusum(x)  accumulate(x.begin(),x.end(),0)
#define acumul(x)  accumulate(x.begin(),x.end(),1, multiplies<int>());
#define bits(x)     __builtin_popcount( x )
#define oo INT_MAX
#define inf 1000000000

const double pi = acos(-1.0);
const double eps = 1e-11;
#define MAXN 1000007
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
void fastIO() {
	std::ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
}
char mat[30][30];
void clearMe() {
	for (int i = 0; i < 30; i++)
		for (int j = 0; j < 30; j++)
			mat[i][j] = '*';
}

int main() {
	fastIO();
	freopen("A-large.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	int tc, r, c, indx, st, en;
	bool isGood;
	char cur;
	cin >> tc;
	for (int t = 1; t <= tc; t++) {
		clearMe();
		cin >> r >> c;
		for (int i = 1; i <= r; i++)
			for (int j = 1; j <= c; j++)
				cin >> mat[i][j];

		for (int i = 1; i <= r; i++) {
			for (int j = 1; j <= c; j++) {
				if (mat[i][j] == '?')
					continue;
				cur = mat[i][j];
				indx = j + 1;

				while (indx <= c) {
					if (mat[i][indx] == '?')
						mat[i][indx] = cur;
					else
						break;
					indx++;
				}
				indx = j - 1;
				while (indx >= 1) {
					if (mat[i][indx] == '?')
						mat[i][indx] = cur;
					else
						break;
					indx--;
				}
			}
		}
		map<char, bool> done;
		for (int i = 1; i <= r; i++) {
			for (int j = 1; j <= c; j++) {
				cur = mat[i][j];
				if (cur != '?' && !done.count(cur)) {
					done[mat[i][j]] = true;

					st = en = j;
					while (mat[i][st] == cur)
						st--;

					while (mat[i][en] == cur)
						en++;
					en--;
					st++;
					indx = i - 1;
					while (indx >= 1) {
						isGood = true;
						for (int k = st; k <= en; k++) {
							if (mat[indx][k] != '?') {
								isGood = false;
								break;
							}
						}
						if (isGood) {
							for (int k = st; k <= en; k++)
								mat[indx][k] = cur;
						} else {
							break;
						}
						indx--;
					}
					indx = i + 1;
					while (indx <= r) {
						isGood = true;

						for (int k = st; k <= en; k++) {
							if (mat[indx][k] != '?') {
								isGood = false;
								break;
							}
						}
						if (isGood) {
							for (int k = st; k <= en; k++)
								mat[indx][k] = cur;
						} else {
							break;
						}
						indx++;
					}
				}
			}
		}
		cout << "Case #" << t << ":" << endl;

		for (int i = 1; i <= r; i++) {
			for (int j = 1; j <= c; j++)
				cout << mat[i][j];
			if (i == r && t == tc)
				continue;
			cout << endl;
		}
	}

	return 0;
}
