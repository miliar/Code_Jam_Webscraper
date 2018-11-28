#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <bitset>
#include <sstream>
#include <queue>

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef long long int64;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const long long inf64 = ((long long)1 << 62) - 1;
const long double pi = acos(-1);

template <class T> T sqr (T x) {return x * x;}
template <class T> T abs (T x) {return x < 0 ? -x : x;}

int main () {
    ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

    int tc;
	cin >> tc;
	for (int ti = 0; ti < tc; ++ti) {
		int n, p;
		cin >> n >> p;

		vector<int> num(p);
		for (int i = 0; i < n; ++i) {
			int val;
			cin >> val;
			++num[val % p];
		}

		int total_mult = 1;
		for (int i = 1; i < p; ++i) {
			total_mult *= num[i] + 1;
		}

		vector<int> res(total_mult, 0);
		res[0] = 0;
		for (int i = 0; i < total_mult; ++i) {
			vector<int> cur_num(p);
			
			int mask = i;
			for (int j = 1; j < p; ++j) {
				cur_num[j] = mask % (num[j] + 1);
				mask /= num[j] + 1;
			}

			int sum = 0;
			for (int j = 1; j < p; ++j) {
				sum += cur_num[j] * j;
			}
			sum %= p;

			for (int j = 1; j < p; ++j) {
				if (cur_num[j] < num[j]) {
					++cur_num[j];

					mask = 0;
					for (int k = p - 1; k >= 1; --k) {
						mask *= num[k] + 1;
						mask += cur_num[k];
					}

				    res[mask] = max(res[mask], res[i] + (sum == 0));
					--cur_num[j];
				}
			}
		}

		cout << "Case #" << ti + 1 << ": " << num[0] + res[total_mult - 1] << endl;
	}

	
	return 0;
}
