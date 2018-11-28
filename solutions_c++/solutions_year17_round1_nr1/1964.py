#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
	fstream outfile,infile;
	infile.open("A-large.in",ios::in);
	outfile.open("output.txt",ios::out);
	int cas;
	infile >> cas;
	for(int t=1;t<=cas;t++)
	{
		int r,c;
		string str[30];
		infile >> r >> c;
		for(int i=0;i<r;i++)
		{
			infile >> str[i];
		}
		for(int i=0;i<r;i++)
		{
			char tmp=' ';
			for(int j=0;j<c;j++)
			{
				// cout << tmp << endl;
				if(str[i][j]!='?') tmp = str[i][j];
				else {
					if(tmp!=' ') str[i][j]=tmp;
				}
			}
		}
		for(int i=0;i<r;i++)
		{
			char tmp=' ';
			for(int j=c-1;j>=0;j--)
			{
				if(str[i][j]!='?') tmp = str[i][j];
				else {
					if(tmp!=' ') str[i][j]=tmp;
				}
			}
		}
		// for(int i=0;i<r;i++)
		// {
		// 	cout << str[i] << endl;
			
		// }
		for(int i=0;i<r;i++)
		{
			if(str[i][0]=='?')
			{
				for(int j=i;j<r;j++) 
				{
					if(str[j][0]!='?') 
						{
							str[i]=str[j];
							break;
						}
				}
			}
		}
		for(int i=r-1;i>=0;i--)
		{
			if(str[i][0]=='?')
			{
				for(int j=i;j>=0;j--) 
				{
					if(str[j][0]!='?') 
						{
							str[i]=str[j];
							break;
						}
				}
			}
		}
		outfile << "Case #" << t << ":" << endl;
		for(int i=0;i<r;i++)
		{
			outfile << str[i] << endl;
		}
	}



	return 0;
}