#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <fstream>
using namespace std;
int main()
{
	fstream outfile,infile;
	infile.open("A-large.in",ios::in);
	outfile.open("output.txt",ios::out);
	int n;
	infile >> n;
	for(int t=1;t<=n;t++)
	{
		string str;
		int k;
		infile >> str >> k;
		int len = str.length(),flip=0;
		int arr[1005];
		for(int i=0;i<len;i++)
		{
			if(str[i]=='-') arr[i]=-1;
			else arr[i]=1;
		}
		for(int i=0;i<len-k+1;i++)
		{
			if(arr[i]==-1) 
			{
				flip++;
				arr[i]=1;
				for(int j=1;j<=(k-1) && j+i<len;j++)
				{
					arr[i+j]*=(-1);
				}
			}
		}
		bool noans=false;
		for(int i=0;i<len;i++) 
		{
			if(arr[i]==-1){
				noans=true;
				break;
			}
		}
		if(noans) outfile << "Case #" << t << ": IMPOSSIBLE" << endl;
		else outfile << "Case #" << t << ": " << flip << endl;
	}
	return 0;
}