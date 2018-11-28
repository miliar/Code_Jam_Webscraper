#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <cstdio>
#include <map>
#include <unordered_map>
#include <string>
#include <iomanip>
#include <vector>
#include <memory.h>
#include <queue>
#include <set>
#include <unordered_set>
#include <stack> 
#include <algorithm>
#include <math.h>
#include <sstream>
#include <functional>
#include <bitset>
using namespace std;
#define mems(A, val) memset(A, val, sizeof(A))
#define mp(a, b) make_pair(a, b)
#define all(B) (B).begin(), (B).end()
#define forn(it, from, to) for(int it = from; it < to; ++it)
#define forit (it, coll) for(auto it = coll.begin(); it != coll.end(); ++it)
#define sz(a) (int)a.size()
#define pb push_back
const int MAXN = 2 * 1000 * 100 + 10;
const double EPS = 1e-9;
typedef long long LL;
const LL MOD = 1000 * 1000 * 1000 + 7;



int main(int argc, char* argv[]) {

#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen("data.in", "r", stdin); freopen("data.out", "w", stdout);
#endif
	ios::sync_with_stdio(0);
	cin.tie();
	
	int tcs;
	cin >> tcs;

	forn(tc, 0, tcs) {
		int ans = 0;

		string s;
		cin >> s;
		int k;
		cin >> k;

		int count = 0;
		for (int i = 0; i + k - 1< s.size(); ++i) {
			if (s[i] == '-'){
				for (int j = 0; j < k; ++j) {
					s[i+j] = s[i+j] == '-' ? '+' : '-';
				}

				count++;
			}
		}

		int minus = 0;
		for (int i = 0; i < s.size(); ++i) {
			minus += s[i] == '-';
		}

		if (minus != 0) {
			cout << "Case #" << tc + 1 << ": " << "Impossible";
		}
		else {
			cout << "Case #" << tc + 1 << ": " << count;
		}

		cout << endl;
	}

	return 0;
}