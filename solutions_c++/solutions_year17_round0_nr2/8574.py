#include <iostream>
#include <fstream>
#include <string>
using namespace std;


string getLastTidyNumber(string &input) {
	char last = '0';
	for (auto digit = input.begin(); digit != input.end(); ++digit) {
		if (*digit < last) {
			--digit; //step back
			--(*digit); //subtract one
			fill(next(digit, 1), input.end(), '9'); //fill remainder with 9
			--digit; //step back one more and check again to be safe
		}
		last = *digit;
	}
	input.erase(0, min(input.find_first_not_of('0'), input.size()-1));
	return input;
}

int main()
{
	ifstream infile("thisInput.txt");
	ofstream outfile("thisOutput.txt");

	int numCases;
	infile >> numCases;

	for (int i = 1; i <= numCases; ++i) {
		string N;
		infile >> N;
		outfile << "Case #" << i << ": " << getLastTidyNumber(N) << endl;		
	}
}

