#include <bits/stdc++.h> 
using namespace std;

void make(string &s)
{
int i,j;
int count=0;
for(i=0;i<s.length();i++)
{
	if(s[i]=='?')
		count++;

}
if(count==s.length())
	return;

int l=s.length();
for(i=0;i<l;i++)
{
	if(s[i]=='?')
	{
		for(j=i+1;j<l;j++)
		{
			if(s[j]!='?')
			{
					s[i]=s[j];
				break;
			}
		}
	}
}

for(i=l-1;i>=0;i--)
{
	if(s[i]=='?')
	{
		for(j=i-1;j>=0;j--)
		{
			if(s[j]!='?')
			{
					s[i]=s[j];
				break;
			}
		}
	}
}




}


int main()
{

int t;
cin>>t;
int var=1;
while(t--)
{

int r,c;
int j,i;
cin>>r>>c;
string s[50];
for(i=0;i<r;i++)
{
	cin>>s[i];
}

for(i=0;i<r;i++)
{
		make(s[i]);
}


for(i=0;i<r;i++)
{
	if(s[i][0]=='?')
	{
		for(j=i+1;j<r;j++)
		{
			if(s[j][0]!='?')
			{
				s[i]=s[j];
				break;
			}
		}
		
	}

}


for(i=r-1;i>=0;i--)
{
	if(s[i][0]=='?')
	{
		for(j=i-1;j>=0;j--)
		{
			if(s[j][0]!='?')
			{
				s[i]=s[j];
				break;
			}
		}
		
	}

}

cout<<"Case #"<<var<<":";
cout<<"\n";
for(i=0;i<r;i++)
	cout<<s[i]<<"\n";





var++;


}



}
