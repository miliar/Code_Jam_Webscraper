#include <fstream>
//~ #include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;
ifstream fin ("A-large.in");
ofstream fout ("output.txt");

long long int T, N, K;
long long int R[1001];
long long int H[1001];
long long int ord [1001];
long long int soluz;
long long int solor;
double pi = 3.1415926535;

bool ordrag (int a, int b){
	if (R[a]>R[b]) return true;
	return false;
	}
bool ordalt (int a, int b){
	if (R[a]*H[a]>R[b]*H[b]) return true;
	return false;
	}
	
int main(){
	fin>>T;
	for (int t=1; t<=T; t++){
		fin>>N>>K;
		for (int i=0; i<N; i++) fin>>R[i]>>H[i];
		for (int i=0; i<N; i++) ord[i]=i;
		nth_element (ord, ord, ord+N, ordrag);
		soluz=0;
		for (int i=0; i<=N-K; i++){
			solor=0;
			solor+=R[ord[i]]*R[ord[i]];
			solor+=2*H[ord[i]]*R[ord[i]];
			sort(ord+i+1, ord+N, ordalt);
			for (int j=i+1; (j-i)<K; j++) solor += 2*H[ord[j]]*R[ord[j]];
			if (solor>soluz) soluz=solor;
			nth_element (ord+i+1, ord+i+1, ord+N, ordrag);
			}
		fout<<"Case #"<<t<<": "<<setprecision(10)<<(double)soluz*pi<<"\n";
		}
	//~ cout<<setprecision(10)<<pi;
	
	return 0;
	}
