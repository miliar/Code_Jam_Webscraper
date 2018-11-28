#include <bits/stdc++.h>
using namespace std;
int T; long long N; int A[25];
long long power(int x, int y)
{
	long long ret=1;
	for(int i=1; i<=y; i++)
	ret=ret*x;
	return ret;
}
int main()
{
	ifstream cin("B-large.in");
	ofstream cout("B-large.out");
	cin>>T;
	for(int cases=1; cases<=T; cases++)
	{
		cin>>N;
		int digits=0;
		/*Lets count the digits of N*/
		long long copy=N;
		while(copy>0)
		{
			copy/=10;
			digits++;
		}
		/*We have the digits in A[] from 1.....digits*/
		int cnt=digits;
		copy=N;
		while(copy>0)
		{
			A[cnt--]=copy%10;
			copy/=10;
		}
		//
		long long build=0;
		/*if(digits==1)
		{
			cout<<"Case #"<<cases<<": "<<N<<endl;
			continue;
		}*/
		int i;
		for(i=1; i<=digits; i++)
		{
			int to=digits-i;
			long long S=N%power(10,to);
			to--;
			long long tmp=0;
			for(int j=i+1; j<=digits; j++)
			{
				tmp=tmp+(power(10,to)*A[i]);
				to--;
			}
			if(tmp>S)
			{
				//change is required here
			
				if(A[i]!=1)
				{
					A[i]=A[i]-1;
					//cout<<A[i]<<endl;
				}
				else
				{
					A[i]=9;
					digits--;
				}
				break;
			}
			else
			{
				continue;
			}
		}
		for(int j=i+1; j<=digits; j++)
		{
			A[j]=9;
		}
		cout<<"Case #"<<cases<<": ";
		for(int i=1; i<=digits; i++)
		{
			cout<<A[i];
		}
		cout<<endl;
	}
	return 0;
}
