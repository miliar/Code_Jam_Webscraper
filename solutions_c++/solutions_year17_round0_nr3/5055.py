#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <string>

#include <strstream>

using namespace std;


const int NMax=1000001;
//const int NMax=10;
//int L[NMax],R[NMax];

void stall(long long int N, long long int K, long long int &y, long long int &z)
{
	if(K==0) {y=z=0;}
	else if(K==1) {
		if(N%2==1) {y=z=(N-1)/2;}
		else{ y=(z=N/2)-1;}
	}
	else {
	long long int N1, N2, K1, K2,y1,y2,z1,z2;

	K--;
	N--;
	K2 = K-long long int(K/2);
	K1 = K-K2;
	N2 = N-long long int(N/2);
	N1 = N-N2;

	if(K1<K2)
		stall(N2,K2,y,z);
	else
		stall(N1,K1,y,z);

	//if(y1>y2) { y = y1; z = z1;}
	//else if(y1==y2) { y = y1; z = max(z1,z2);}
	//else {y = y2; z = z2;}
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for(int NumCase=1; NumCase <=T; NumCase++) {
		cout << "Case #" << NumCase << ": ";


		long long int N, K,y,z,i;
		
		cin >> N >> K;
		stall(N,K,y,z);
#if 0

		for( i=0;i<N;i++) {L[i]=i;R[i]=N-i-1;}
		
		for(int k=0;k<K;k++) {
			for( i=1,y=min(L[0],R[0]),z=max(L[0],R[0]);i<N;i++)
			{
				if(y<min(L[i],R[i])) {
					y=min(L[i],R[i]) ;z=max(L[i],R[i]);
				}
				else if (y==min(L[i],R[i]) && z < max(L[i],R[i])) 
					z=max(L[i],R[i]);
			}

			for( i=0;i<N;i++)
				if(y==min(L[i],R[i])&&z==max(L[i],R[i])) {
					L[i]=R[i]=-1;
					for(int j=i-1;j>=0 && R[j]!=-1;j--)R[j]=i-j-1;
					for(int j=i+1;j<=N && L[j]!=-1;j++)L[j]=j-i-1;
					i=N;
				}
		}
#endif
		cout << z << " " << y;
		cout << endl;
	}
 	return 0;
}
