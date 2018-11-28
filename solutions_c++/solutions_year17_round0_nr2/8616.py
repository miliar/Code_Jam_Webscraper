#include <string>
#include<cmath>
#include<cstdlib>
#include <fstream>
#include <iostream>

using namespace std;

string test(string str) {
	int step;
	std::string::size_type sz = 0;
	for (int i=1; i<str.length(); i++) {
		if (str[i-1] > str[i]) {
			unsigned long long num = stoull(str, &sz, 0)-1;
			return test(to_string(num));
			}		
	}

	return str;

}

int main(){

	ifstream input;
	input.open("B-small-attempt2.in");
	ofstream output;
	output.open("output_file.txt");
	string number;
	unsigned long long int num;
	input >> num;
	for (int i = 0; i < num; i++) {
		input >> number;
		output << "Case #" << i + 1 << ": " << test(number)<< endl;
	}
	
	
	return 0;
}