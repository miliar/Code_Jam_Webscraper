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
using namespace std;
#define LONG_INF 10000000000000000
#define MAX_MOD 1000000007
#define REP(i,n) for(long long i = 0;i < n;++i)
int main() {
	int t;
	cin >> t;
	REP(test_case, t) {
		double a;
		cin >> a;
		int n;
		cin >> n;
		double time = 0;
		REP(i, n) {
			double c, d;
			cin >> c >> d;
			time = max(time, (a - c) / d);
		}
		cout << "Case #" << test_case+1 << ": ";
		cout <<fixed << setprecision(10) << a / time << endl;
	}
}