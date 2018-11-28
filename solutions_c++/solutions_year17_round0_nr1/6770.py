#include<iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

bool flip(string &s, int pos, int K){
	if(pos+K > s.size()) return false;
	for (int i = pos; i < pos + K; i++){
		if (s[i] == '+') s[i] = '-';
		else s[i] = '+';
	}
	return true;
}

int main(){
	int n; 
	ifstream fp("A-large.in");
	ofstream outfile;
	outfile.open("A-large.out"); 
	if (fp){
		fp >> n;
		for (int i = 0; i < n; i++){
			string s;
			int K, count = 0;
			bool OK = true;
			getline(fp,s);
			getline(fp,s,' ');
			//cout<<s<<' ';
			fp>>K;
			//cout<<K<<endl;
			outfile << "Case #" << i+1 << ": ";
			for (int i = 0; i < s.size(); i++){
				if (s[i] == '+') continue;
				else if(flip(s,i,K)) count++;
				else break;
			}
			for (int i = s.size() - K; i < s.size(); i++)
				if (s[i] == '-'){
					outfile << "IMPOSSIBLE" << endl;
					OK = false;
					break;
				}
			if (OK) outfile << count << endl;
		}
	}
	return 0;
}
