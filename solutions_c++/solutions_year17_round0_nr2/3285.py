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
		cout << "Case #" << test_case + 1 << ": ";
		string n;
		cin >> n;
		string ans;
		for (int i = 0;i < n.length();++i) {
			for (int q = i;q < n.length();++q) {
				if (n[i] > n[q]) {
					ans.push_back(n[i] - 1);
					for (int j = i + 1;j < n.length();++j) {
						ans.push_back('9');
					}
					goto ok;
				}
				else if (n[i] < n[q]) {
					goto win;
				}
			}
		win:;
			ans.push_back(n[i]);
		}
	ok:;
		long long gya = stoll(ans);
		cout << gya << endl;
	}
}