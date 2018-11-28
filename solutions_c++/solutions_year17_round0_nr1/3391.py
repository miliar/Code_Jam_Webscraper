#include <fstream>
#include <iostream>
#include <string>
using namespace std;

string fname = "A-small";

int main()
{
	string ifname = fname + ".in";
	string ofname = fname + ".out";
	ifstream f;
	ofstream of;
	of.open(ofname);
	f.open(ifname);
	int t;
	f >> t;
	for (int tt=0;tt<t;++tt){
		string s;
		int k;
		f >> s >> k;
		int i, cc =0;
		for (i=0;i<=s.length()-k;++i)
		{
			char c = s[i];
			if (c == '-')
			{
				++cc;
				for (int j=0;j<k;++j){
					if (s[i+j] == '-')
						s[i+j] = '+';
					else
						s[i+j] = '-';
				}
			}
		}
		bool ok = true;
		while (i < s.length())
		{
			if (s[i] == '-')
			{
				ok = false;
				break;
			}
			++i;
		}
		of << "Case #" << tt+1 << ": ";
		if (ok)
		{
			of << cc;
		}
		else
		{
			of << "IMPOSSIBLE";
		}
		of << "\n";
	}

	f.close();
	of.close();
}