#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main(){
	ofstream fout("A-large.out");
	ifstream fin("A-large.in");
	long long T, K, count, c = 1, moves = 0;
	string S;
	bool x = true;
	fin >> T;
	while (T--){
		fin >> S >> K;
		moves = 0;
		for (int i = 0; i < S.length(); i++){
			count = 0;
			if (S[i] == '-'){
				//count = 0;
				while (count < K && i <= S.length() - K){
					if (S[i + count] == '-'){
						S[i + count] = '+';
					}
					else if (S[i + count] = '+') {
						S[i + count] = '-';
					}
					count++;
				}
				moves++;
			}
			//cout << S << endl;
		}
		x = true;
		for (int i = 0; i < S.length(); i++){
			if (S[i] == '-'){
				x = false;
				break;
			}
		}
		if (x)
			fout << "Case #" << c << ": " << moves << endl;
		else
			fout << "Case #" << c << ": IMPOSSIBLE" << endl;
		c++;
	}
	//system("pause");
	return 0;
}