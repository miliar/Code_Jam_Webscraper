#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <utility>
#include <algorithm>
using namespace std;

int const INT_INF = 1000000000;

char st[128];
int dp[2][128][10][2];

int calc_dp(string st, int first_dg, int index, int allow_first_zeros) {
	int n = (int) st.length();

	for (int i=0; i<=n; i++)
		for (int ldg=0; ldg<10; ldg++)
			for (int eq_st=0; eq_st<2; eq_st++)
				dp[index][i][ldg][eq_st] = 0;
	
	dp[index][0][first_dg][1] = 1;

	for (int i=0; i<n; i++)
		for (int ldg=0; ldg<10; ldg++)
			for (int eq_st=0; eq_st<2; eq_st++)
				if (dp[index][i][ldg][eq_st]) {
					int c = 0;
					if (ldg <= 0 && !allow_first_zeros)
						c = 1;

					int d = 9;
					if (eq_st) d = st[i]-'0';
					
					for (int ndg=c; ndg<=d; ndg++)
						if (ndg >= ldg) {
							int new_eq_st = eq_st;
							if (ndg != st[i]-'0') new_eq_st = 0;
							dp[index][i+1][ndg][new_eq_st] = 1;
						}
				}

	int ldg_from = 0;
	if (!allow_first_zeros)
		ldg_from = 1;

	for (int ldg=ldg_from; ldg<10; ldg++)
		for (int eq_st=0; eq_st<2; eq_st++)
			if (dp[index][n][ldg][eq_st])
				return 1;

	return 0;
}

int is_non_zero(string st) {
	for (int i=0; i<(int) st.length(); i++)
		if (st[i] != '0')
			return 1;
	return 0;
}

string calc_ans(string st) {
	int n = (int) st.length();
	int is_ans = calc_dp(st, 0, 0, 0);

	string ans = "";

	if (!is_ans) {
		for (int i=0; i<n-1; i++) ans += (char) '9';
		return ans;
	}

	int ldg = 0;
	int eq_st = 1;

	for (int i=0; i<n; i++) {
		int c = 0;
		int d = 9;
		if (eq_st) d = st[i]-'0';
		for (int ndg=d; ndg>=c; ndg--)
			if (ndg >= ldg) {
				int new_eq_st = eq_st;
				if (ndg != st[i]-'0') new_eq_st = 0;

				if (dp[0][i+1][ndg][new_eq_st]) {
					string tmp = "";
					if (new_eq_st)
						for (int j=i+1; j<n; j++) tmp += st[j];
					else
						for (int j=i+1; j<n; j++) tmp += (char) '9';

					string tmp_ans = ans;
					tmp_ans += (char) ('0' + ndg);

					if (calc_dp(tmp, ndg, 1, is_non_zero(tmp_ans))) {
						ans += (char) ('0' + ndg);
						ldg = ndg;
						eq_st = new_eq_st;
						break;
					}
				}
			}
	}

	return ans;
}

//int slow_prec = 0;
//char slow_ms[11000000];
//string slow_solve(string st) {
//	long long n = 0;
//	for (int i=0; i<(int) st.length(); i++)
//		n = n*10 + (st[i]-'0');
//	
//	char tmp_st[25];
//
//	if (n < 11000000) {
//		if (!slow_prec) {
//			for (int i=0; i<11000000; i++) {
//				slow_ms[i] = 1;
//				sprintf(tmp_st,"%d",i);
//				for (int j=1; tmp_st[j]; j++)
//					if (tmp_st[j-1] > tmp_st[j]) {
//						slow_ms[i] = 0;
//						break;
//					}
//			}
//			slow_prec = 1;
//		}
//
//		int x = n;
//		while (x >= 1 && !slow_ms[x]) x--;
//		sprintf(tmp_st,"%d",x);
//		return tmp_st;
//	}
//
//	while (n >= 1) {
//		int is_Ok = 1;
//		sprintf(tmp_st,"%lld",n);
//		for (int j=1; tmp_st[j]; j++)
//			if (tmp_st[j-1] > tmp_st[j]) {
//				is_Ok = 0;
//				break;
//			}
//		if (is_Ok) {
//			sprintf(tmp_st,"%lld",n);
//			return tmp_st;
//		}
//		n--;
//	}
//}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	gets(st);
	int t;
	sscanf(st,"%d",&t);
	for (int q=1; q<=t; q++) {
		gets(st);
		printf("Case #%d: ",q);
		printf("%s\n",calc_ans(st).c_str());
	}
	return 0;
}
