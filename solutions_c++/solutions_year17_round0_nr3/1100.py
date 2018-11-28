// C.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <map>
using namespace std;


int main(){
	//freopen("D:\\C-large.in", "r+", stdin);
	//freopen("D:\\output.txt", "w+", stdout);
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++){
		printf("Case #%d: ", cases);
		__int64 N, K;
		scanf("%I64d%I64d", &N, &K);
		__int64 base = 1;
		__int64 sum = 0;
		__int64 maxnum = N;
		__int64 minum = N;
		__int64 maxcnt = 1;
		__int64 mincnt = 0;
		while (true){
			if (sum + base >= K){
				__int64 tmp = K-sum;
				if (tmp <= maxcnt){
					printf("%I64d %I64d\n", maxnum / 2, (maxnum - 1) / 2);
				}
				else{
					printf("%I64d %I64d\n", minum / 2, (minum - 1) / 2);
				}
				break;
			}

			sum += base;
			base *= 2;

			__int64 maxnum_max = maxnum / 2;
			__int64 maxnum_min = (maxnum - 1) / 2;
			__int64 minum_max = minum / 2;
			__int64 minum_min = (minum - 1) / 2;
			__int64 tmpmax = maxnum_max;
			__int64 tmpmaxcnt = maxcnt;
			__int64 tmpmin = minum_min;
			__int64 tmpmincnt = mincnt;
			if (maxnum_min == tmpmax){
				tmpmaxcnt += maxcnt;
			}
			if (minum_max == tmpmax){
				tmpmaxcnt += mincnt;
			}
			if (maxnum_min == tmpmin){
				tmpmincnt += maxcnt;
			}
			if (minum_max == tmpmin){
				tmpmincnt += mincnt;
			}
			if (maxnum_max == minum_min){
				tmpmincnt = 0;
				tmpmaxcnt = 2 * (maxcnt + mincnt);
			}
			maxnum = tmpmax;
			maxcnt = tmpmaxcnt;
			minum = tmpmin;
			mincnt = tmpmincnt;
		}

	}
	return 0;
}