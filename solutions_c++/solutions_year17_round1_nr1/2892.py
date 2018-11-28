#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<math.h>
#define ll unsigned long long int
using namespace std;



void _main()
{
	cout<<"\n";
	int r,c;
	cin>>r>>c;
	vector<char>::iterator it;
	vector<char> v;
	string a[r];
	
	for(int j=0;j<r;j++)
	{
		cin>>a[j];
	}
	//cout<<"hi";
	for(int k=0;k<r+c;k++){
	
	for(int i=0;i<r;i++)
	{for(int j=0;j<c;j++)
	{	if(a[i][j]=='?')
		{for(int l=0;l<=i;l++)
		{if(a[i-l][j]!='?')
		{a[i][j]=a[i-l][j];
		break;
		}
		}	
		}
		}
		
	}}for(int k=0;k<r+c;k++){
	for(int i=r-1;i>=0;i--)
	{for(int j=c-1;j>=0;j--)
	{	if(a[i][j]=='?')
		{for(int l=0;l<=(r-1-i);l++)
		{
	
		if(a[i+l][j]!='?')
		{a[i][j]=a[i+l][j];
		break;
		}
		}	
		}
		}
		
	}}
		
		
//hi
	for(int k=0;k<r+c;k++){
	
	for(int j=0;j<c;j++)
	{for(int i=0;i<r;i++)
	{	if(a[i][j]=='?')
		{for(int l=0;l<=j;l++)
		{if(a[i][j-l]!='?')
		{a[i][j]=a[i][j-l];
		break;
		}
		}	
		}
		}
		
	}}
	for(int k=0;k<r+c;k++){
	for(int j=c-1;j>=0;j--)
	{for(int i=r-1;i>=0;i--)
	{	if(a[i][j]=='?')
		{for(int l=0;l<=(c-1-i);l++)
		{
	
		if(a[i][j+l]!='?')
		{a[i][j]=a[i][j+l];
		break;
		}
		}	
		}
		}
		
	}}
		for(int k=0;k<r+c;k++){
	
	for(int i=0;i<r;i++)
	{for(int j=0;j<c;j++)
	{	if(a[i][j]=='?')
		{for(int l=0;l<=i;l++)
		{if(a[i-l][j]!='?')
		{a[i][j]=a[i-l][j];
		break;
		}
		}	
		}
		}
		
	}}for(int k=0;k<r+c;k++){
	for(int i=r-1;i>=0;i--)
	{for(int j=c-1;j>=0;j--)
	{	if(a[i][j]=='?')
		{for(int l=0;l<=(r-1-i);l++)
		{
	
		if(a[i+l][j]!='?')
		{a[i][j]=a[i+l][j];
		break;
		}
		}	
		}
		}
		
	}}
		
		
		

	for(int i=0;i<r;i++)
	{for(int j=0;j<c;j++)
	{
		cout<<a[i][j];
		}
cout<<endl;	}	
	
}

int main()
{
	freopen("a.in","r",stdin);
//	freopen("a.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{ 
	cout<<"Case #"<<i+1<<": ";_main();}
}
