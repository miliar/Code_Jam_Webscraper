#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
	ifstream fin("A-large.in");
	ofstream fout("output.out");
	int t;
	fin >> t;
	for(int x = 1; x <= t; x++){
		fout << "Case #" << x << ": ";
		string cake;
		int k, flip = 0;
		fin >> cake >> k;
		int yo = cake.find('-'), l = cake.length();
		bool broken = 0;
		while(yo != -1) {
			if(l - yo < k) {
				broken = 1;
				break;
			} else {
				string cak = cake.substr(0, yo) + '+';
				for(int i = yo + 1; i < yo + k; i++) cak += (cake.at(i) == '-')? '+': '-';
				cak += cake.substr(yo + k);
				cake = cak;
				flip++;
			}
			yo = cake.find('-');
		}
		if(broken) fout << "IMPOSSIBLE\n";
		else fout << flip << endl;
	}
	fin.close();
	fout.close();
	return 0;
}