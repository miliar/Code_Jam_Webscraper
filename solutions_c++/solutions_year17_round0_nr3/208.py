#include <iostream>
#include <string>
#include <fstream>
using namespace std;


int main(){

	int T;
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");
	fin >> T;

	for(int t = 0; t < T ; t++){
		
		long N, K;
		fin >> N >> K;

		long klegend = 0, M = N;

		while(true){

			if( 2*klegend+1 >= K ) break;

			M = M/2;
			klegend = 2*klegend+1;
		}

		long x = N - klegend - (M-1)*(klegend+1);

		if(x < K-klegend) M = M-1; 

		fout << "Case #" << t+1 << ": " << M/2 <<" "<< (M-1)/2 <<endl;
	}

	fin.close();
	fout.close();

	return 0;
}
