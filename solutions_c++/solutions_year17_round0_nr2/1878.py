/*************************************************************************
    > File Name: B.cpp
    > Author: wmg_1007
    > Mail: wmg_1007@163.com
    > Created Time: 2017年04月08日 星期六 22时10分06秒
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

string S, ans;
int L;

int main()
{
	int T, caseT = 0;
	cin >> T;
	while (T--) {
		cin >> S;
		while (S[0] < '0' || S[0] > '9')
			cin >> S;
		L = S.size();
		ans = "";
		bool succ = false;
		for (int i = 0; i < L - 1; i++) {
			if (S[i] > S[i + 1]) {
				succ = true;
				S[i]--;
				int pos = i;
				while (pos > 0 && S[pos - 1] > S[pos])
					S[--pos]--;
				i = pos;
				if (S[0] == '0')
					for (int j = 0; j < L - 1; j++)
						ans.insert(0, "9");
				else {
					for (int j = 0; j <= i; j++)
						ans.insert(j, S.substr(j, 1));
					for (int j = i + 1; j < L; j++)
						ans.insert(j, "9");
				}
				break;
			}
		}
		if (!succ)
			ans = S;
		cout << "Case #" << ++caseT << ": " << ans << endl;
	}
	return 0;
}



