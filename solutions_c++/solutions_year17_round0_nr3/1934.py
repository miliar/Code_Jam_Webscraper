/*************************************************************************
    > File Name: C.cpp
    > Author: wmg_1007
    > Mail: wmg_1007@163.com
    > Created Time: 2017年04月08日 星期六 23时00分42秒
 ************************************************************************/

#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <iomanip>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <deque>
using namespace std;

typedef long long LL;

int main()
{
	int T, caseT = 0;
	cin >> T;
	while (T--) {
		LL n, m;
		cin >> n >> m;
		LL num[2], tot[2];
		num[0] = n, tot[0] = 1;
		num[1] = -1, tot[1] = 0;
		LL ans;
		while (true) {
			if (m <= tot[0] + tot[1]) {
				if (m <= tot[0])
					ans = num[0];
				else
					ans = num[1];
				break;
			}
			m -= tot[0] + tot[1];
			LL tmp_num[2], tmp_tot[2];
			if (num[0] % 2LL == 1LL) {
				tmp_num[0] = num[0] / 2LL;
				tmp_tot[0] = 2LL * tot[0];
				//
				tmp_tot[0] += tot[1];
				tmp_num[1] = num[0] / 2LL - 1LL;
				tmp_tot[1] = tot[1];
			} else {
				tmp_num[0] = num[0] / 2LL;
				tmp_num[1] = num[0] / 2LL - 1LL;
				tmp_tot[0] = tot[0];
				tmp_tot[1] = tot[0];
				//
				tmp_tot[1] += 2LL * tot[1];
			}
			num[0] = tmp_num[0], num[1] = tmp_num[1];
			tot[0] = tmp_tot[0], tot[1] = tmp_tot[1];
		}
		cout << "Case #" << ++caseT << ": " << ans / 2LL << ' ' 
			<< (ans % 2LL == 0LL ? ans / 2LL - 1LL : ans / 2LL) << endl;
	}
	return 0;
}


