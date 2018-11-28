#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void flip(string& S, const int& a, const int& K){
	for (int i = a; i < a + K; i++)
		if (S[i] == '+') S[i] = '-';
		else S[i] = '+';
}

int recurse(string& S, int a, const int& K){
	//if (a > S.size() - K) return -1000;
	while (a <= S.size() - K){
		if (S[a] == '+') a++;
		else {
			flip(S, a, K);
			return 1 + recurse(S, a + 1, K);
		}
	}
	for (int i = a; i < S.size(); i++) if (S[i] == '-') return -1000;
	return 0;
}

void main(){
	int T;
	ifstream infile;
	infile.open("A-large.in");
	if (!infile.is_open()) cout << "Failed to load file!" << endl;

	ofstream outfile;
	outfile.open("outputL.txt");
	infile >> T;
	int i = T;
	while (i){
		string S;
		int K;
		infile >> S;
		infile >> K;
		int count = recurse(S, 0, K);
		if (count < 0) outfile << "Case #" << T - i + 1 << ": IMPOSSIBLE\n";
		else outfile << "Case #" << T - i + 1 << ": " << count << endl;
		i--;
	}
	infile.close();
	outfile.close();
	system("pause");
}