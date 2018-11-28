#include<bits/stdc++.h>
#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
	ifstream inFile;
	inFile.open("B-large.in");
	ofstream outFile;
	outFile.open("longoutput.txt");
	long long t;
	inFile>>t;
	for(long long j=1;j<=t;j++)
	{
		string s;
		inFile>>s;
		long long a[s.size()];
		for(long long i=0;i<s.size();i++)
		{
			a[i]=s[i]-'0';
		}
		long long level=-1;
		for(long long i=s.size()-1;i>0;i--)
		{
			if(a[i]<a[i-1])
			{
				a[i]=9;
				a[i-1]--;
				level=i;
			}
		}
		outFile<<"Case #"<<j<<": ";
		if(level!=-1)
		{
			if(a[0]!=0)
			{
				for(long long i=0;i<=level;i++)
				outFile<<a[i];
				for(long long i=level+1;i<s.size();i++)
				outFile<<"9";
			}
			else
			{
				for(long long i=1;i<=level;i++)
				outFile<<a[i];
				for(long long i=level+1;i<s.size();i++)
				outFile<<"9";
			}
		}
		else
		{
			for(long long i=0;i<s.size();i++)
			outFile<<a[i];
		}
		outFile<<endl;
	}
	inFile.close();
	outFile.close();
	return 0;
}
