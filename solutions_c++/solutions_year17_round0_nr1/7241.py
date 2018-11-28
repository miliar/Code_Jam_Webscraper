/*
 * pancake.cpp
 *
 *  Created on: Apr 8, 2017
 *      Author: dtran080
 */
#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

void flip(char s[],int pos, int k){
	for (int i=0;i<k;i++){
		s[pos+i]=(s[pos+i]=='-')?'+':'-';
	}
}
bool isHappy(char s[]){
	for (int i=0;i<strlen(s);i++){
		if (s[i]=='-') return false;
	}
	return true;
}
/*void printCake(char s[]){
	for (int i=0;i<strlen(s);i++){
		printf("%c",s[i]);
	}
	printf("\n");
}*/
int main(){
	int T,K;
	char s[1001];
	int flipCount;
	bool happy = false;
	scanf("%d\n",&T);
	for (int i=1;i<=T;i++){
		scanf("%[+-]s ",&s);
		scanf("%d\n",&K);
		flipCount = 0;
		happy = false;
		/*printf("%s %d\n",s,K);*/
		for (int j=0;j<=strlen(s)-K;j++){
			if (s[j]=='-'){
				flip(s,j,K);
				flipCount++;
			}
//			printCake(s);
			if (isHappy(s)){
				happy = true;
				break;
			}
		}
		printf("Case #%d: ",i);
		if (happy) printf("%d\n",flipCount);
		else printf("Impossible\n");
	}
	return 0;
}




