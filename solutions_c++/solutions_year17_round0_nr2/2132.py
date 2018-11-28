#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("outputL.txt");

	int T;
	fin >> T;

	for (int cas = 1; cas <= T; cas++){
		string n;
		fin >> n;

		fout << "Case #" << cas << ": ";
		if (n.length() == 1){
			fout << n << endl;
			continue;
		}

		while (1){
			int i;
			for (i = 1; i < n.length(); i++){
				if (n[i - 1] > n[i]){
					n[i - 1]--;
					for (int k = i; k < n.length(); k++){
						n[k] = '9';
					}
					break;
				}
			}

			if (i == n.length())
				break;
		}

		bool check = true;
		for (int i = 0; i < n.length(); i++){
			if (check){
				if (n[i] != '0'){
					fout << n[i];
					check = false;
				}
			}
			else
				fout << n[i];
		}
		fout << endl;
	}
}