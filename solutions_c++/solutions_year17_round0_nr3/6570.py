#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int n,k;
	for(int i=0;i<t;i++)
	{
		cin>>n>>k;
		int a[n]={0};
		
		for(int j=0;j<k;j++)
		{
			int ls[n]={0},rs[n]={0};
			int max1=-1;
			int index=-1;
			vector<int> v;
			for(int p=0;p<n;p++)
			{
				if(a[p]==0)
				{
					int mum=p-1;
					for(;a[mum]!=1 && mum>=0;mum--)
					{
						ls[p]++;
					}//cout<<ls[p]<<" ";
					int mum1=p+1;
					for(;a[mum1]!=1 && mum1<=n-1;mum1++)
					{
						rs[p]++;
					}//cout<<rs[p]<<" ";
					if(max1<min(ls[p],rs[p]))
					{
						max1=min(ls[p],rs[p]);
						index=p;
						//cout<<index<<endl;
						v.clear();
						v.push_back(p);
					}
					else if(max1==min(ls[p],rs[p])) v.push_back(p);
				}
				//cout<<ls[p]<<" "<<rs[p]<<endl;
			}
			if(v.size()>1)
			{
				int i2=-1;
				int maxer=-1;
				for(int p=0;p<v.size();p++)
				{
					int lm=v[p];//cout<<lm<<endl;
					if(maxer<max(ls[lm],rs[lm]))
					{
						maxer=max(ls[lm],rs[lm]);
						i2=lm;
					}
				}
				a[i2]=1;
				index=i2;
				//cout<<index<<endl;
			}
			else
			{
				a[index]=1;
			}
		
		if(j==k-1) cout<<"Case #"<<i+1<<": "<<std::max(ls[index],rs[index])<<" "<<std::min(ls[index],rs[index])<<endl;
	}
	}
}