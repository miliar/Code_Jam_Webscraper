#include <iostream>
#include <fstream>
#include <string>

#define MAXN 1000

using namespace std;

int T, K;
string str;
bool A [MAXN];

int main() {
	ifstream fin ("A.in");
	ofstream fout ("A.out");

	fin >> T;
	for (int t = 1; t <= T; t++) {
		fin >> str >> K;
		for (int i = 0; i < str.size(); i++) 
			A[i] = (str[i]=='+' ? true : false);
		int count = 0;
		for (int i = 0; i <= str.size()-K; i++) {
			if (!A[i]) {
				for (int j = i; j < i+K; j++)
					A[j] = !A[j];
				count++;
			}
		}
		bool happy = true;
		for (int i = str.size()-K; i < str.size(); i++) 
			if (!A[i]) 
				happy = false;
		fout << "Case #" << t << ": ";
		if (happy)
			fout << count << endl;
		else
			fout << "IMPOSSIBLE" << endl;

	}

	fout.close();

	return 0;
}

