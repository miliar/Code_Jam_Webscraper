#include <iostream>
#include <cstdio>
#include <fstream> 

using namespace std;

void flip(string &s, int idx, int k)	{
	for(int i = 0 ; i < k ; ++i)	{
		if(s[idx + i] == '-')	{
			s[idx + i] = '+';
		}else	{
			s[idx + i] = '-';
		}
	}
}

int getAnswer(string s, int k)	{
	int n = s.length();
	int ctr = 0;
	for(int i = 0 ; i <= n - k ; ++i)	{
		if(s[i]=='-')	{
			flip(s,i,k);
			++ctr;
		}
	}
	for(int i = n - k + 1 ; i < n ; ++i)	{
		if(s[i]=='-')return -1;
	}
	return ctr;
}

int main()	{

	int t,k,caseNum = 0;
	string s;
	ifstream in; in.open("/Users/paliws/Downloads/A-large.in");
	ofstream out; out.open("/Users/paliws/Downloads/output.txt");
	in>>t;
	while(t--)	{
		++caseNum;
		in>>s;
		in>>k;
		int answer = getAnswer(s,k);
		if(answer != -1)	{
			out<<"Case #"<<caseNum<<": "<<answer;
		}else	{
			out<<"Case #"<<caseNum<<": IMPOSSIBLE";
		}
		if(t != 0)	{
			out<<endl;
		}
	}
	in.close();
	out.close();
	return 0;
}