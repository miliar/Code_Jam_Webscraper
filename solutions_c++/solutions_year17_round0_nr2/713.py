#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int T;
int num[20], res[20];
string N;

int main() {
	ifstream fin ("B.in");
	ofstream fout ("B.out");

	fin >> T;
	for (int t = 1; t <= T; t++) {
		fin >> N;
		int size = N.size();
		for (int i = 0; i < size; i++) 
			num[i] = N[i] -'0';
		res[0] = num[0];
		int temp = 0;
		for (int i = 1; i < size; i++) {
			if (num[i] < num[i-1]) {
				if (num[i-1] == 1) {
					size--;
					for (int j = 0; j < size; j++)
						res[j] = 9;
				} 
				else {
					res[temp] = num[temp] - 1;
					for (int j = temp+1; j < size; j++)
						res[j] = 9;
				}
				break;
			}
			if (num[i] != num[i-1])
				temp = i;
			res[i] = num[i];
		}
		fout << "Case #" << t << ": ";
		for (int i = 0; i < size; i++)
			fout << res[i];
		fout << endl;
	}

	fout.close();

	return 0;
}