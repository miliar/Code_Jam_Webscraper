#include<iostream.h>
#include<conio.h>
#include<iomanip.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<fstream.h>

const int C=1100;

void main()
{
	clrscr();

	ifstream infile;
	infile.open("larger.in");
	int t;
	infile>>t;

	ofstream outfile;
	outfile.open("largeout.txt");

	char *n;
	n = new char[C];
	int l[1100];
	for(int i=0;i<t;i++)
	{
		int cntm=0;
		int flag=0, tries=0;
		infile>>n;
		infile>>l[i];
		for(int j=0;j<strlen(n);j++)
			if(n[j]=='-')
				cntm++;
		for(j=0;j<strlen(n)&&flag==0;j++)
		{
			if(cntm<l[i]&&j>strlen(n)-l[i])
			{
				outfile<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
				flag=1;
				break;
			}
			else if(n[j]=='-')
			{
				for(int z=j;z<j+l[i];z++)
				{
					if(n[z]=='-')
					{
						n[z]='+';
						cntm--;
					}
					else if(n[z]=='+')
					{
						n[z]='-';
						cntm++;
					}
				}
				tries++;
			}
			if(cntm==0)
			{
				outfile<<"Case #"<<i+1<<": "<<tries<<endl;
				flag=1;
			}

		}
		delete [] n;
	}
	getch();
}