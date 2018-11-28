// GCJ Tidy Numbers.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include<cstring>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<iostream>
using namespace std;
const int MAXN = 1e2 + 10;
char s[MAXN];
int t;
int main(){
	//freopen("in.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	int kase = 0;
	cin >> t;
	while (t--){
		cin >> s;
		++kase;
		int len = strlen(s);
		char ti = '0';
		printf("Case #%d: ", kase);
		for (int i = 0; i < len; ++i){
			if (s[i] < ti){
				char tm = s[i - 1];
				int j = i - 1;
				while (j > 0 && s[j - 1] == tm){
					--j;
				}
				--s[j];
				if (s[j] != '0'){
					s[j + 1] = '\0';
					cout << s;
				}
				++j;
				while (j < len){
					cout << 9;
					++j;
				}
				cout << endl;
				break;
			}
			if (i == len - 1){
				cout << s << endl;
				break;
			}
			ti = s[i];
		}
	}
	return 0;
}