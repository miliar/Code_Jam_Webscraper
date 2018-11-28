#define  _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>
#include <utility>
#include <functional>
#include <cstring>
#include <queue>
#include <stack>
#include <math.h>
#include <iterator>
#include <vector>
#include <string>
#include <set>
#include <math.h>
#include <iostream> 
#include<map>
#include <iomanip>
#include <time.h>
#include <random>
#include <stdlib.h>
#include <list>
#include <typeinfo>
#include <list>
#include <set>
using namespace std;
#define LONG_INF 10000000000000000
#define MAX_MOD 1000000007
#define REP(i,n) for(long long i = 0;i < n;++i)
int main() {
	int t;
	cin >> t;
	REP(test_case, t) {
		string s;
		cin >> s;
		int k;
		int cnt = 0;
		cin >> k;
		for (int i = 0;i < s.length() - k+1;++i) {
			if (s[i] == '-') {
				cnt++;
				for (int q = 0;q < k;++q) {
					if (s[i + q] == '-') {
						s[i + q] = '+';
					}
					else {
						s[i + q] = '-';
					}
				}
			}
		}
		cout << "Case #" << test_case + 1 << ": ";
		for (int i = 0;i < s.length();++i) {
			if (s[i] == '-') {
				cout << "IMPOSSIBLE" << endl;
				goto ok;
			}
		}
		cout << cnt << endl;
	ok:;
	}
}