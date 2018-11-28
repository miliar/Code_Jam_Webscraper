#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iomanip>
using namespace std;
struct S
{
	int pos;
	int speed;
	bool operator< (const S&s1)const
	{
		if(pos<s1.pos)
			return pos<s1.pos;
		return 0;
	}
};S A[1010];

double T[1010];
int main()
{
	int t;
	int D,N;
	double V;
	cin>>t;
	int i,j,k;

	for(i=1;i<=t;i++)
	{
		cin>>D>>N;
		for(k=0;k<N;k++)
		{
			cin>>A[k].pos>>A[k].speed;
		}
		sort(A,A+N);
		for(k=N-1;k>=0;k--)
		{
			if(k==N-1)
			{
				T[k]=(D-A[k].pos)*1.0/A[k].speed;
			}
			else
			{
				T[k]=max((D-A[k].pos)*1.0/A[k].speed,T[k+1]);
			}
		}
		V=D/T[0];
		cout<<"Case #"<<i<<": "<<fixed<<setprecision(6)<<V<<endl;
	}

}
