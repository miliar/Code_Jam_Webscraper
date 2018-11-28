//============================================================================
// Name        : A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <set>
#include <iostream>
#define max(x,y) ((x)>(y)?(x):(y))
#define min(x,y) ((x)<(y)?(x):(y))
#define MAXN 100050
#define LL long long
using namespace std;
int N, P;
int a[1111];
int cal2() {
	int res = 0;
	int cnt = 0;
	for (int i = 0; i < N; ++i)
		if (a[i] & 1)
			cnt++;
		else
			res++;
	res += (cnt + 1) / 2;
	return res;
}
int cal3() {
	int res = 0;
	int cnt1 = 0;
	int cnt2 = 0;
	for (int i = 0; i < N; ++i) {
		if (a[i] % 3 == 0)
			res++;
		else if (a[i] % 3 == 1)
			cnt1++;
		else
			cnt2++;
	}
	if (cnt1 > cnt2)
		swap(cnt1, cnt2);
	res += cnt1;
	cnt2 -= cnt1;
	res += (cnt2 + 2) / 3;
	return res;
}
int dp[101][101][101];
int cal4() {
	int cnt[5];
	memset(cnt,0,sizeof(cnt));
	for (int i = 0; i < N; ++i)
		cnt[a[i] % 4]++;
	for (int i = cnt[1]; i >= 0; --i) {
		for (int j = cnt[2]; j >= 0; --j) {
			for (int k = cnt[3]; k >= 0; --k) {
				dp[i][j][k] = 0;
			}
		}
	}
	int maxn=0;
	for (int i = cnt[1]; i >= 0; --i) {
		for (int j = cnt[2]; j >= 0; --j) {
			for (int k = cnt[3]; k >= 0; --k) {

				maxn=max(maxn,dp[i][j][k]);
				if(i!=0||j!=0||k!=0)
					maxn=max(maxn,dp[i][j][k]+1);
				if(j>=2)dp[i][j-2][k]=max(dp[i][j-2][k],dp[i][j][k]+1);
				if(i>=1&&k>=1)dp[i-1][j][k-1]=max(dp[i-1][j][k-1],dp[i][j][k]+1);

				if(i>=2&&j>=1)dp[i-2][j-1][k]=max(dp[i-2][j-1][k],dp[i][j][k]+1);
				if(k>=2&&j>=1)dp[i][j-1][k-2]=max(dp[i][j-1][k-2],dp[i][j][k]+1);

				if(i>=4)dp[i-4][j][k]=max(dp[i-4][j][k],dp[i][j][k]+1);
				if(k>=4)dp[i][j][k-4]=max(dp[i][j][k-4],dp[i][j][k]+1);
			}
		}
	}
	return maxn+cnt[0];
}
int main() {
	freopen("A-large (1).in","r",stdin);
	freopen("A-large (1).out","w",stdout);
	int tt, ri = 0;
	scanf("%d", &tt);
	while (tt--) {
		scanf("%d%d", &N, &P);
		for (int i = 0; i < N; ++i)
			scanf("%d", &a[i]);
		int ans;
		if (P == 2)
			ans = cal2();
		else if (P == 3)
			ans = cal3();
		else
			ans = cal4();
		printf("Case #%d: %d\n", ++ri, ans);
	}
	return 0;
}
