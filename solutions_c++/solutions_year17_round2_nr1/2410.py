#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <utility>
#include <map>
#include <iomanip>
using namespace std;
vector<long double> K,S;
int main()
{
	ios_base::sync_with_stdio(false);
	long long T,N,x,i;
	long double maxi,D;
	cin>>T;
	for(x=1;x<=T;x++)
	{
		K.clear();
		S.clear();
		cin>>D>>N;
		K.resize(N);
		S.resize(N);
		maxi=0;
		for(i=0;i<N;i++)
		{
			cin>>K[i]>>S[i];
			if((D-K[i])/S[i]>maxi)
			{
				maxi=(D-K[i])/S[i];
			}
		}
		cout<<fixed<<setprecision(10)<<"Case #"<<x<<": "<<D/maxi<<"\n";
	}	
	return 0;
}
