#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;
static string solve(vector<int> vec)
{
	string res="";
	for(int i=1;i<vec.size();i++)
	{
		if(vec[i]<vec[i-1])
		{
			i--;
			while(i>0)
			{
				if(vec[i]==vec[i-1])
					i--;
				else
					break;
			}
			vec[i]--;
			for(int j=i+1;j<vec.size();j++)
				vec[j]=9;
			break;
		}
	}
	bool start=false;
	for(int i=0;i<vec.size();i++)
	{
		if(vec[i]!=0)
			start=true;
		char c=vec[i]+('0');
		if(start)
			res=res+c;
	}
	if(res=="")
		res='0';
	return res;
}
int main()
{
	ofstream fout;
	ifstream fin;
	fout.open("output.txt");
	fin.open("B-large.in");
	int t;
	fin >> t;
	for(int i=0;i<t;i++)
	{
		string s;
		fin >> s;
		vector<int> vec(s.size());
		for(int i=0;i<s.size();i++)
			vec[i]=s[i]-'0';
		fout << "Case #" << i+1 << ": ";
		fout <<solve(vec) << endl;
	}
}