/*
 * GCJ_17_1A_A.cpp
 *
 *  Created on: 15-Apr-2017
 *      Author: neeraj
 */

#include<iostream>
#include <fstream>
#include<vector>
using namespace std;


int main() {
	long long int i,j,k,l,m,n,r,t,c,y,z;
	ifstream fin;
	ofstream fout;
	fin.open("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/A-large.in", ios::in);
	fout.open("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/A-large-out.txt",ios::trunc);

	fin>>t;

	for(i=0;i<t;i++)
	{
		fin>>r>>c;

		vector< vector<char> > a;
		char x;
		z=0;//number of ?
		for(j=0;j<r;j++)
		{
			vector<char>b;
			for(l=0;l<c;l++)
			{
				fin>>x;
				if(x=='?')
					z++;
				b.push_back(x);
			}
			a.push_back(b);
		}

		if(z==0)
		{
			fout<<"Case #"<<i+1<<":\n";

			for(j=0;j<r;j++)
			{
				for(l=0;l<c;l++)
					fout<<a[j][l];

				fout<<"\n";
			}
		}
		else
		{
			z=0;
			vector<int> e(r,0);
			for(j=0;j<r;j++)
			{
				z=0;
				for(l=0;l<c;l++)
				{
					if(a[j][l]=='?')
					{
						if(a[j][l-1]!='?' && l!=0)
						{
							a[j][l]=a[j][l-1];
						}
						else if(a[j][l+1]!='?' && l!=c-1)
						{
							if(z>0)
							{
								while(z!=0)
								{
									a[j][l-z]=a[j][l+1];
									z--;
								}
								a[j][l]=a[j][l+1];
							}
							else
								a[j][l]=a[j][l+1];

						}
						else
							z++;
					}
				}
				if(z==c)
				{
					e[j]=1;
				}
			}
			z=0;
			for(j=0;j<r;j++)
			{
				if(e[j]==1)
				{
					if(e[j-1]==0 && j!=0)
					{
						a[j]=a[j-1];e[j]=0;
					}
					else if(e[j+1]==0 && j!=r-1)
					{
						if(z>0)
						{
							while(z!=0)
							{
								a[j-z]=a[j+1];z--;
							}
							a[j]=a[j+1];
						}
						else
							a[j]=a[j+1];

					}
					else
						z++;
				}
			}

			fout<<"Case #"<<i+1<<":\n";
			for(j=0;j<r;j++)
			{
				for(l=0;l<c;l++)
					fout<<a[j][l];

				fout<<"\n";
			}
		}
	}
	return 0;
}
#if 0
ifstream fin;
ofstream fout;
fin.open("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/A-small-attempt0.in", ios::in);
fout.open("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/A-small-out.txt",ios::trunc);

fin>>t;
for(int ii=1;ii<=t;ii++)
{
	int r,c;
	fin>>r>>c;
	char a[r][c];

	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			fin>>a[i][j];
		}
	}

	int flag=0,posr,posc;

	if(a[0][0]=='?')
	{
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(a[r][c]!='?')
				{
					posr=i;
					posc=j;
					flag=1;
					break;
				}
			}
			if(flag==1)
				break;
		}


		for(int i=0;i<=posr;i++)
			for(int j=0;j<=posc;j++)
				a[i][j]=a[posr][posc];
	}

	for(int i=0;i<1;i++)
	{
		for(int j=0;j<c;j++)
		{
			if(a[i][j]=='?')
				a[i][j]=a[i][j-1];
		}
	}

	for(int i=1;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			if(a[i][j]=='?')
				a[i][j]=a[i-1][j];
		}
	}

	fout<<"Case #"<<ii<<":"<<endl;

	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			fout<<a[i][j];
		}
		fout<<endl;
	}
}

return 0;
}

#endif
