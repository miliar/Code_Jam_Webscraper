#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>
#include <ctime>


typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;
using namespace std;

int main() {
	FILE *stream;
	//freopen_s(&stream, "A_small.in", "r", stdin);
	//freopen_s(&stream, "A_small.out", "w", stdout);
	freopen_s(&stream, "A_large.in", "r", stdin);
	freopen_s(&stream, "A_large.out", "w", stdout);
	int T;
	string str;
	int l;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> str >> l;
		cout << "Case #" << (i + 1) << ": ";
		int res = 0;
		int strlen = str.size();
		if (l > strlen) l = strlen;
		int skip = 0;
		for (int j = 0; j <= strlen - l; j++) {
			if (str[j] == '-') {
				res++;
				for (int k = j; k < j + l; k++) {
					if (str[k] == '-') {
						str[k] = '+';
					} else str[k] = '-';
				}
			}
			if (j == strlen - l) {
				for (int k = j; k < j + l; k++) {
					if (str[k] == '-') {
						cout << "IMPOSSIBLE" << endl;
						skip = 1;
						break;
					}
				}
			}
		}
		if (!skip) cout << res << endl;
	}

	return 0;
}