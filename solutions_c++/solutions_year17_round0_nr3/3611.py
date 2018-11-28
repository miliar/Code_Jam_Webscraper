#include<iostream>
using namespace std;

int main()
{
	int cases;
	cin>>cases;
	for(int z=1; z<=cases; z++)
	{
		long long N,K;
		cin>>N>>K;
		long long L=N/2,R=(N-1)/2,lc=1,rc=1;
		long long k=2;
		while(k<=K)
		{
			k*=2;
			long long nL=L/2,nR=(R-1)/2;
			long long nlc=lc,nrc=rc;
			if((L-1)/2==nL) nlc+=lc;
			else nrc+=lc;
			if(R/2==nL) nlc+=rc;
			else nrc+=rc;
			L=nL,R=nR,lc=nlc,rc=nrc;
			// cout<<L<< " "<<R<<" "<<
		}
		long long kek=K-k/2+1;
		long long l1=R,r1=R;
		if(kek<=lc)
		{
			l1=L;
			if(kek+k/2<=lc) r1=L;
		}
		// cout<<L<<" "<<R<<" "<<lc<<" "<<rc<<" "<<k/2-1<<" "<<kek<<endl;
		// cout<<kek+k/2<<endl;
		cout<<"Case #"<<z<<": "<<l1<<" "<<r1<<endl;
	}
}