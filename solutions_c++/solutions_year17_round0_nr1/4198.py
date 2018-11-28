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
	
		
		// Input
		string S;
		int K;
		
		size_t nPP=0,oPP=0;
		getline(ifh,line);		
		nPP = line.find(' ',oPP);stringstream(line.substr(oPP,nPP-oPP)) >> S;oPP=nPP+1;
		nPP = line.find(' ',oPP);stringstream(line.substr(oPP,nPP-oPP)) >> K;oPP=nPP+1;

		 // ans=0;

		int c[1000];
		char v[1000];

		int tc[1000];
		char tv[1000];

		FF(i,1000) c[i]=0;
		FF(i,1000) tc[i]=0;
		// FF(i,1000) v[i]=0;
		
		int stackCount=0;
		int currentCount=0;

		// FF(i,S.length()){
		// 	currentCount++;
		//   	if(S[i]!=S[i+1] || (i==S.length()-1)){
		//     	c[stackCount]=currentCount;
		//     	v[stackCount]=S[i];
		//     	if(v[stackCount]=='-')
		//     		c[stackCount]*=-1;
		//     	currentCount=0;
		//     	stackCount++;
		//   	}
		// }
		  
		// FF(i,stackCount)
		// 	cout << c[i] << ":" << v[i] << ",";
		// cout << ans << endl;

		LL ans=0;
		bool imp=false;
			cout << S << endl;
		// while(!imp){
			LL tempAns=ans;
			int count=0;
			
			
			// if(count==S.length())
			// 	break;
			
			FF(i,S.length()-K+1){
				if(S[i]=='-'){
					ans++;
					for(int j=i;j<i+K;j++){
						if(S[j]=='-') S[j]='+';
							else S[j]='-';
					}
				}
			}

			FF(i,S.length()){
				if(S[i]=='+') count++;
			}

			cout << S << endl;

			// if(tempAns==ans && count!=S.length())
			if(count!=S.length())
				imp=true;

			cout << ans << endl;
		// }


		// Output
		if(imp){
			cout << "Case #"<< t+1 << ": " << "IMPOSSIBLE" << endl;
			ofh << "Case #"<< t+1 << ": " << "IMPOSSIBLE" << endl;
		}
		else{
			cout << "Case #"<< t+1 << ": " << ans << endl;
			ofh << "Case #"<< t+1 << ": " << ans << endl;
		}
	}
return 0;
}



		