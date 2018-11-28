#include <fstream>
#include <iostream>
#include <utility>
#include <algorithm>
#include <string>
using namespace std;

ifstream fin ("inputA.txt"); ofstream fout ("outputA.txt");
vector<bool> pancakes;

void onerun(int t) {
	string S; int k; fin >> S >> k;
	cout << S.size() << endl;
	pancakes.clear();
	for (int i=0; i<(int)S.size(); i++) {
		pancakes.push_back(S[i]=='+');
	}
	int flips = 0;
	for (int i=0; i<=(int)pancakes.size()-k; i++) {
		if (!pancakes[i]) {
			flips++;
			for (int j=i; j<i+k; j++) pancakes[j] = !pancakes[j];
		}
	}
	for (int i=(int)pancakes.size()-k+1; i<(int)pancakes.size(); i++) {
		if (!pancakes[i]) {
			fout << "Case #" << t << ": IMPOSSIBLE" << endl;
			return;
		}
	}
	fout << "Case #" << t << ": " << flips << endl;
}

int main() {
	int T; fin >> T;
	for (int t=1; t<=T; t++) {
		onerun(t);
	}
	fin.close(); fout.close();
}