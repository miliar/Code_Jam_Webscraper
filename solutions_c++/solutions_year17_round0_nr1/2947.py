#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void swap(string& s, long pos) {
	s[pos] = s[pos] == '+' ? '-' : '+';
}

void swapK(string& s, long k, long start) {
	for (long i = 0; i < k; i++) {
		swap(s,start+i);
	}
}

bool lastKPlus(const string& s, long k) {
	long length = s.length();
	for (int i =0; i< k; i++) {
		if (s[length-i-1] == '-') {
			return false;
		}
	}
	return true;
}

long getTurns(string& s, long k) {
	long len = s.length();
	long acc = 0;
	for (long i = 0; len >= i + k; i++) {
		if (s[i] == '-') {
			acc++;
			swapK(s,k,i);
		}
	}
	return lastKPlus(s,k) ? acc : -1;
}

int main(int argc, char **argv) {
	int t;
	ifstream input;
	ofstream output;
	
	input.open("A-large.in");
	output.open("out.txt");
	input >> t;
	for (int i = 1;i<=t;i++) {
		long k;
		string s;
		input >> s;
		input >> k;
		
		long turns = getTurns(s,k);
		output << "Case #" << i << ": ";
		if (turns < 0) output << "IMPOSSIBLE";
		else output << turns;
		output << endl;
	
	}
    input.close();
	output.close();
	return 0;
}
