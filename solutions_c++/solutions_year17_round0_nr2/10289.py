#include <fstream>
#include <iostream>
#include <string>

using namespace std;
int main() {
	ifstream inFile("B-small-attempt5.in");
	ofstream outFile("out.txt");
	string line;
	getline(inFile, line);
	int t = stoi(line);
	for (int a1 = 1; a1 <= t; a1++) {
		getline(inFile, line);
		string pro_str = line;
		int position = 1;
		char past = pro_str[0];
		while (position != pro_str.length()) {
			if (past > pro_str[position]) {
				int temp = position - 2;
				if (temp < 0) temp = 0;
				if (temp != position - 1) {
					while (past == pro_str[temp]) {
						temp--;
						position = temp + 1;
						if (temp < 0) break;
					}
				}
				break;
			}
			else past = pro_str[position++];
		}
		if (position != 0) position--;
		if (pro_str.length() != 1 && position+1 !=pro_str.length()) {
			pro_str[position] = pro_str[position] - 1;
			for (int i = position+1; i < pro_str.length(); i++) {
				pro_str[i] = '9';
			}
		}
		long long int result = stoi(pro_str);
		outFile << "Case #" << a1 << ": " << result << endl;
	}
	outFile.close();
	inFile.close();
}