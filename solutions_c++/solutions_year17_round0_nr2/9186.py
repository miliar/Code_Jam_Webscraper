#include<conio.h>
#include<iostream.h>
#include<string.h>
#include<iomanip.h>
#include<stdio.h>
#include<process.h>
#include<stdlib.h>
#include<fstream.h>

void main()
{
	clrscr();

	ifstream infile;
	infile.open("bsmall.in");

	ofstream outfile;
	outfile.open("outtidy.txt");

	int t;
	infile>>t;

	for(int i=0;i<t;i++)
	{
		unsigned long long int m[110];
		int flag=1;
		unsigned long long int n, d[2];
		infile>>m[i];
		n=m[i];
		unsigned long long int p=n;
		for(p;p>0&&flag==1&&!kbhit();p--)
		{
			n=p;
			flag=0;
			while(n>0&&flag==0)
			{
				d[0]=n%10;
				n=n/10;
				d[1]=n%10;
				if(d[0]<d[1])
				{
					flag=1;
				}
			}
			if(flag==0)
				outfile<<"Case #"<<i+1<<": "<<p<<endl;
		}
	}
	getch();
}