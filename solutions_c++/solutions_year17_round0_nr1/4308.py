#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

char str[1002];

int findMinFlips(int);
void printOutput(int,int);
void flipString(int,int);

int main(){
	int T, K;
	scanf("%d", &T);
	for(int i=1;i<=T;i++){
		scanf("%s", str);
		scanf("%d", &K);
		int min = findMinFlips(K);
		printOutput(i,min);
	}
}

int findMinFlips(int K){
	int len = strlen(str);
	int min = 0;

	for(int i=1;i<=len;i++){
		if(str[i-1] == '-'){
			if(len-i+1 < K)
				return -1;
			else{
				min++;
				flipString(i,K);
			}				
		}
	}

	return min;
}


void flipString(int i, int K){
	for(int j = 0; j< K;j++){
		if(str[i-1+j] == '+')
			str[i-1+j] = '-';
		else
			str[i-1+j] = '+';
	}
}

void printOutput(int i, int min){
	printf("Case #%d: ", i);
	if(min == -1)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", min);
}
