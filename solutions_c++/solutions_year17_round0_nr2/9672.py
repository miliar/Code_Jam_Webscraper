#include <bits/stdc++.h>
using namespace std;

int main() {
	string s;
	int t;

	ifstream fin("input.in");
    ofstream fout("output.out");

    fin>>t;
	for(int q = 0 ;q<t; q++) {
		fin>>s;
		int len = s.size();
		int l = len;
		int eqF = 0;
		int prevCorr = 0;
		while(len-->0) {
			if(int(s[len])<int(s[len-1])) {
				s[len] = 57;
				s[len-1]--;
				if(eqF || prevCorr){
					for(int k = len+1; k<l; k++) {
						s[k] = 57;
					}
					eqF = 0;
				}
			}
			else if (int(s[len])==int(s[len-1])) {
				eqF = 1;
			}
			else if (int(s[len])>int(s[len-1])) {
				prevCorr = 1;
			}
		}
		fout<<"Case #"<<(q+1)<<": ";
		if(int(s[0]) != 48) {
			fout<<int(s[0])-48;
		}
		for(int i = 1; i<l; i++) {
			fout<<int(s[i])-48;
		}
		fout<<"\n";
	}
	fin.close();
	fout.close();
	return 0;
}