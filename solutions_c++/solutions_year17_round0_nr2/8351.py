#pragma once

#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;


int Test,MySize;
char Mozi[10] = {'0','1','2','3','4','5','6','7','8','9'};
long long int result=0;
int num[21];
bool MyEnd[2] = {};
char c[21] = {};
string S;

FILE *file;
FILE *fp;


int main() {



	fp = fopen("answer5_5.txt", "r");
	file = fopen("answer4_1.txt", "w");

	fscanf(fp, "%d", &Test);

	//cin >> Test;

	


	for (int aa = 0; aa < Test;aa++) {

		for (int i = 0; i < 21; i++) {
			c[i] = 'a';
		}
		
		S = "";

		fscanf(fp, "%s", c);

		for (int i = 0;i<21; i++) {
			if (c[i] == 'a') {
				MySize = i-1;
				break;
			}
		}

		for (int i = 0;i<MySize; i++) {
			for (int j = 0; j < 10; j++) {
				if (c[i] == Mozi[j]) {
					num[i] = j;
					break;
				}
			}
		}


		for (int i = MySize-1; i>=1; i--) {
			if(num[i]<num[i-1]){
				num[i - 1]--;
				for(int j=i;j<MySize;j++){
					num[j] = 9;
				}
			}
		}

		if (num[0] != 0) {
			for (int j = 0; j < 10; j++) {
				if (num[0] == j) {
					S += Mozi[j];
					break;
				}
			}
		}

		for (int i = 1; i<MySize; i++) {
			for (int j = 0; j < 10; j++) {
				if (num[i] == j) {
					S+= Mozi[j];
					break;
				}
			}
		}
	
		result = stoll(S.c_str());

		//cin >> S >> K;
		
	

			printf("Case #%d: %lld\n", aa + 1, result);
			fprintf(file, "Case #%d: %lld\n", aa + 1, result);
		
	
	}

	fclose(fp);
	fclose(file);

	return 0;
}


