#include <bits/stdc++.h>
using namespace std;

int main()
{

freopen("hu.in","r",stdin);
 freopen("out.txt","w",stdout);
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
	long long n,k;
	cin>>n>>k;
	multiset<long long> arr;
	multiset<long long>:: iterator it;
	arr.insert(n);
	while(k!=1)
	{

		it=arr.end()--;
		it--;
		long long x=*it;
		arr.erase(it);
		x--;
		long long y=x/2;
		long long z=x-y;
		arr.insert(z);
		arr.insert(y);
	//	cout<<z<<" "<<y<<endl;
		k--;
	}

	it=arr.end()--;
	it--;
	long long x=*it;

	x--;
	//for(it=arr.begin();it!=arr.end();it++)
	//cout<<"x="<<*it<<endl;
	cout<<"Case #"<<i<<": "<<max(0LL,x-x/2)<<" "<<max(0LL,x/2)<<endl;
	//cout<<x-x/2<<" "<<x/2<<endl;
}

}
