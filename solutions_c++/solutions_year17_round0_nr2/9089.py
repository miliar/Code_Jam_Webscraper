#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <stdbool.h>
#include <string>
#include <queue>

#define MAXLINE 21

void flip(int, int);
int readInput();
int findIncon(int);
bool isAllOne(int);
void printNines(int len);
void flip(int from, int to);
void printTidy(int len);

int inputNum[20] = {0};

int main(int argc, char * argv[]){
	int numTest = 0;
	scanf("%d",&numTest);
	getchar();
	int i = 0;
	while(i < MAXLINE){
		inputNum[i] = -1;
		i += 1;
	}

	int testCount = 0;
	while(testCount < numTest){
		printf("Case #%d: ",testCount + 1);
		int len = readInput();
		if(len == 1){
			printf("%d\n",inputNum[0]);
		}else if(isAllOne(len)){
			printNines(len);
		}else{
			int incon = findIncon(len);
			if(incon != -1){
				flip(incon, len -1);
			}
			printTidy(len);
		}
		testCount += 1;
	}
}

int readInput(){
	int length = 0;
	std::queue<int> q;
	char c = 0;
	while((c = getchar()) != '\n'){
		int num = c - '0';
		q.push(num);
	}

	length = q.size();
	int i = 0;
	while(!q.empty()){
		inputNum[i] = q.front();
		q.pop();
		i += 1;
	}

	return length;
}


int findIncon(int len){
	int i = 0;
	while(i < len - 1){
		if(inputNum[i] > inputNum[i+1]){
			int inconNum = inputNum[i];
			int j = 0;
			while(inputNum[j] != inconNum)
				j += 1;
			return j;
		}
		i += 1;
	}

	return -1;
}

bool isAllOne(int len){
	int i = 0;
	if(inputNum[len-1] != 0){
		return false;
	}
	bool oneFlag = true; //are we still parsing 1?
	bool zeroFlag = false; // are we still parsing 0?
	while(i < len){
		if(inputNum[i] != 1 && inputNum[i] != 0){
			return false;
		}
		if(oneFlag){
			if(inputNum[i] == 0){
				zeroFlag = true;
			}
		}else if(zeroFlag){ //now we expect only zeros
			if(inputNum[i] != 0){
				return false;
			}
		}

		i += 1;
	}

	return true;
}

void printNines(int len){
	int i = 0;
	while(i < len-1){
		printf("9");
		i += 1;
	}
	printf("\n");
}

void flip(int from, int to){
	int i = from + 1;
	inputNum[from] -= 1;
	while(i <= to){
		inputNum[i] = 9;
		i += 1;
	}
}

void printTidy(int len){
	int i = 0;
	while(inputNum[i] == 0){
		i += 1;
	}
	for(; i < len; i += 1){
		printf("%d",inputNum[i]);
	}
	printf("\n");
}