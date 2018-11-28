#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	string s;
	int i, j, k, t, e, count;
	in >> t;
	for (i=1; i<=t; i++)
	{
		in >> s;
		in >> k;
		count = 0;
		for (j=0; j<s.size()-k+1; j++)
		if (s[j]=='-')
		{
			for (e = 0; e<k; e++)
			if (s[j+e]=='-') 
				s[j+e] = '+';
			else
				s[j+e] = '-';
			count++;
		}
		out << "Case #" << i << ": ";
		bool impossible = false;
		for (j=s.size()-k+1; j<s.size(); j++)
			if (s[j]=='-')
			{
				out << "IMPOSSIBLE" << endl;
				impossible = true;
				break;
			}
		if (!impossible) out << count << endl;
	}
	in.close();
	out.close();
	cout << "Program finish!" << endl;
	getchar();
	return 0;
}
