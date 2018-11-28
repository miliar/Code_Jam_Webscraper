//https://code.google.com/codejam/contest/3264486/dashboard#s=p1
#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ofstream fout("q2.out");
	ifstream fin("q2.in");

	int cases = 0;
	bool found = false;
	fin >> cases;

	for (int i = 1; i <= cases; i++) {
		long long number = 0LL;
		fin >> number;
		fout << "Case #" << i <<": ";
		//Iterate through each digit of a number to see if it is in descending order
		while (!found && number >= 10){
			long long temp = number;
			while (temp >= 10) {
				int unit = temp % 10;
				temp = temp / 10;
				int tens = temp % 10;

				if (tens > unit) {
					number--;
					break;
				}
				else if (temp < 10) found = true;
			}
		}
		fout << number << endl;
		found = false;
	}

	fin.close();
	fout.close();
	
	return 0;
}
