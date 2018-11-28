#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	ifstream in;
	in.open("B-large.in");
	ofstream out;
	out.open("B-large.out");
	int t;
	in >> t;
	int testnum = 0;
	while (t--)
	{
		testnum++;
		string s;
		in >> s;
		int len = s.size();
		for (int i = len - 1; i>0; i--)
		{
			if (s[i - 1]>s[i])
			{
				s[i - 1]--;
				for (int j = i; j<len; j++)
					s[j] = '9';
			}
		}
		out << "Case #" << testnum << ": ";
		for (int i = 0; i<len; ++i)
		{
			if (s[i] != '0')
			{
				for (int j = i; j<len; ++j)
					out << s[j];
				out << endl;
				break;
			}
		}
	}
	in.close();
	out.close();
}
