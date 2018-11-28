#include<iostream>
#include<string>
using namespace std;
int main()
{
int t;
cin>>t;
int m=1;
while(m<=t)
{
string s;
cin>>s;
long int l=s.length();
for(long int i=l-1;i>0;i--)
	{
	if(s[i]=='0')
		{
		for(long int j=i;j<=l;j++)
		{
		s[j]='9';
		}
		int b=int(s[i-1])-49-1;
		s[i-1]=(49+b);
		}
	
	
	
	else if(int((s[i])-49)<(int(s[i-1])-49))
		{
		for(long int j=i;j<=l;j++)
		{
		s[j]='9';
		}
		int a=int(s[i-1])-49-1;
		s[i-1]=(49+a);
		}
	}
long int k=0;
while(1)
{
if(s[k]=='0'){k++;}
else {break;}
}
cout<<"Case #"<<m<<": ";
for(long int i=k;i<l;i++)
{
cout<<s[i];
}
cout<<endl;
m++;
}	
return(0);
}
