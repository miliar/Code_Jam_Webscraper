#pragma once

#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;


int Test,MySize;
long long int rmax,rmin;
long long int isu, hito;
int num[21];
typedef pair<long long int, long long int> p;
vector<p> sit;
char c[21] = {};
string S;

FILE *file;
FILE *fp;


int main() {



	fp = fopen("C-small-1-attempt7 (1).IN", "r");
	file = fopen("answer4_1.txt", "w");

	fscanf(fp, "%d", &Test);

	//cin >> Test;

	
	p buf[2];
	long long int a;

	for (int aa = 0; aa < Test;aa++) {

		

		S = "";

		fscanf(fp, "%lld%lld", &isu,&hito);
		
		if (1 == isu % 2){
			a = (isu - 1) / 2;
			if (1 == a%2) {
				buf[0].first = (a - 1) / 2;
				buf[0].second = (a - 1) / 2;
				buf[1].first = (a - 1) / 2;
				buf[1].second = (a - 1) / 2;
			}
			else {
				buf[0].first = (a  / 2)-1;
				buf[0].second = a/2;
				buf[1].first = (a / 2) - 1;
				buf[1].second = a / 2;
			}
			rmax = a;
			rmin = a;
		}
		else {

			a = (isu/ 2)-1;
			if (1 == a % 2) {
				buf[0].first = (a - 1) / 2;
				buf[0].second = (a - 1) / 2;
			}
			else {
				buf[0].first = (a / 2) - 1;
				buf[0].second = a / 2;
			}
			rmin = a;
			a = (isu / 2);
			if (1 == a % 2) {
				buf[1].first = (a - 1) / 2;
				buf[1].second = (a - 1) / 2;
			}
			else {
				buf[1].first = (a / 2) - 1;
				buf[1].second = a / 2;
			}
			rmax = a;

		}


		sit.push_back(buf[0]);
		sit.push_back(buf[1]);

		sort(sit.begin(), sit.end());
		reverse(sit.begin(), sit.end());

		for (int i = 0; i < hito-1; i++){


			sort(sit.begin(), sit.end());
			reverse(sit.begin(), sit.end());

			

			if (1 == sit[0].first % 2) {
					buf[0].first = (sit[0].first - 1) / 2;
					buf[0].second = (sit[0].first - 1) / 2;
			}
			else {
					buf[0].first = (sit[0].first / 2) - 1;
					buf[0].second = sit[0].first / 2;

			}


			if (1 == sit[0].second % 2) {
					buf[1].first = (sit[0].second - 1) / 2;
					buf[1].second = (sit[0].second - 1) / 2;
			}
			else {
				buf[1].first = (sit[0].second / 2)-1;
				buf[1].second = sit[0].second / 2;

			}
			rmin = sit[0].first;
			rmax = sit[0].second;

			sit.push_back(buf[0]);
			sit.push_back(buf[1]);
			reverse(sit.begin(), sit.end());
			sit.pop_back();

		}

		
		//cin >> S >> K;
		
	

			printf("Case #%d: %lld %lld\n", aa + 1, rmax ,rmin);
			fprintf(file, "Case #%d: %lld %lld\n", aa + 1, rmax, rmin);
		
			sit.clear();
	
	}

	fclose(fp);

	fclose(file);

	return 0;
}


