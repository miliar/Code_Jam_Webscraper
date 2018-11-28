#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("input1.txt","r",stdin);
	freopen("output1.txt","w",stdout);
	int n;
	cin>>n;
	for(int k=1;k<=n;k++)
	{
		string s;
		int i,j;
		cin>>s;
		int l=s.length();
		if(l==1)
		{
			cout<<"Case #"<<k<<": "<<s<<endl;
		}
		else
		{
			for(i=l-2;i>=0;i--)
			{
				
				if(s[i]>s[i+1])
				{
					s[i]=s[i]-1;
					for(j=i+1;j<l;j++)
						s[j]='9';

					
				}
				
			}
			s.erase(0, s.find_first_not_of('0'));
			cout<<"Case #"<<k<<": "<<s<<endl;
			
		}
		
	}
return 0;
}
