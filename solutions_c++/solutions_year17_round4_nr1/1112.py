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
#include <stdlib.h>
#include <list>
#include <typeinfo>
#include <list>
#include <set>
#include <fstream>
using namespace std;
#define eps 0.000000001
#define LONG_INF 10000000000000000
#define GOLD 1.61803398874989484820458
#define MAX_MOD 1000000007
#define REP(i,n) for(long long i = 0;i < n;++i)
int main() {
#define int long long
	int test_case;
	cin >> test_case;
	REP(tester, test_case) {
		int n, p;
		cin >> n >> p;
		map<int, int> hoge;
		int ans = 0;
		REP(i, n) {
			int a;
			cin >> a;
			hoge[a%p]++;
		}
		ans = hoge[0];
		if (p == 2) {
			ans += (hoge[1]+1) / 2;
		}
		else if (p == 3) {
			int nya = min(hoge[1], hoge[2]);
			hoge[1] -= nya;
			hoge[2] -= nya;
			ans += nya;
			ans += (hoge[1] + hoge[2]+2) / 3;
		}
		else if(p == 4) {
			int nya = hoge[2] / 2;
			ans += nya;
			hoge[2] -= nya * 2;
			nya = min(hoge[1], hoge[3]);
			hoge[1] -= nya;
			hoge[3] -= nya;
			ans += nya;
			if (hoge[2] % 2 == 0) {
				ans += (hoge[1] + hoge[3] + 3) / 4;
			}
			else {
				int mew = (hoge[1] + hoge[3]);
				ans++;
				mew -= 2;
				if (mew >= 0) {
					ans += (mew + 3) / 4;
				}
			}
		}
		cout << "Case #" << tester+1 << ": " << ans << endl;
	}
}