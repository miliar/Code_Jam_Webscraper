//
//  main.cpp
//  GoogleCodeJam2017
//
//  Created by nastia on 08/04/2017.
//  Copyright © 2017 Anastasiia Soboleva. All rights reserved.
//

#include <iostream>
#include <vector>
#include <cmath>

//Tidy numbers
using namespace std;

vector<int> toArrayFromNumber(unsigned long long n) {
	int res[19];
	int i = 0;
	while (n > 0) {
		int lastDigit = (int)(n - (n / 10) * 10);
		res[i] = lastDigit;
		i++;
		n /=10;
	}
	res[i] = 'a';
	i = 0;
	while (res[i] != 'a') {
		i++;
	}
	
	vector<int> array(i);
	for (int j = 0; j < i; j++) {
		array[i - 1 - j] = res[j];
	}
	return array;
}

unsigned long long toNumberFromArray(vector<int> array) {
	unsigned long long sum = 0;
	unsigned long size = array.size();
	for (int i = 0; i < size; i++) {
		sum += array[i] * (unsigned long long)(std::pow(10, size - 1 - i));
	}
	return sum;
}

vector<int> tidy(unsigned long long n) {
	
	vector<int> array = toArrayFromNumber(n);
	
	bool shoulDo = true;
	int m = (int)array.size();
	
	while (m > 1) {
		if (shoulDo) {
			
			for (int i = 1; i < m; i++) {
				if (array[i] >= array[i-1]) {
					shoulDo = false;
					continue;
				} else {
					array[i-1] -= 1;
					for (int j = i; j < m; j++) {
						array[j] = 9;
					}
					m = i;
					shoulDo = true;
					break;
				}
			}
			
		} else {
			return array;
		}
	}
	return array;
}

unsigned long long tidyNumber(unsigned long long n) {
	vector<int> result = tidy(n);
	unsigned long long tidy = toNumberFromArray(result);
	return tidy;
}

void tidyNumbers() {
	
	int t;
	cin >> t;
	
	unsigned long long n;

	for (int t_i = 1; t_i <= t; t_i++) {
		
		cin >> n;
		cout << "Case #" << t_i << ": " << tidyNumber(n) << endl;
		
	}
	
}

int main(int argc, const char * argv[]) {
	tidyNumbers();
	return 0;
}
