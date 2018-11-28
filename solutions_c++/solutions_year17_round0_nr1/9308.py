#include <bits/stdc++.h>
using namespace std;
int main()
{
int T,o;
cin>>T;o=T;
while(T--)
{ string s;int x; cin>>s; cin>>x;
	int ans=0;
	for(int i=0;i<=s.length()-x;i++)
	    {
	    if(s[i]!= '+')
	    {
	    for(int j=i;j<i+x;j++)
	    {
	    if(s[j]== '+')
	     s[j]= '-';
	     else
	     s[j]='+';
	    }
	    ans++;    
	    }
	    }
	    int temp=0;
for(int i=0;i<s.length();i++)
	 if(s[i]== '-')
	 {cout<<"Case #"<< o-T<<": "<<"IMPOSSIBLE"<<endl;
	 temp=1;
	 break;
	 }
	 if(temp==0)
	 cout<<"Case #"<< o-T<<": "<<ans<<endl;
	}
}
