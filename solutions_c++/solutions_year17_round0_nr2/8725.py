#include<iostream>
#include<vector>
using namespace std;
int main()
{
	int t,x=0;
	cin>>t;
	while(t--)
	{
		long long n,nc;
		cin>>n;
		nc=n;
		vector<int>v;
		while(nc!=0)
		{
			v.push_back((nc%10));
			nc=nc/10;
		}
		int d=v.size()-1,flag=0,flag2=0;
		if(d==0)
		{
			flag=2;
		}
		/*for(int i=0;i<=d;i++)
		{
			cout<<v[i];
		}*/
		//cout<<"\n";
		for(int j=d;j>0;j--)
		{
			if(v[j-1]<v[j])
			{
				//cout<<v[j]<<"\n";
				flag2=1;
				for(int p=j;p<d;p++)
				{
					if(v[p]>v[p+1])
					{
						flag=1;
						//cout<<flag<<"\n";
						v[p]-=1;
						for(int i=0;i<p;i++)
						{
							v[i]=9;
						}
						break;
					}
				}
			}
			if(flag==1)
			{
				break;
			}
		}
			x++;
		if(flag==1)
		{
			cout<<"Case #"<<x<<": ";
			for(int i=d;i>=0;i--)
			{
				cout<<v[i];
			}
			cout<<"\n";
		}
		else if(flag==0&&flag2==1)
		{
			cout<<"Case #"<<x<<": ";
			for(int i=d;i>=0;i--)
			{
				if(i==d)
				{
					v[i]-=1;
					if(v[i]>0)
					cout<<v[i];
				}
				else
				cout<<"9";
			}
			cout<<"\n";
		}
		else
		{
			cout<<"Case #"<<x<<": ";
			for(int i=d;i>=0;i--)
			{
				cout<<v[i];
			}
			cout<<"\n";
		}
	
	}
	return 0;
}
