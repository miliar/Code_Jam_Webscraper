// GCJ 2017.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<queue>
#include<map>
#include<vector>
using namespace std;
int n, p;
const int MAXN = 1e2 + 10;
int a[MAXN];
int tn[5];
int main(){
	//freopen("in.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	int t;
	cin >> t;
	int kase = 0;
	while (t--){
		++kase;
		memset(tn, 0, sizeof tn);
		cin >> n >> p;
		for (int i = 1; i <= n; ++i){
			cin >> a[i];
			a[i] %= p;
			tn[a[i]]++;
		}
		int ans = tn[0];
		tn[0] = 0;
		for (int i = 1; i < p; ++i){
			int tmp = min(tn[i], tn[p - i]);
			if (i == p - i){
				tmp = tn[i] / 2;
				tn[i] %= 2;
			}
			else{
				tn[i] -= tmp;
				tn[p - i] -= tmp;
			}
			ans += tmp;
		}
		if (p == 2){
			ans += tn[1];
		}
		else if (p == 3){
			ans += tn[1] / 3 + ((tn[1] % 3) ? 1 : 0);
			ans += tn[2] / 3 + ((tn[2] % 3) ? 1 : 0);
		}
		else{
			if (tn[2] == 0){
				ans += tn[1] / 4 + ((tn[1] % 4) ? 1 : 0);
				ans += tn[3] / 4 + ((tn[3] % 4) ? 1 : 0);
			}
			else{
				if (tn[1]){
					ans += (tn[2] * 2 + tn[1]) / 4 + (tn[2] * 2 + tn[1]) % 4;
				}
				else if (tn[3]){
					ans += (2 + tn[3]) / 4 + (((2 + tn[3]) % 4) ? 1 : 0);
				}
				else{
					ans += tn[2];
				}
			}
		}
		printf("Case #%d: %d\n", kase, ans);
	}
	return 0;
}