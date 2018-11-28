
#include<bits/stdc++.h>
using namespace std;
main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("outlarge.txt","w",stdout);
	int tt;
	cin>>tt;
	for(int p=1;p<=tt;p++)
	{
	string s;
	int k;
	cin>>s>>k;
	int len=s.length();
	int move=0;
	int flag=0;
	for(int i=0;i<len;i++)
	{
       if(s[i]=='-' and i+(k-1)>=len)
       {
       flag=1;
       break;
       }
       else if(s[i]=='-')
       {
       for(int j=i;j<=(i+k-1);j++)
       {
       if(s[j]=='-')
       s[j]='+';
       else
       s[j]='-';
       }
       move++;
       }
       else
       continue;
       if(flag)
       break;

	}
	if(!flag)
    cout<<"Case #"<<p<<": "<<move<<'\n';
    else
    cout<<"Case #"<<p<<": "<<"IMPOSSIBLE"<<'\n';
	}
	//cout<<"papa";
}