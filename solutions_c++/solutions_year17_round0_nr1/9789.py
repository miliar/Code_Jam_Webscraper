#include<iostream>
#include<cstring>
#include<fstream>
#include<stdio.h>
using namespace std;
int main()
{
	ifstream fin("A-small-attempt1.in");
    ofstream fout("output.out");
	int t;
	fin>>t;
	for (int j = 1; j <= t; ++j) {
		int n,k,count=0;
		char s[20];
		fin>>s>>k;
		n=strlen(s);
		for(int i=0;i<=n-k;){
			if(s[i]=='+')
				i++;
			else if(s[i]=='-')
			{	count++;
				for(int m=i;m<i+k;m++)
				{	if(s[m]=='+')
						s[m]='-';
					else
						s[m]='+';
				}
				i++;
			}
		}
		int f=0;
		for(int i=0;i<n;i++)
		{
			if(s[i]!='+')
			{
				f=1;
				break;
			}
		}
		if(f==0)
			fout<< "Case #" << j << ": " << count << endl;
		else
			fout<< "Case #" << j << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}
