#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int T,R,C;
char arr[30][30];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> T;
	for (int now_case = 1;now_case <= T;++now_case) {
		memset(arr, 0, sizeof(arr));
		arr[0][0] = '1';
		int first = 30;
		cin >> R >> C;
		for (int i = 1;i <= R;++i) {
			char(&now)[30] = arr[i];
			int numq = 0;
			int last = 0;
			for (int j = 1;j <= C;++j) {
				cin >> now[j];
				if (now[j] == '?') {
					++numq;
				}
				else {
					last = j;
					for (int k = j - 1;now[k]=='?'&&k != 0;--k) {
						now[k] = now[j];
					}
				}
			}
			if (numq == C) {
				if (arr[i-1][0]!='1') {
					char(&pre)[30] = arr[i-1];
					for (int l = 1;l <= C;++l) {
						now[l] = pre[l];
					}
				}
				else {
					now[0] = '1';
				}
				continue;
			}
			if (first ==30) first = i;
			for (int k = last+1;k<=C;++k) {
				now[k] = now[last];
			}
		}
		if (first !=30) {
			for (int i = first - 1;i != 0;--i) {
				for (int j = 1;j <= C;++j) {
					arr[i][j] = arr[first][j];
				}
			}
		}
		cout << "Case #" << now_case << ": \n";
		for (int i = 1;i <= R;++i) {
			for (int j = 1;j <= C;++j) {
				cout << arr[i][j];
			}
			cout << '\n';
		}
	}
	return 0;
}