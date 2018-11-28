#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,i,ch,l1,j,flag,k;
	cin>>t;
	string s1;
	for(i=1;i<=t;i++)
	{
		ch=0;
		flag=0;
		cin>>s1;
		l1=s1.length();
		if(l1==1)
		{
			cout<<"Case #"<<i<<": "<<s1[0]<<"\n";
			continue;
		}
		for(j=1;j<l1;j++)
		{
			if(s1[j]>s1[j-1])
			ch=j;
			else if(s1[j]<s1[j-1])
			{
				s1[ch]--;
				flag=1;
				break;
			}
		}
		cout<<"Case #"<<i<<": ";
		for(k=0;k<=ch;k++)
		if(s1[k]!='0')
		break;
		if(!flag)
		ch=l1-1;
		for(;k<=ch;k++)
		{
			cout<<s1[k];
		}
		for(;k<l1;k++)
		cout<<"9";
		cout<<"\n";
	}
	return 0;
}
