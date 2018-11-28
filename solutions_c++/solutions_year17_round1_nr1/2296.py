//============================================================================
// Name        : grid.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int r,c,j,k,m;


		cin>>r>>c;
		char a[r][c+1];
		string s;
		string b[r];

		for(j=0;j<r;j++)
		{
			//cin>>b[j];
			for(m=0;m<c;m++)
			{
				//a[j][m]=b[j][m];
				cin>>a[j][m];
			}

		}
				for(j=0;j<r;j++)
		{
			for(k=0;k<c;k++)
			{
				if(a[j][k]!='?')
				{
					int l=k-1;
					while(a[j][l]=='?' && l>=0)
					{
						a[j][l]=a[j][l+1];
						l--;
					}

					l=k+1;

					while(a[j][l]=='?'  && l<c)
					{
						a[j][l]=a[j][l-1];
						l++;
					}
				}

			}
		}


		for(j=0;j<r;j++)
		{


				if(a[j][0]=='?')
				{
					int l=j-1;

					while(a[l][0]=='?'  && l>=0)
					{
						l--;
					}

					if(a[l][0]!='?' && l>=0)
					{
						for(m=0;m<c;m++)
						{
							a[j][m]=a[l][m];
						}
					}
					else
					{
						l=j+1;
						while(a[l][0]=='?'  && l<r)
						{
							l++;
						}
						if(a[l][0]!='?' && l<r)
						{
							for(m=0;m<c;m++)
							{
								a[j][m]=a[l][m];
							}
						}


					}

				}


		}

		cout<<"Case #"<<i+1<<":\n";
		for(j=0;j<r;j++)
		{
			for(k=0;k<c;k++)
			cout<<a[j][k];

			cout<<"\n";
		}




	}
	return 0;
}

