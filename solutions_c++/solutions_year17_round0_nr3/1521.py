// GCJ Bathroom Stalls.cpp : �������̨Ӧ�ó������ڵ㡣
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
ll n;
ll k;
int main(){
	//freopen("in.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	cin >> t;
	int kase = 0;
	while (t--){
		++kase;
		cin >> n >> k;
		printf("Case #%d: ", kase);
		if (k == 1){
			--n;
			cout << n - n / 2 << " " << n / 2 << endl;
			continue;
		}
		ll n1 = 0, n2 = 0;//ÿ���ж��ٸ��ڵ�
		ll t1 = 0, t2 = 0;//���ж���
		--n;
		n1 = n - n / 2;
		n2 = n / 2;
		t1 = 1, t2 = 0;
		if (n2 == n1)++t1;
		else ++t2;
		--k;
		while (k){
			if (k <= t1 + t2){
				--n1; --n2;
				if (k <= t1){
					cout << n1 - n1 / 2 << " " << n1 / 2 << endl;
				}
				else{
					cout << n2 - n2 / 2 << " " << n2 / 2 << endl;
				}
				break;
			}
			k -= t1 + t2;
			--n1; --n2;
			ll tn1 = max(n1 - n1 / 2, n2 - n2 / 2);
			ll tn2 = min(n1 / 2, n2 / 2);
			ll tt1 = 0, tt2 = 0;
			if (tn1 == n1 / 2)tt1 += t1;
			else tt2 += t1;
			if (tn1 == n1 - n1 / 2)tt1 += t1;
			else tt2 += t1;
			if (tn1 == n2 / 2)tt1 += t2;
			else tt2 += t2;
			if (tn1 == n2 - n2 / 2)tt1 += t2;
			else tt2 += t2;
			n1 = tn1; n2 = tn2;
			t1 = tt1; t2 = tt2;
		}
	}
	return 0;
}