#include <iostream>
#include <stdlib.h>
#include <string>
#include <fstream>

using namespace std;

/* Returns true if and only if x is "tidy" as described in the comment above int "getLastTidyNumber(int n)" */
bool isTidy(int x) {
	/* s is the string representation of the int x */
	string s = to_string(x);
	int i;
	/* Check that each character of the string is less than or equal the next one. */
	for (i = 0; i < s.length() - 1; i++) {
		if (s[i] > s[i + 1]) return false;
	}
	return true;
}

/* getLastTidyNumber(int n) calculates and returns the lsat integer in the set {1, 2, ..., n} that has the tidy structure. A number has the tidy structure if each digit (in base
 * 10) is nondecreasing from left to right, e.g., 55, 125, 599, etc. 
 */
int getLastTidyNumber(int n) {
	/* i is the index used in the for loops */
	int i;
	for (i = n; i >= 1; i--) {
		/* Return the first tidy number counting down from n */
		if(isTidy(i)) return i;
	}
	return 1;
}

int main() {
	/* Open the input file for reading */
	ifstream inputFile;
	inputFile.open("B-small-attempt1.in", ios::in);

	/* n is the number of test cases in the input */
	int n;
	inputFile >> n;
	/* i is the index for the for loops, number is the number that Tatiana counted up to, and result will be the last number she counted that maintains the tidy property */
	int i, number, result;
	
	/* Getting the test cases from the input */
	ofstream myfile;
  	myfile.open("output.txt", std::fstream::out);

	for (i = 0; i < n; i++) {
		inputFile >> number;
		result = getLastTidyNumber(number);
		myfile << "Case #" << (i + 1) << ": " << result << endl;
	}


	myfile.close();
	
}
