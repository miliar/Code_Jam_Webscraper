#include <vector>
#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main() {
	ifstream in("B-large.in");
	ofstream out("out.txt");

	int T;
	string temp;
	getline(in, temp);
	T = stoi(temp);

	string s;
	int current = 1;
	while (T) {
		getline(in, s);

		string largest = "";
		for (int i = 0; i < s.size(); i++) {
			char current = s[i];

			bool all_pass = true;
			for (int j = i + 1; j < s.size(); j++) {
				if (s[j] > current) break;
				if (s[j] < current) {
					all_pass = false;
					break;
				}
			}


			if (all_pass) {
				largest += current;
			}
			else {
				largest += (current - 1);
				for (int j = i + 1; j < s.size(); j++) {
					largest += '9';
				}
				break;
			}
		}

		if (largest[0] == '0') largest.erase(largest.begin());


		out << "Case #" << current << ": " << largest << endl;


		T--;
		current++;
	}
}