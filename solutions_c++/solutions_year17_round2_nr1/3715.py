#include <fstream>
//~ #include <iostream>
using namespace std;
ifstream fin ("A-large.in");
ofstream fout ("output.txt");
int T, N;
double D;
double maxT;
double k, s, tt;


int main(){
	fin>>T;
	fout.precision(12);
	
	for (int t=1; t<=T; t++){
		maxT=-1;
		fin>>D>>N;
		for (int i=0; i<N; i++){
			fin>>k>>s;
			tt=(D-k)/s;
			if (maxT<tt || maxT==-1) maxT=tt;
			}
		//~ cout<<D<<" "<<maxT<<"\n";
		fout<<"Case #"<<t<<": "<<D/maxT<<"\n";
		}
	return 0;
	}
