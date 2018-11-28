// 2017codeJamRound1A.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"

#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

char m[50][50];

int main(){
	//freopen("D:\\A-large.in", "r+", stdin);
	//freopen("D:\\output.txt", "w+", stdout);


	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++){
		printf("Case #%d:\n", cases);
		int r, c;
		scanf("%d%d", &r, &c);
		for (int i = 0; i < r; i++){
			scanf("%s", m[i]);
		}
		int flag[50] = { 0 };
		for (int i = 0; i < r; i++){

			for (int j = 0; j < c; j++){
				if (m[i][j] == '?'){
					continue;
				}
				flag[i] = 1;
				for (int k = 1; j - k >= 0; k++){
					if (m[i][j - k] == '?'){
						m[i][j - k] = m[i][j];
					}
					else{
						break;
					}
				}
				for (int k = 1; j + k <c; k++){
					if (m[i][j + k] == '?'){
						m[i][j + k] = m[i][j];
					}
					else{
						break;
					}
				}
			}
		}
		for (int i = 0; i < r; i++){
			if (flag[i] == 0){
				if (i == 0){
					int pos = 0;
					while (flag[pos] == 0){
						pos++;
					}
					for (int j = 0; j < c; j++){
						m[i][j] = m[pos][j];
					}
				}
				else{
					for (int j = 0; j < c; j++){

						m[i][j] = m[i - 1][j];
					}
				}
			}
		}
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				printf("%c", m[i][j]);
			}
			printf("\n");
		}




	}

	//system("pause");
	return 0;
}