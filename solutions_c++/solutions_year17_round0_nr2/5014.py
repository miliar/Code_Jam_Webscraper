#include <iostream>
#include <cstdio>
#include <fstream> 

using namespace std;

string removeLeadingzeroes(string s)	{
	int n = s.length();
	string ret = "";
	bool zeroes = true;
	for(int i = 0 ; i < n ; ++i)	{
		if(zeroes && s[i] == '0'){}
		else	{
			zeroes = false;
			ret += s[i];
		}
	}
	return ret;
}

string getAnswer(string s)	{
	int n = s.length();
	bool happened = true;
	while(happened)	{
		happened = false;
		for(int i = 0 ; i < n - 1; ++i)	{
			if(s[i] > s[i+1])	{
				happened = true;
				s[i] = s[i]-1;
				for(int j = i+1; j < n ; ++j)	{
					s[j] = '9';
				}
				break;
			}
		}
	}
	return removeLeadingzeroes(s);
}

int main()	{

	int t,caseNum = 0;
	string s;
	ifstream in; in.open("/Users/paliws/Downloads/input.txt");
	ofstream out; out.open("/Users/paliws/Downloads/output.txt");
	in>>t;
	while(t--)	{
		++caseNum;
		in>>s;
		string answer = getAnswer(s);
		out<<"Case #"<<caseNum<<": "<<answer;
		if(t != 0)	{
			out<<endl;
		}
	}
	in.close();
	out.close();
	return 0;
}