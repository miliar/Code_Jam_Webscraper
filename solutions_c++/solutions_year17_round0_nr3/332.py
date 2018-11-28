#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(){
	cout<<"launching function main"<<endl;
	ifstream file("C-large.in");
	ofstream outputfile("myoutput.txt");
	int T, swp=0, swp1=1;
	long long int N, K, M, n[4], nop;
	file>>T;
	for(int t=0;t<T;t++){
		//read input
		file>>N>>K;
		//solve
		nop=0; n[2*swp]=1; n[2*swp+1]=0;
		while(nop+n[2*swp]+n[2*swp+1]<K){
			nop+=(n[2*swp]+n[2*swp+1]);
			if(N%2 == 0){
				n[2*swp1]=n[2*swp];
				n[2*swp1+1]=n[2*swp]+2*n[2*swp+1];
			}else{
				n[2*swp1]=2*n[2*swp]+n[2*swp+1];
				n[2*swp1+1]=n[2*swp+1];
			}
			N=(N-1)/2;
			swp=swp1; swp1=1-swp;
		}
		if((nop+n[2*swp+1]>=K) && (K>1))
			N++;
		//write output
		outputfile<<"Case #"<<(t+1)<<": "<<(N/2)<<" "<<((N-1)/2)<<endl;
	}
	file.close();
	outputfile.close();
}

