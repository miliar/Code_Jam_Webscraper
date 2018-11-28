#include <iostream>
#include <fstream>
#include <string>
using namespace std;



int main() {

	ifstream in;
	in.open("A-large.in");

	ofstream out;
	out.open("output.txt");

	int T;

	in >> T;

	for (int i = 0; i < T; i++)
	{
		out << "Case #" << (i + 1) << ": ";

		string s;
		int k;
		int count = 0;
		int sublength = 0;
		bool counting = false;
		bool done = false;
		bool flip = false;

		in >> s;
		in >> k;

		if (s.length() < k)
		{
			for (int j = 0; j < s.length(); j++)
			{
				if (s[j] == '-')
				{
					out << "IMPOSSIBLE\n";
					done = true;
				}
			
			}
			if (!done) out << "0\n";
			continue;
		}

		for (int j = 0; j < s.length(); j++)
		{
			if (s[j] == '-')
			{
				sublength++;
				counting = true;

				if (sublength == k)
				{
					sublength = 0;
					counting = false;
					count++;
					for (int p = k; p > 0; p--)
					{
						s[j - p + 1] = '+';
					}
				}
			}
			else
			{
				if (counting)
				{
					counting = false;
					count++;

					//Do the flip
					for (int p = 0; p < k - sublength; p++)
					{
						if (j + p == s.length())
						{
							done = true;
							break;
						}
						if (s[j + p] == '+') s[j + p] = '-'; else s[j + p] = '+';
						flip = true;
					}
				}

				if (done)
					break;
				if (flip)
				{
					flip = false;
					counting = true;
					sublength = 1;
				}
				else
				{
					sublength = 0;
				}
				
			}
		}
		

		for (int j = s.length() - k + sublength; j < s.length(); j++)
		{
			if (s[j] == '-')
			{
				done = true;
				break;
			}
		}

		if (done)
		{
			out << "IMPOSSIBLE\n";
			//cout << i + 1 << " " << s << " IMPOSSIBLE" << endl;
		}
		else
		{
			out << count << endl;
			//cout << i + 1 << " " << s << " " << count << endl;
		}

	}


	in.close();
	out.close();
	system("PAUSE");

	return 0;
		
}