//~ #include <iostream>
#include <fstream>
#include <string>
using namespace std;
ifstream fin ("A-large.in");
ofstream fout ("output.txt");

int T, K;
string S;
int quanti;

void cambia (int p) {
	for (int i=p; i<p+K; i++){
		if (S[i]=='-') S[i]='+';
		else if (S[i]=='+') S[i]='-';
		}
	return;
	}
	
bool possibile () {
	bool a = 1;
	for (int i=(int)S.size()-K; i<(int)S.size(); i++){
		a= a && (S[i]=='+');
		if (!a) return false;
		}
	return true;
	}
	
int main(){
	fin>>T;
	for (int i=1; i<=T; i++){
		fin>>S>>K;
		quanti=0;
		for (int j=0; j<(int)S.size()-K+1; j++){
			if (S[j]=='-') {
				cambia(j);
				quanti++;
				//~ for (int j=0; j<(int)S.size(); j++) fout<<S[j];
				}
			//~ fout<<"\n";
			}
		fout<<"Case #"<<i<<": ";
		if (possibile()) fout<<quanti;
		else fout<<"IMPOSSIBLE";
		//~ fout<<" ";
		//~ for (int j=0; j<(int)S.size(); j++) fout<<S[j];
		fout<<"\n";
		}
	return 0;
	}
