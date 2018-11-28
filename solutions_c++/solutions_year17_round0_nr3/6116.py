#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main()
{
	ll t;
	cin>>t;
	for(ll it=1;it<=t;it++)
	{
		vector <int> v;
		queue <int> q;
		ll n,k,count=1;
		cin>>n>>k;
		ll height=(int)log2(n)+1;
		height=pow(2,height)-1;
		v.push_back(n);
		q.push(n);
		while(!q.empty())
		{
			int x=q.front();
			q.pop();
			if(x%2==0)
			{
				int num=x/2;
				if(v.size()==height)
					break;
				v.push_back(num);
				if(v.size()==height)
					break;
				v.push_back(num-1);
				q.push(num);
				q.push(num-1);
			}
			else
			{
				int num=x-1;
				num/=2;
				if(v.size()==height)
					break;
				v.push_back(num);
				if(v.size()==height)
					break;
				v.push_back(num);
				q.push(num);
				q.push(num);
			}
		}
		sort(v.rbegin(),v.rend());
		ll ans=v[k-1];
		int a1,a2;

		if(ans%2==0)
		{
			int num=ans/2;
			a1=num;
			a2=num-1;
		}
		else
		{
			int num=ans-1;
			num/=2;
			a1=num;
			a2=num;
		}


		cout<<"Case #"<<it<<": "<<max(a1,a2)<<" "<<min(a1,a2)<<"\n";
//		for(int i=0;i<v.size();i++)
//			cout<<v[i]<<" ";
//		cout<<endl;
	}
	return 0;
}