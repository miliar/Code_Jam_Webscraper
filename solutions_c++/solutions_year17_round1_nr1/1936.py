#include<iostream>
#include <string.h>
#include <vector>
char chars[30][30];
char filled[30][30];
using namespace std;
int main()
{
	int t;
	cin>>t;
	int r,c;
	for(int ti =1;ti<=t;ti++)
	{
		for(int i =0;i<30;i++)
			for(int j=0;j<30;j++)
				filled[i][j] = chars[i][j] = '?';
		cin>>r>>c;
		for(int i=0;i<r;i++)
		{
			string s;
			cin>>s;
			for( int j=0;j<c;j++)
				filled[i][j] = chars[i][j] = s[j];
		}

		for( int i=0;i<r;i++)
		{
			char currentChar;			
			int j =0;
			for(j=0;j<c;j++)
			{
				if(chars[i][j]!='?')
				{
					for(int k=0;k<j;k++)
						filled[i][k] = chars[i][j]; 
					currentChar = chars[i][j];
					break;
				}
			}					

			for( int k=j+1;k<c;k++)
			{
				if(chars[i][k] == '?')
					filled[i][k] = currentChar;
				else
					currentChar = chars[i][k];
			}
		}
		/*
		cout<<"Case #"<<ti<<": "<<endl;
		for(int i=0;i<r;i++)
		{
			for(int j =0;j<c;j++)
				cout<<filled[i][j];
			cout<<endl;
		}
		*/
		for(int i=0;i<c;i++)
		{
			char currentChar;			
			int j=0;
			for( j=0;j<r;j++)
			{
				if(filled[j][i]!='?')
				{
					for(int k=0;k<j;k++)
						filled[k][i] = filled[j][i]; 
					currentChar = filled[j][i];
					break;
				}
			}
			for( int k=j+1;k<r;k++)
			{
				//cout<<k<<i<<filled[k][i]<<endl;
				if(filled[k][i] == '?')
					filled[k][i] = currentChar;
				else
					currentChar = filled[k][i];
			}

		}
		cout<<"Case #"<<ti<<": "<<endl;
		for(int i=0;i<r;i++)
		{
			for(int j =0;j<c;j++)
				cout<<filled[i][j];
			cout<<endl;
		}
	}
	return 0;
}