#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
vector<long long> v;
long long ceili(long double a)
{
	if(a-(long long)a>0)
		return (long long)a+1;
	else
		return (long long)a;
}
long long flr(long double a)
{
	return (long long)a;
}
int main()
{
	ios_base::sync_with_stdio(false);
	long long x,T,N,K,bits,val,i;
	cin>>T;
	for(x=1;x<=T;x++)
	{
		v.clear();
		cin>>N>>K;
		bits=ceili(log2(K+1))-1;
		val=K-(long long)pow(2,flr(log2(K)));
		while(bits--)
		{
			v.push_back(val%2);
			val/=2;
		}
		for(i=0;i<v.size();i++)
		{
			N=v[i]==0?ceili((N-1)*1.0/2):flr((N-1)*1.0/2);
		}
		cout<<"Case #"<<x<<": "<<ceili((N-1)*1.0/2)<<" "<<flr((N-1)*1.0/2)<<"\n";
	}
	return 0;
}
