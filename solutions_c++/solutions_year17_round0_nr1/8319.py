#pragma once

#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;


int Test,K;
string S;
int Mozi[1000];
int result=0;
bool MyEnd[2] = {};

FILE *file;
FILE *fp;


int main() {



	fp = fopen("answer5_5.txt", "r");
	file = fopen("answer4_1.txt", "w");

	//fscanf(fp, "%d", &Test);

	cin >> Test;

	string mainas = "-";
	string purasu = "+";



	for (int aa = 0; aa < Test;aa++) {

		//fscanf(fp, "%s%d", &S,&K);

		result = 0;
		MyEnd[0] = false;
	
		cin >> S >> K;
		
		for (int i = 0; i < S.size(); i++) {
			if (S[i] == mainas[0]) {
				Mozi[i] = 1;
			}
			if (S[i] == purasu[0]) {
				Mozi[i] = 0;
			}


		}


		for (int i = 0; i < S.size()-K+1; i++) {
			if (1 == Mozi[i] % 2) {
				for(int j=0;j<K;j++){
					Mozi[i + j]++;
				}
				result++;
			}

			if (1 == Mozi[S.size()-1-i] % 2) {
				for (int j = 0; j<K; j++) {
					Mozi[S.size() - 1 - i - j]++;
				}

				result++;
			}

			for (int j = 0; j<S.size(); j++) {
				if(1==Mozi[j]%2){
					break;
				}
				else if (j == S.size() - 1) {
					MyEnd[0] = true;
				}

			}
			if (MyEnd[0] == true) {
				break;
			}


		}

		if (MyEnd[0]==true) {
			printf("Case #%d: %d\n", aa + 1, result);
			fprintf(file, "Case #%d: %d\n", aa + 1, result);
		}
		if (MyEnd[0] == false) {
			printf("Case #%d: IMPOSSIBLE\n", aa + 1);
			fprintf(file, "Case #%d: IMPOSSIBLE\n", aa + 1);
		}
	
	}

	fclose(fp);
	fclose(file);

	return 0;
}


