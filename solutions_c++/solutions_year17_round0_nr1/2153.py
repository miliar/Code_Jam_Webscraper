#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("outputL.txt");

	string str;
	int T, k, cnt;
	fin >> T;

	cnt = 0;
	for (int cas = 1; cas <= T; cas++){
		cnt = 0;
		fin >> str >> k;
		for (int i = 0; i <= str.length() - k; i++){
			if (str[i] == '-'){
				cnt++;
				for (int j = i; j < i + k; j++){
					if (str[j] == '-')
						str[j] = '+';
					else
						str[j] = '-';
				}
			}
		}

		int check;
		for (check = 0; check < str.length(); check++){
			if (str[check] == '-')
				break;
		}

		fout << "Case #" << cas << ": ";
		if (check == str.length()){
			fout << cnt << endl;
		}
		else{
			fout << "IMPOSSIBLE" << endl;
		}
	}
}