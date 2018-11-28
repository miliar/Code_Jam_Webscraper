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
		long long n,k;
		cin >> n >> k;
		cout << "Case #" << test_case + 1 << ": ";
		priority_queue<pair<pair<long long,long long>,pair<long long,long long>>> wow;
		wow.push(make_pair(make_pair(0,0), make_pair(0, n - 1)));
		int cnt = 1;
		while (wow.empty() == false) {
			pair<pair<long long,long long>, pair<long long, long long>> now = wow.top();
			wow.pop();
			int selected = now.second.first + now.second.second;
			selected /= 2;
			if (cnt == k) {
				cout << max(selected - now.second.first,now.second.second - selected) << " " << min(selected - now.second.first, now.second.second - selected) << endl;
				goto ok;
			}
			int tmp[2] = { now.second.first,selected - 1 };
			if (tmp[1] >= 0 &&tmp[0] <= tmp[1] &&(tmp[0] + tmp[1]) / 2 != selected) {
				int next_chosen = (tmp[0] + tmp[1]) / 2;
				wow.push(make_pair(make_pair(min(next_chosen - tmp[0],tmp[1] - next_chosen), max(next_chosen - tmp[0], tmp[1] - next_chosen)), make_pair(tmp[0], tmp[1])));
			}
			tmp[0] = selected + 1;
			tmp[1] = now.second.second;
			if (tmp[0] < n &&tmp[0] <= tmp[1]&&(tmp[0] + tmp[1]) / 2 != selected) {
				int next_chosen = (tmp[0] + tmp[1]) / 2;
				wow.push(make_pair(make_pair(min(next_chosen - tmp[0], tmp[1] - next_chosen), max(next_chosen - tmp[0], tmp[1] - next_chosen)), make_pair(tmp[0], tmp[1])));
			}
			cnt++;
		}
	ok:;
	}
}