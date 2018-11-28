#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;
int main()
{
	ofstream fout;
	ifstream fin;
	fout.open("output.txt");
	fin.open("A-large.in");
	int t;
	fin >> t;
	for(int h=0;h<t;h++)
	{
		string s;
		fin >> s;
		int k;
		fin >> k;
		int count=0;
		for(int i=0;i+k-1<s.size();i++)
		{
			if(s[i]=='+')
				continue;
			count++;
			for(int j=0;j<k;j++)
			{
				if(s[i+j]=='+')
					s[i+j]='-';
				else
					s[i+j]='+';
			}
		}
		bool finish=true;
		for(int i=0;i<s.size();i++)
		{
			if(s[i]=='-')
				finish=false;
		}
		fout << "Case #" << h+1 << ": ";
		if(finish)
			fout << count << endl;
		else
			fout << "IMPOSSIBLE" << endl;
	}
	fin.close();
	fout.close();
}