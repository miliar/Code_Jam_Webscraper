// gcj Cruise Control.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<algorithm>
using namespace std;
typedef long long ll;
int t;
const int MAXN = 2e3 + 10;
ll ki[MAXN];
ll d;
ll si[MAXN];
int n;
int main(){
	//freopen("in.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	int kase = 0;
	cin >> t;
	while (t--){
		++kase;
		cin >> d >> n;
		double ti = 0;
		for (int i = 1; i <= n; ++i){
			cin >> ki[i] >> si[i];
			ti = max(ti, (d - ki[i])*1.0 / si[i]);
		}
		double sp = d / ti;
		printf("Case #%d: %.8f\n", kase, sp);
	}
	return 0;
}