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
	
		// LL N;getline(ifh,line);stringstream(line) >> N;
		LL L=0,R=0;		
		LL N,K;

		size_t nPP=0,oPP=0;
		getline(ifh,line);		
		nPP = line.find(' ',oPP);stringstream(line.substr(oPP,nPP-oPP)) >> N;oPP=nPP+1;
		nPP = line.find(' ',oPP);stringstream(line.substr(oPP,nPP-oPP)) >> K;oPP=nPP+1;
		
		int depth = log(K)/log(2);

		LL oc[depth+1];
		LL ov[depth+1];
		LL ec[depth+1];
		LL ev[depth+1];

		for(int i=0;i<=depth;i++){
			oc[i]=0;
			ov[i]=0;
			ec[i]=0;
			ev[i]=0;
		}

		if(N%2==0){
			ec[0]=1;
			ev[0]=N;
		} else{
			oc[0]=1;
			ov[0]=N;
		}

		for(int i=1;i<=depth;i++){
			cout << "Before:d,ev[d],ec[d],ov[d],oc[d]:" << i << "," << ev[i] << "," << ec[i] << "," << ov[i] << "," << oc[i] << endl;
			if(ec[i-1]>0){
				if(((ev[i-1]-1)/2)%2==0 ){
					ec[i]+=ec[i-1];
					ev[i]=((ev[i-1]-1)/2);
				} else{
					oc[i]+=ec[i-1];
					ov[i]=((ev[i-1]-1)/2);
				}

				if(((ev[i-1])/2)%2==0 ){
					ec[i]+=ec[i-1];
					ev[i]=((ev[i-1])/2);
				} else{
					oc[i]+=ec[i-1];
					ov[i]=((ev[i-1])/2);
				}
			}

			cout << "Mid:d,ev[d],ec[d],ov[d],oc[d]:" << i << "," << ev[i] << "," << ec[i] << "," << ov[i] << "," << oc[i] << endl;

			if(oc[i-1] > 0){
				if(((ov[i-1]-1)/2)%2==0 ){
					ec[i]+=oc[i-1];
					ev[i]=((ov[i-1]-1)/2);
				} else{
					oc[i]+=oc[i-1];
					ov[i]=((ov[i-1]-1)/2);
				}

				if(((ov[i-1])/2)%2==0 ){
					ec[i]+=oc[i-1];
					ev[i]=((ov[i-1])/2);
				} else{
					oc[i]+=oc[i-1];
					ov[i]=((ov[i-1])/2);
				}
			}
			cout << "After:d,ev[d],ec[d],ov[d],oc[d]:" << i << "," << ev[i] << "," << ec[i] << "," << ov[i] << "," << oc[i] << endl;
		}

		LL count = K - (LL)pow(2,depth) + 1;

		LL node=0;

		LL maxCount = 0;

		if(ev[depth] > ov[depth]){
			if(count <= ec[depth])
				node = ev[depth];
			else
				node = ov[depth];
		}
		else{
			if(count <= oc[depth])
				node = ov[depth];
			else
				node = ev[depth];
		}



		// if(ec[depth]<=count){
		// 	node = max(ev[depth],ov[depth]);
		// } else
		// 	node =  min(ev[depth],ov[depth]);

		cout << "Count,node,ec[depth],depth:" << count << "," << node << "," << ec[depth] << "," << depth << endl;

		L = (node-1)/2;
		R = (node)/2;


		// cout << "Depth:" << depth << endl;

		// int delta = 0;
		// if((LL) pow(2,depth) == K && N%2==0){
		// 	// cout << "Last node:" << K << endl;
		// 	delta=1;
		// }
		// cout << "N,K,Depth,Delta:" << N << "," << K << "," << depth << "," << delta << ",";
		// L = (((LL)((N-1)/pow(2,depth))+delta)-1)/2;
		// R = (((LL)((N-1)/pow(2,depth))+delta))/2;

		// cout << (LL) pow(2,depth) << endl;

		// Output
		cout << "Case #"<< t+1 << ": " << R << " " << L << endl;
		// ofh << "Case #"<< t+1 << ": " << N << endl;
		ofh << "Case #"<< t+1 << ": " << R << " " << L << endl;
		
	}
return 0;
}



		