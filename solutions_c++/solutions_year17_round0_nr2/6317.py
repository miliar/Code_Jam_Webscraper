#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int t;
ll n,i,x,temp,c=0;
int main()
{

	cin>>t;
	while(t--)
	{
		c+=1;
		int a[100];
		for(i=0;i<100;i++)
		{
			a[i]=-1;
		}
		x=0;
		cin>>n;
		temp=n;
		while(temp)
		{
			a[x]=temp%10;
			temp/=10;
			x++;		
		}
		int dig[x+2];
		int k=0;
		for(i=x-1;i>=0;i--)
		{
			dig[k]=a[i];
			//cout<<dig[k];
			k++;
			
		}
		int chk;
		int f=0;
		cout<<"Case #"<<c<<":"<<" ";
		for(i=0;i<k-1;i++)
		{
			if(dig[i]>dig[i+1])
			{
				f=1;
				chk=i;
				break;
			}
			
		}
		//cout<<chk;	
		int br=chk;
		if(f==0)
		cout<<n;
		else
		{
			for(i=chk;i>=1;i--)
			{
				
				{
					if(dig[i-1]!=dig[i])
					{
						br=i;
						break;
					}
					br=i-1;
					
				}
			}
			vector<int> ans;
			for(i=0;i<br;i++)
			ans.push_back(dig[i]);
			ans.push_back(dig[br]-1);
			for(i=br+1;i<k;i++)
			ans.push_back(9);
			int start=0;
			for(i=0;i<ans.size();i++)
			{
				if(ans[i]!=0)
				{
					start=i;
					break;
				}
			}
			for(i=start;i<ans.size();i++)
			{
				cout<<ans[i];
			}

		}
	
		cout<<endl;
	}

	return 0;
}
