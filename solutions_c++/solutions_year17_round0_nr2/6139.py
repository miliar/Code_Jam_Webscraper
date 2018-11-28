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
		string number;
		cin >> number;

		while (true) {
			bool repeat = false;

			for (int i = 0; i < number.size() - 1; i++) {
				if (number[i] > number[i + 1]) {
					if (number[i] != '0') {
						number[i]--;
						for (int j = i + 1; j < number.size(); ++j) {
							number[j] = '9';
						}
					}
					else {
						for (int j = i - 1; j >= 0; --j) {
							if (number[j] != '0') {
								number[j]--;
								for (int k = j + 1; k < number.size(); ++k) {
									number[k] = '9';
								}

								break;
							}
						}
					}

					repeat = true;
					break;
				}
			}
			if (repeat) continue;
			break;
		}
		
		reverse(all(number));
		while (number.back() == '0') number.pop_back();
		reverse(all(number));


		cout << "Case #" << tc + 1 << ": " << number;

		cout << endl;
	}

	return 0;
}