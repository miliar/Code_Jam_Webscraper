#include<bits/stdc++.h>
#define li long long int
using namespace std;
 
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	li t,i;
	cin>>t;
	for(li k=1;k<=t;k++)
	{
		string s;
		cin>>s;
		li l=s.length();
		for( i=l-1;i>0;i--)
		{
			if(s[i]<s[i-1])
			{
				for(li j=i;j<l;j++)
					s[j]='9';
				s[i-1]=s[i-1]-1;	
			}
			
			
		}
		s.erase(0, min(s.find_first_not_of('0'), s.size()-1));
		cout<<"Case #"<<k<<": "<<s<<endl;
	}
	return 0;
}
