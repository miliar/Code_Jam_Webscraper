#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

char ch[30][30];
int R=0,C=0;

int populate(int i,int j, char c)
{
	int l=j-1, right=j+1;

	while(right<C && ch[i][right]=='?')
	{
		ch[i][right]=c;
		right++;
	}
	while(l>=0 && ch[i][l]=='?')
	{
		ch[i][l]=c;
		l--;
	}

	right--;
	l++;

	for(int ii=i-1;ii>=0;ii--)
	{
		bool f=false;
		for(int jj=l;jj<=right;jj++)
		{
			if(ch[ii][jj]!='?')
			{
				f=true;
				break;
			}
		}

		if(f)
		{
			break;
		}
		else
		{
			for(int jj=l;jj<=right;jj++)
			{
				ch[ii][jj]=c;
			}
		}
	}

	for(int ii=i+1;ii<R;ii++)
	{
		bool f=false;
		for(int jj=l;jj<=right;jj++)
		{
			if(ch[ii][jj]!='?')
			{
				f=true;
				break;
			}
		}

		if(f)
		{
			break;
		}
		else
		{
			for(int jj=l;jj<=right;jj++)
			{
				ch[ii][jj]=c;
			}
		}
	}
	return 0;
}

int main()
{
	char input[]="input.in";
	char output[]="outut.out";



	FILE * fin = fopen("input.in", "r+");
	FILE * fin2 = fopen("output.out", "w+");

	int t=0,QWERTY=1;
	fscanf(fin,"%d", &t);
		
	while(t-->0)
	{
		fscanf(fin,"%d%d", &R, &C);

		for(int i=0;i<R;i++)
		{
			fscanf(fin,"%s",&ch[i][0]);
		}

		vector<bool>F(50, true);
		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
			{
				if((ch[i][j]>='A' && ch[i][j]<='Z') && F[ch[i][j]-'A'])
				{
					populate(i,j,ch[i][j]);
					F[ch[i][j]-'A'] = false;
				}
			}
		}

		fprintf(fin2,"Case #%d:\n",QWERTY);QWERTY++;

		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
			{
				fprintf(fin2,"%c",ch[i][j]);
			}
			fprintf(fin2,"\n");
		}
	}

	return 0;
}