#include <iostream>
#include <fstream>
#include <string>

using namespace std;


string lasttidy(string s)
{
	if (s.size()==1) return s;
	string ans = s;
	int i,j;
	i = 0;
	j = 1;
	while (j<s.size())
	{
		if (s[j]-s[i]==0) j++;
		else
			if (s[j]-s[i]>0)
			{
				i = j;
				j = i+1;
			}
			else
			{
				char c = s[i]-1;
				if ((i==0)&&(c=='0'))
				{
					ans.clear();
					for (int k=0; k<s.size()-1; k++)
						ans = ans + "9";
					return ans;
				}
				else
				{
					ans[i] = c;
					for (int k=i+1; k<s.size(); k++)
						ans[k] = '9';
					return ans;
				}	
			}
	}
	return ans;
}

int main()
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");

	int t;
	in >> t;
	for (int i=0; i<t; i++)
	{
		string s;
		in >> s;
		out << "Case #" << i+1 << ": " << lasttidy(s) << endl;
	}
	in.close();
	out.close();
	cout << "Program finished!" << endl;
	getchar();
	return 0;
}

