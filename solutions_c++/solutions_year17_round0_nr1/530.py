#include <iostream>
#include <fstream>
using namespace std;

int helper(string str, int k, char c) {
	int count = 0;
	for(int i=0; i<str.length(); i++) {
		if(str[i] == c) continue;
		for(int j=0; j<k; j++) {
			if(i+j >= str.length()) return -1;
			if(str[i+j] == '+') {
				str[i+j] = '-';
			}
			else{
				str[i+j] = '+';
			}
		}
		count++;
	}
	return count;
}

int main() {
	ifstream file("A-large.in");
	ofstream out("output2.txt");
	int n, k;
	string str;
	file >> n;
	for(int i=0; i<n; i++) {
		file >> str >> k;
		int c1, c2;
		/*
		c1 = helper(str, k, '+');
		c2 = helper(str, k, '-');
		if(c1 == -1) {
			if(c2 == -1) {
				out << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
			}
			else {
				out << "Case #" << i+1 << ": " << c2 << endl;				
			}
		}
		else {
			if(c2<c1 && c2!=-1) {
				out << "Case #" << i+1 << ": " << c2 << endl;	
			}
			else {
				out << "Case #" << i+1 << ": " << c1 << endl;				
			}
		}
		out << c1 << " " << c2 << endl;
		*/
		c1 = helper(str, k, '+');
		if(c1 == -1) {
			out << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
		}	
		else {
			out << "Case #" << i+1 << ": " << c1 << endl;
		}
	}
}