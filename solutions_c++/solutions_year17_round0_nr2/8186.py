// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "stdio.h"
#include <vector>
#include <string>
using namespace std;
void transformtoTidyNOS(vector<string>* vec, int number) {
	int i = 0;
	while (i < number) {
		string s(vec->at(i));
		int len = s.size();
		int j = len - 2;
		while (j >= 0) {
			while (j>=0 && s[j] <= s[j + 1]) {
				j--;
			}
			if (j < 0) break;
			s[j] = s[j] -1;
			for (int k = j + 1; k < len; k++) {
				s[k] = '9';
			}
		}
		vec->at(i) = to_string(stoull(s));
		i++;
	}
}
int main()
{
	int number = 0;
	vector<string> vec;
	cin >> number;
	for (int i = 0; i < number; i++) {
		string num;
		cin >> num;
		vec.push_back(num);
	}
	transformtoTidyNOS(&vec, number);
	for (int i = 0; i < number; i++) {
		cout << "Case #" << i+1 << ": " << vec.at(i) << endl;
	}
	int stop;
	cin >> stop;
    return 0;
}


