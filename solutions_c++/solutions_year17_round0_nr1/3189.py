#include <vector>
#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main() {
	ifstream in("A-large.in");
	ofstream out("out.txt");

	int T;
	string temp;
	getline(in, temp);
	T = stoi(temp);

	string s;
	int current = 1;
	while (T) {
		getline(in, s);
		auto space = s.find(" ");
		auto pancake = s.substr(0, space);
		int K = stoi(s.substr(space + 1));

		int cnt = 0;
		for (int i = 0; i <= pancake.size() - K; i++) {
			if (pancake[i] == '-') {
				for (int j = i; j < i + K; j++) {
					if (pancake[j] == '+') pancake[j] = '-';
					else pancake[j] = '+';
				}

				cnt++;
			}
		}

		bool impossible = false;
		for (int i = 0; i < pancake.size(); i++) {
			if (pancake[i] == '-') {
				impossible = true;
				break;
			}
		}

		if (!impossible) {
			out << "Case #" << current << ": " << cnt << endl;
		}
		else {
			out << "Case #" << current << ": IMPOSSIBLE" << endl;
		}

		T--;
		current++;
	}
}