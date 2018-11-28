#include <bits/stdc++.h>
using namespace std;
int T,N,L; string S; char A[1005];
int main()
{
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	cin>>T;
	for(int cases=1; cases<=T; cases++)
	{
		cin>>S;
		cin>>N;
		L=S.size();
		//To make it mutable.
		for(int i=0; i<L; i++)
		{
			A[i]=S[i];
		}
		//
		int cnt=0;
		for(int i=0; i<=(L-N); i++)
		{
			if(A[i]=='+')continue;
			else
			{
				cnt++;
				for(int j=i; j<(i+N); j++)
				{
					if(A[j]=='+')
					A[j]='-';
					else A[j]='+';
				}
			}
		}
		//Lets check whether all are happy else IMPOSSIBLE.
		int flag=1;
		for(int i=0; i<L; i++)
		{
			if(A[i]=='+')continue;
			flag=0;
			break;
		}
		if(flag==0)
		{
			cout<<"Case #"<<cases<<": IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"Case #"<<cases<<": "<<cnt<<endl;
		}
	}
	return 0;
}
