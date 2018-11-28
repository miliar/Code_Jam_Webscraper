#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
#include "math.h"
using namespace std;


void swapPanc(string& p, int i){
	if (p[i]=='-'){
		p[i]='+';
	} else {
		p[i]='-';
	}
}

void problemaA(int t){
	int res = 0;
	bool canDo = true;
	string pancakes;
	int flipper;
	cin >> pancakes;
	cin >> flipper;

	for (int i = 0; i < pancakes.size()-flipper+1; ++i){
		if(pancakes[i] == '-'){
			res++;
			for (int j = i; j < min((int )pancakes.size(),i+flipper); ++j){
				swapPanc(pancakes,j);
			}
		}
	}
	for (int i = pancakes.size()-flipper; i < pancakes.size(); ++i){
		if (pancakes[i] == '-'){
			canDo = false;
			break;
		}
	}

	cout << "Case #" << t << ": ";
	if (canDo){
		cout << res << endl;
	} else {
		cout << "IMPOSSIBLE" << endl;
	}

}

void volverIgual(vector<int>& n, int index){
	for (int i = index-1; i >= 0; ++i){
		if (i == 0){
			n[i]--;
			break;
		}
		if(n[i] == n[index] && i!=0){
			n[i] = 9;
		} else {
			n[i+1]--;
			break;
		}
		
	}
}
void problemaB(int t){
	long long int input;
	cin >> input;
	int quantityDigits = floor(log10(input))+1;
	vector<int> number(quantityDigits,0);
	vector<int> result(quantityDigits,0);
	long long int res = 0;

	for (int i = 0; i < quantityDigits; ++i){

		number[quantityDigits-1-i] = input%10;
		input = input/10;
	}


	int i;
	for (i = 0; i < quantityDigits; ++i){
		if (i == quantityDigits-1){
			result[i] = number[i];
			break;
		}
		if (number[i] <= number[i+1]){
			result[i] = number[i];
		} else {
			if(i!=0 && number[i] == number[i-1]){
				result[i] = number[i];
				volverIgual(result,i);
				result[i] = 9;
			} else {
				result[i] = number[i]-1;
			}
			
			break;
		}
	}

	for (i = i+1; i < quantityDigits; ++i){
		result[i] = 9;
	}

	for (i = 0; i < quantityDigits; ++i){
		long long int d = pow(10,quantityDigits-i-1);
		res += result[i]*d;
	}

	cout << "Case #" << t << ": ";
	cout << res << endl;
}

int solvEq(int a, int b, int n, int l){
	return n-l*a;
}

void problemaC(int t){
	long long int k,n;
	cin >> n;
	cin >> k;
	long long int res = n+2;
	int sobra = 0;
	long long int hasta = floor(log2(k))+1;
	for (int i = 0; i < hasta; ++i){
		if (i == hasta-1){
			int p = pow(2,floor(log2(k)));
			int cantMayor = solvEq(res-1,res,n+2+p-1,p);
			if (k-p>=cantMayor){
				sobra = (res)%2;
				res = (res)/2;
			} else {
				sobra = (res+1)%2;
				res = (res+1)/2;
			}
			//sobra = (res+1)%2;
			//res = (res+1)/2;
		} else {
			res = (res+1)/2+(res+1)%2;
		}
	}

	
	//int resMin = floor((float)(res-2)/2);
	long long int resMin = res-2;
	long long int resMax = resMin+sobra;

	cout << "Case #" << t << ": ";
	cout << resMax << " " << resMin << endl;
	
}

int main(){
	int cantTest;
	cin >> cantTest;
	for (int i = 0; i < cantTest; ++i){
		problemaC(i+1);
	}
	

	return 0;
}
