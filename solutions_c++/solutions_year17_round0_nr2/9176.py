#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("2Small.in");
ofstream fout("2Small.out");

int num[20] = {0};

bool check (long long n) {
	if (n < 10) {
		return true;
	}
	int digits = 0;
	int i = 1;
	while (n > 0) {
		num[i] = n % 10;
		n /= 10;
		i++;
	}
	digits = i - 1;
	for (int i = 1; i < digits; i++) {
		if (num[i] < num[i + 1]) {
			return false;
		}
	}
	return true;
}

int main () {
	int t;
	fin >> t;
	for (int o = 1; o <= t; o++) {
		long long n;
		fin >> n;
		while (1) {
			if(check(n)) {
				fout << "Case #" << o << ": " << n << endl;
				break;
			}
			n--;
		}
	}
	return 0;
} 
