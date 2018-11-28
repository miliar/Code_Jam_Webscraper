#include<bits/stdc++.h>

using namespace::std;

long long int t,T;
char a[26][26];
int r,c,i,j,k,x,l,z;

int main()
{
cin>>T;
for(t=1;t<=T;++t)
{
	cout<<"Case #"<<t<<": "<<endl;
	cin>>r>>c;
	k=0;
	for(i=0;i<r;++i)
	{
	for(j=0;j<c;++j)
	cin>>a[i][j];
	j=0;
	while(j<c && a[i][j]=='?')j++;
	if(j==c){k++;}
	else
	{
		l=j;
		while(k>=0)
		{k--;
		x=l;
		for(j=0;j<c;++j)
		if(a[i][j]=='?')cout<<a[i][x];
		else {cout<<a[i][j];x=j;}
		cout<<endl;
		}
	k=0;
	}
	}
	z=k+1;
	while(k>0)
	{
		x=l;
		for(j=0;j<c;++j)
		if(a[i-z][j]=='?')cout<<a[i-z][x];
		else {cout<<a[i-z][j];x=j;}
		cout<<endl;
		k--;
	}
	
	
	
	
}
return 0;
}

