#include <fstream>
#include <iostream>
#include <utility>
#include <algorithm>
#include <string>
#include <sstream>
using namespace std;

ifstream fin ("B.in"); ofstream fout ("B.out");

void onerun(int t) {
	string S; fin >> S;
	int p = 0; bool tidy = true;
	for (int i=0; i<(int)S.size()-1; i++) {
		int a = S[i]-'0', b = S[i+1]-'0';
		if (a < b) p = i+1;
		else if (a > b) {
			tidy = false; break;
		}
	}
	if (!tidy) {
		int a = S[p]; a--;
		S[p] = a;
		for (int i=p+1; i<(int)S.size(); i++) {
			S[i] = '9';
		}
		long long ans = stoll(S);
		fout << "Case #" << t << ": " << ans << endl;
	}
	else {
		fout << "Case #" << t << ": " << S << endl;
	}
}


int main() {
	int T; fin >> T;
	for (int t=1; t<=T; t++) {
		onerun(t);
	}
	fin.close(); fout.close();
}