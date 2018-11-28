//i am vengence i am the night i am Batman
//ios_base::sync_with_stdio(false);cin.tie(NULL);
#include<bits/stdc++.h>
using namespace std;

int main()
{
	long long int i,j,k,l,m,n,r,t;
	
	cin>>t;
	
	for(i=1;i<=t;i++)
	{
		string s;
		cin>>s;
		cin>>k;
		
		r=0;m=0;
		for(j=s.length()-1;j>=0;j--)
		{
			if(s[j]=='-')
			{
				if(j>=k-1)
				{
					for(l=j;l>j-k;l--)
					{
						if(s[l]=='-')
						s[l]='+';
						else
						s[l]='-';
					}
					r++;
					//cout<<s;
				}
				else
				{
					m=1;
					cout<<"Case #"<<i<<": "<<"IMPOSSIBLE\n";
					break;
				}
			}
		}
		
		if(m==0)
		{
			cout<<"Case #"<<i<<": "<<r<<"\n";
		}
		
	}
	
	
    return 0;
}
