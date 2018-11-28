#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

char str[30];

void findLastTidy();
void outputLastTidy(int);
int findFirstMismatch();

int main(){
	int T;
	scanf("%d", &T);
	
	for(int i=1;i<=T;i++){
		scanf("%s", str);
		findLastTidy();
		outputLastTidy(i);
	}
}

void findLastTidy(){

	int i = findFirstMismatch();
	if(i != -1){
		int len = strlen(str);
		str[i] = str[i] - 1;
		for(int j=i+1; j<len;j++)
			str[j] = '9';	
		findLastTidy();
	}
}

int findFirstMismatch(){
	
	char last = str[0];
	int len = strlen(str);

	for(int j=1;j<len;j++){
		if(last > str[j])
			return j-1;
		last = str[j];
	}

	return -1;
}

void outputLastTidy(int i){
	
	printf("Case #%d: ", i);

	int len = strlen(str);
	int j = 0;

	while(str[j] == '0'){
		j++;
	}

	for(;j<len;j++){
		printf("%c",str[j]); 
	}
	printf("\n");
}
