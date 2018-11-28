#include<iostream>
#include<vector>
using namespace std;

vector<long long> lol[18];
vector<long long> K;

int main()
{
	for(int i=1; i<=9; i++) {lol[0].push_back(i);K.push_back(i);}
	for(int i=1; i<18; i++)
	{
		for(int j=0; j<lol[i-1].size(); j++)
		{
			int d=lol[i-1][j]%10;
			for(int k=d; k<=9; k++)
				{lol[i].push_back(lol[i-1][j]*10+k);K.push_back(lol[i-1][j]*10+k);}
		}
	}
	// cout<<K.size()<<endl;
	long long cases;
	cin>>cases;
	for(int z=1; z<=cases; z++)
	{
		long long N;
		cin>>N;
		long long L=0, R=K.size();
		while(R-L>5)
		{
			long long M=(L+R)/2;
			if(K[M]>N) R=M;
			else L=M;
		}
		long long idx=L;
		for(int i=L; i<=R; i++)
		{
			if(K[i]<=N) idx=i;
			else break;
		}
		cout<<"Case #"<<z<<": "<<K[idx]<<endl;
	}
}