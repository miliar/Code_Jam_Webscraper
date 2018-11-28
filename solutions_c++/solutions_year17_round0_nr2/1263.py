#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

int main(){
	ifstream fin("B-large.in");
	ofstream fout("tout.out");
	
	int T,tt = 1;
	fin >> T;
	while(T--){
		string s;
		int len, i;
		int bef[20],idx = -1;
		fin >> s;
		//cout << s <<endl;
		len = s.length();
		for(i = 0;i < 20; ++i) bef[i] = -1;
		for(i = 1;i < len; ++i){
			bef[i] = s[i] - s[i-1];
			//cout << bef[i]<<" ";
			if(bef[i] < 0 && idx == -1) idx = i;
		}
		fout << "Case #" << tt++ <<": ";
		if(idx == -1) fout << s <<endl;
		else{
			for(i = idx-1; i > 0; --i){
				if(bef[i] != 0) break; 
			}
			idx = i;
			
			if(idx == 0 ){
				if(s[idx] != '1') fout << char(s[idx]-1);
				for(i = idx+1; i < len; ++i) fout <<"9";
			}
			else{
				for(i = 0;i < idx; ++i) fout << s[i];
				fout << char(s[idx]-1);
				for(i = idx+1;i < len;++i) fout << "9";
			}
			fout <<endl;
		}
		
	}
	return 0;
}