/*
Problem B. Tidy Numbers

Problem

Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest to longest and her computers from oldest to newest. One day, when practicing her counting skills, she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?

Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with a single integer N, the last number counted by Tatiana.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last tidy number counted by Tatiana.

Limits

1 ¡Ü T ¡Ü 100.
Small dataset

1 ¡Ü N ¡Ü 1000.
Large dataset

1 ¡Ü N ¡Ü 1018.
Sample


Input 
 	
Output 
 
4
132
1000
7
111111111111111110

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

Note that the last sample case would not appear in the Small dataset.

*/


#include <iostream>
#include <vector>
#include <string>
#include <fstream>


using namespace std;


long long findLastTidyNum(long long num) {
	if (num < 10) return num;
	string str = to_string(num);
	// stack<char> st;
	int i = 1, n = str.size();
	for (; i < n; ++i) {
		if (str[i] < str[i - 1]) {
			break;
		}
	}
	if (i == n) return stoll(str);
	for (int j = i; j < n; ++j) {
		str[j] = '9';
	}
	--str[--i];
	while (i > 0 && str[i] < str[i - 1]) {
		str[i] = '9';
		--str[--i];
	}
	if (str[0] == '0') str.erase(0, 1);
	return stoll(str);
}


int main() {
	
	// ifstream in("B-small-attempt0.in");
	// ofstream out("B-small-attempt0.out");
	
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	
	int n;
	long long num;
	in >> n;
	
	for (int i = 1; i <= n; ++i) {
		in >> num;
		out << "Case #" << i << ": " << findLastTidyNum(num) << endl;
	}
	
	// cout << findLastTidyNum(132) << endl;
	// cout << findLastTidyNum(1000) << endl;
	// cout << findLastTidyNum(7) << endl;
	// cout << findLastTidyNum(111111111111111110) << endl;
}




