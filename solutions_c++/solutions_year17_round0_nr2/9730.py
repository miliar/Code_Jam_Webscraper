#include<bits/stdc++.h>
using namespace std;
#define llt long long int
#define endl "\n"
int main()
{
ios_base::sync_with_stdio(false);
cin.tie(0);
cout.tie(0);
freopen("/home/rahul/Desktop/inl.txt","r",stdin);
 freopen("/home/rahul/Desktop/outl.txt","w",stdout);
llt t;
cin>>t;
for(int k=1;k<=t;k++)
{
string str;
cin>>str;
llt l=str.length();
llt left=0,ind=0;
for(int i=0;i<l-1;i++)
{
	if(str[i]==str[i+1])
	{
	left=i+1;
	ind=i+1;
	}
	else if(str[i] < str[i+1])
	ind=i+1;
	else
	{
		if(left==ind and left!=0)
		{
		for(int j=i-1;j>=0;j--)
		{
			if(str[j]==str[j+1])
			i--;
			else
			break;
				
		}
			
			str[i]=char(int(str[i])-1);
			for(int j=i+1;j<l;j++)
			str[j]='9';
			break;
		}
		else
		{
			str[i]=char(int(str[i])-1);
			for(int j=i+1;j<l;j++)
			str[j]='9';
			break;
		}	
	
	}

}
cout<<"Case #"<<k<<": ";
if(str[0]=='0')
{
for(int i=1;i<l;i++)
cout<<str[i];
cout<<endl;
}
else
cout<<str<<endl;
}
return 0;
}
