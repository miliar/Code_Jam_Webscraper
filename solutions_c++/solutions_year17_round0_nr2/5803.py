#include<bits/stdc++.h>
using namespace std;
long long t,tt,i,j;
string s;
int main()
{
	freopen("q17boo.txt","r",stdin);
	freopen("q17bout.txt","w",stdout);
	//cout<<"#1";
	cin>>t;
	//cout<<t;
	//t=4;
	while(t--)
	{
		//cout<<t<<" "<<tt<<endl;
		tt++;
		cin>>s;
		for(i=s.length()-2;i>=0;i--)
		{
			if(s[i]>s[i+1])
			{
				s[i]=char(int(s[i]-1));
				for(j=i+1;j<s.length();j++)
				{
					s[j]='9';
				}
			}
		}
		if(s[0]=='0')
		{
			s.erase(0,1);
		}
		printf("Case #%lld: ",tt);
		cout<<s<<endl;
	}
}
