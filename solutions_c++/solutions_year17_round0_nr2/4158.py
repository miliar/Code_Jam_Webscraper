// Include Header and Libraries
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <iomanip>
#include <stdint.h>
#define FF(I,N) for(int I=0;I<N;I++)
#define FR(I,N) for(int I=N-1;I>=0;I--)
typedef long long LL;
using namespace std;
const LL INFN = -9223372036854775807; //const LL INFN = (int64_t)1<<63;
const LL INFP = 9223372036854775807; // const LL INFN = (int64_t)1<<62;

int main(int argc, char * argv[]){
		
	string infile = argv[1];
	string outfile = infile + ".out";
	
	ofstream ofh (outfile, ios::out); if (!ofh.is_open()) { cout << "Can't open the output file " << outfile << "\n";return 1;}
	string line;ifstream ifh (infile);if (!ifh.is_open()) { cout << "Can't open input file" << infile << "\n";return 1;}
	
	
	// Input: Number of Test Cases
	int T;getline(ifh,line);stringstream(line) >> T;
	
	
	FF(t,T){
	
		LL N;getline(ifh,line);stringstream(line) >> N;
		int len=0;
		
		LL temp=N;
		while(temp>0){
			len++;
			temp/=10;
		}


		int d[len];
		FF(i,len) d[i]=0;
		
		while(N>0){

			LL temp=N;
			for(int i=0;i<len;i++){
				d[len-i-1]=temp%10;
				temp/=10;
			}

			cout << "N:" << N << ",Len:" << len << " | ";
			for(int i=0;i<len;i++) cout << d[i];
			cout << " | ";

			bool flag=true;

			for(int i=len-1;i>0;i--){
				if(d[i]<d[i-1]){
					N = N - N%((LL) pow(10,len-i-1)) -1;
					// N%((LL) pow(10,len-i-1))
					cout << "Breaking, N:" << N << endl;
					flag=false;
					break;
				}
			}

			if(flag)
				break;
		}

		// Output
		cout << "Case #"<< t+1 << ": " << N << endl;
		ofh << "Case #"<< t+1 << ": " << N << endl;
		
	}
return 0;
}



		