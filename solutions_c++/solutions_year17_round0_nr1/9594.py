#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main() {
	fstream result;
	result.open("result.txt", ios::out);

	string s , check = "";
	int T , k , count = 0;

	cin >> T;

	for (int i = 0; i < T; i++) {

		cin >> s >> k;

		s = s + "+++";
		check = "";
		count = 0;
		for (int i = 0; i < s.size(); i++) {
			check += '+';
		}

		for (int i = 0; i < s.size() - k; i++) {
			if (s.at(i) == '-') {
				for (int j = 0; j < k; j++) {
					if (s.at(i + j) == '-'){
						s.at(i + j) = '+';
					}
					else {
						s.at(i + j) = '-';
					}
				}
				count++;
			}
		}




		if (s == check) {
			result << "Case #" << i+1 << ": " << count << endl;
		}
		else {
			result << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
		}
	}

	result.close();
	system("pause");
	return 0;
}