// B.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
using namespace std;

char str[100];
int main(){
	//freopen("D:\\B-small-attempt0.in", "r+", stdin);
	//freopen("D:\\output.txt", "w+", stdout);
	int T;
	scanf("%d", &T);

	for (int cases = 1; cases <= T; cases++){
		printf("Case #%d: ", cases);
		scanf("%s", str);
		int len = strlen(str);
		char pre = '9';
		int pos = len;
		for (int i = len - 1; i >= 0; i--){
			if (str[i] > pre){
				str[i]--;
				pos = i;
			}
			pre = str[i];
		}
		int lead_zero = str[0]=='0'?1:0;
		for (int i = 0; i < len; i++){
			if (i > pos){
				printf("9");
				continue;
			}
			if (lead_zero == 1){
				if (str[i] == '0'){
					continue;
				}
				else{
					lead_zero = 0;
					printf("%c", str[i]);
				}
			}
			else{
				printf("%c", str[i]);
			}
		}
		printf("\n");
	}
	return 0;
}