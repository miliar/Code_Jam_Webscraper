#include <iostream>
#include <math.h>
#include <string>
#include <cstdlib>
#include <stdio.h>
using namespace std;


bool is_tidy(long long &N);
int count_digits(long long N);
long long to_int(string N_string, int no_of_digits);
long long power(int x,int y);

int main() {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out1","w",stdout);
	long long N;
	int no_of_cases;
	cin >> no_of_cases;
	for (int i=0; i<no_of_cases; i++) {
		cin >> N;
		for (long long j=N; j>=0; j--) {
			if (is_tidy(j)){
				cout << "Case #" << i+1 << ": " << j << "\n";
				break;
			}
		}
	}
	return 0;
}

bool is_tidy(long long &N) {

	std::string N_string = std::to_string(N);
	int no_of_digits = count_digits(N);
	int tempA,tempB;
	for(int i=0; i<no_of_digits-1; i++){
		tempA = N_string[i] - '0';
		tempB = N_string[i+1] - '0';
		if (tempA <= tempB){
			continue;
		}else{
			N_string[i] = (tempA - 1) + '0';
			for (int j=i; j<no_of_digits-1; j++){
				N_string[j+1] = 9 + '0';
			}
			N = to_int(N_string,no_of_digits)+1;
			return false;
		}
	}
	return true;
}

int count_digits(long long N) {

	int x=0; //number of digits
	while (N != 0) {
		x++;
		N /= 10;
	}
	return x;
}

long long to_int(string N_string, int no_of_digits) {
	long long x;
	long long N=0;
	int powr = no_of_digits-1;
	string temp;
	for (int i=0; i<no_of_digits; i++) {
		temp = N_string[i];
		x = atoi(temp.c_str());
		x = atoi(temp.c_str()) * power(10,powr);
		N += atoi(temp.c_str()) * power(10,powr);
		powr--;
	}
	return N;
}

long long power(int x,int y){
	long long n = x;
	if (y == 0)
		return 1;
	for (int i = 0; i<y-1; i++){
		n *= x;
	}
	return n;
}