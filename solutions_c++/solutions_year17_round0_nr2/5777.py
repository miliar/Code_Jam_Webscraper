#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main() {

	ifstream input;
	ofstream output;
	input.open("B-large.in");
	output.open("output.txt");

	int t;
	input >> t;
	for (int i = 0;i < t;i++) {
		unsigned long long n;
		input >> n;
		string s = to_string(n);
		bool tidy = false;
		while (!tidy) {
			tidy = true;
			for (int j = 1;j < s.length();j++) {
				if (s[j - 1] > s[j]) {
					int a = s[j - 1] - '0';
					a--;
					s[j - 1] = a + '0';

					for (int k = j;k < s.length();k++) {
						s[k] = '9';
					}
					tidy = false;
					break;
				}
			}
		}
		while (s[0] == '0') {
			s=s.substr(1, s.length());
		}
		
		output << "Case #" << i + 1 << ": " << s << endl;
		
	}

	return 0;
}