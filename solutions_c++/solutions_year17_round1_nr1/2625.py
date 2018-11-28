#include <cstdio>
#include <iostream>
using namespace std;
int r,c,te;
char l[26][26],q;
bool b[26][26],li[50];


int main()
{
	cin>>te;
	for (int t=1;t<=te;t++)
	{
	cout<<"Case #"<<t<<":"<<endl;
	scanf("%d %d",&r,&c);
	for (int i=0;i<r;i++)
	{
		for (int j=0;j<c;j++)
		{
			cin>>l[i][j];
			li[((int)l[i][j])-65]=false;
		}
	}
	for (int i=0;i<r;i++)
	{
		for (int j=0;j<c;j++)
		{
			if (l[i][j]!='?' && li[((int)l[i][j])-65]==false)
			{
			//cout<<l[i][j]<<endl;
			q=l[i][j];
			li[((int)l[i][j])-65]=true;
			j=-1;
			continue;
			}
			else if (l[i][j]=='?')
			l[i][j]=q;
		}
	q='?';
	}

	for (int i=1;i<r;i++)
	{
		for (int j=0;j<c;j++)
		{
			if (l[i][j]=='?')
			l[i][j]=l[i-1][j];
		}
	q='?';
	}
	for (int i=r-2;i>=0;i--)
	{
		for (int j=c-1;j>=0;j--)
		{
			if (l[i][j]=='?')
			l[i][j]=l[i+1][j];
		}
	q='?';
	}




	for(int i=0;i<r;i++)
	{
	for (int j=0;j<c;j++)
	cout<<l[i][j];
	cout<<endl;
	}
	}
	return 0;
}

