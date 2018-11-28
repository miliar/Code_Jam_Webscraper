/*This code is a copyright of princess23*/
/*Write the name of the program*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
freopen("f1.txt","r",stdin);
freopen("f2.txt","w",stdout);
char str[10000];
int t,n,i,j,k,cnt,l,p;
cin>>t;
for(k=1;k<=t;k++)
{
	cin>>str>>p;
	cnt=0;
	l=99999999;
	for(i=0;i<strlen(str);i++)
	{
		if(str[i]=='-')
		{
			j=i;
			l=0;
			while(l<p&&j<strlen(str))
			{
				if(str[j]=='-')
				str[j]='+';
				else
				str[j]='-';
				j++;
				l++;
			}
			if(l<p)
			break;
		cnt++;
		}
	}
if(l<p)
cout<<"Case #"<<k<<": "<<"IMPOSSIBLE"<<endl;
else
cout<<"Case #"<<k<<": "<<cnt<<endl; 
}
return 0;
}

