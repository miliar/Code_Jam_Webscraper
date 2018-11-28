/*
 * B.cc
 *
 *  Created on: Apr 8, 2017
 *      Author: ra162554
 */

#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#define MAX 1002
#define SZ(x) (int) (x).size()

using namespace std;

int main(){
	int test_cases;
	scanf("%d",&test_cases);
	for (int test_number = 0; test_number < test_cases; ++test_number) {
		unsigned long long N;
		vector<int> digits;
		scanf("%lld",&N);
		while (N>0){
			digits.insert( digits.begin() , N%10LL );
			N/=10LL;
		}
		for (int i = SZ(digits)-1;i>=1 ; i--){
			if (digits[i]< digits[i-1]){
				digits[i-1]--;
				for (int j = i; j < SZ(digits) ; ++j) {
					digits[j] = 9;
				}
			}
		}
		printf("Case #%d: ",test_number+1);
		int indice = 0;
		while (digits[indice] == 0){
			indice++;
		}
		for (; indice< SZ(digits); ++indice) {
			printf("%d",digits[indice]);
		}
		printf("\n");
	}
	return 0;
}



