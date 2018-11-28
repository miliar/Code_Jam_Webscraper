#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <set>

using namespace std;

void solve(string &s, int c, ofstream& out)
{
    int n=s.size();
	out<<"Case #"<<c<<": ";
	for (int i=n-2; i>=0; --i)
	{
	    if (s[i]>s[i+1])
		{
		    --s[i];
			for (int j=i+1; j<n; ++j)
				s[j]='9';
		}
	}
	if (s[0]=='0')
		s=s.substr(1, n-1);
	out<<s<<"\n";
}

int main()
{
    ifstream in("B-large.in");
	ofstream out("b_output.txt");
    int t;
	in>>t;
	int i=1;
	while (t--)
	{
	    string s;
		in>>s;
	    solve(s, i, out);
		++i;
	}
	return 0;
}