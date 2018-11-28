// gcj Stable Neigh-bors.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<algorithm>
using namespace std;
int t;
char co[] = { 'R', 'O', 'Y', 'G', 'B', 'V' };
int c[10];
int n;
int ta[5];
void outa(char a){
	if (a == 'R'){
		if (c[3]>0){
			while (c[3]--){
				printf("RG");
			}
			printf("R");
		}
		else
			printf("R");
	}
	else if (a == 'Y'){
		if (c[5]>0){
			while (c[5]--){
				printf("YV");
			}
			printf("Y");
		}
		else
			printf("Y");
	}
	else{//a=="B"
		if (c[1]>0){
			while (c[1]--){
				printf("BO");
			}
			printf("B");
		}
		else
			printf("B");
	}
}
void out(char a, int an, char b, int bn, char c, int cn){
	int tm = bn + cn - an;
	bn -= tm;
	cn -= tm;
	for (int i = 1; i <= an; ++i){
		outa(a);
		if (i <= tm){
			outa(b);
			outa(c);
		}
		else{
			if (bn){
				outa(b);
				--bn;
			}
			else{
				outa(c);
			}
		}
	}
	printf("\n");
}
int main(){
	//freopen("in.in", "r", stdin);
	//freopen("out2.out", "w", stdout);
	cin >> t;
	int kase = 0;
	while (t--){
		++kase;
		cin >> n;
		bool flag = true;
		bool ff = false;
		for (int i = 0; i < 6; ++i){
			cin >> c[i];
		}
		printf("Case #%d: ", kase);
		for (int i = 1; i < 6&&flag&&!ff; i += 2){
			int con = (i + 3) % 6;
			if (c[i] != 0){
				if (c[con] < c[i])flag = false;
				else if (c[con] == c[i]){
					if (c[con] + c[i] != n)flag = false;
					else{
						//out!
						ff = true;
						for (int j = 1; j <= n; ++j){
							if (j % 2)
								printf("%c",co[i]);
							else
								printf("%c", co[con]);
						}
						printf("\n");
					}
				}
				else{
					c[con] -= c[i];
				}
			}
		}
		if (ff)continue;
		if (!flag)
			printf("IMPOSSIBLE\n");
		else if (c[0] + c[2] < c[4]){
			printf("IMPOSSIBLE\n");
		}
		else if (c[0] + c[4] < c[2]){
			printf("IMPOSSIBLE\n");
		}
		else if (c[2] + c[4] < c[0]){
			printf("IMPOSSIBLE\n");
		}
		else if (c[0] >= c[2] && c[0] >= c[4]){
			if (c[2] >= c[4])
				out(co[0], c[0], co[2], c[2], co[4], c[4]);
			else
				out(co[0], c[0], co[4], c[4], co[2], c[2]);
		}
		else if (c[2] >= c[0] && c[2] >= c[4]){
			if (c[0] >= c[4])
				out(co[2], c[2], co[0], c[0], co[4], c[4]);
			else
				out(co[2], c[2], co[4], c[4], co[0], c[0]);
		}
		else{
			if (c[2] >= c[0])
				out(co[4], c[4], co[2], c[2], co[0], c[0]);
			else
				out(co[4], c[4], co[0], c[0], co[2], c[2]);
		}
	}
	return 0;
}
