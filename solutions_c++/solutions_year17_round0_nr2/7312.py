//~ #include <iostream>
#include <fstream>
#include <string>
using namespace std;
ifstream fin ("B-large.in");
ofstream fout ("output.txt");

int T;
string S;
bool stop;

void riempi (int p) {
	for (int i=p; i<(int)S.size(); i++)	S[i]=9+48;
	return;
	}
	
void confronta (int a) {
	if (S[a]>S[a+1]){
		S[a]--;
		riempi(a+1);
		stop=1;
		}
	return;
	}
	
int main(){
	fin>>T;

	for (int i=1; i<=T; i++){
		fin>>S;
		stop=0;
		if (S.size()>1){
			for (int x=0; x<(int)S.size(); x++)
				for (int j=0; j<(int)S.size()-1-x; j++){
					stop=0;
					confronta(j);
					if (stop) break;
					}
			}
		fout<<"Case #"<<i<<": ";
		if (S[0]!=48) fout<<S[0];
		for (int j=1; j<(int)S.size(); j++) fout<<S[j];
		fout<<"\n";	
		}
	return 0;
	}
