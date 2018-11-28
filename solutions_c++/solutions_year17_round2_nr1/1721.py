#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<algorithm>
using namespace std;

struct cmp
{
	bool operator() (int A, int B)
	{
		return A < B;
	}
};

int main()
{
	long long int T,D,N;
	cin>>T;
	for(long long int i=1;i<=T;i++)
	{
		cin>>D>>N;
		vector<double> S(N);
		vector<double> K(N);
		double Tmax = 0;
		for(long long int j=0;j<N;j++)
		{
			cin>>K[j]>>S[j];
			K[j] = D - K[j];
			if(K[j]/S[j] > Tmax) Tmax = K[j]/S[j];
		}
		double ans = D/Tmax;
		
		cout<<"Case #"<< i << ": "<<fixed<< ans << "\n";
	}
}
