#include<fstream>

using namespace std;


bool done(bool *v, int length)
{
	for (int i = 0; i < length; i++)
	{
		if (!v[i]) return false;
	}
	return true;
}
bool same(bool *v, bool *was, int length)
{
	for (int i = 0; i < length; i++)
	{
		if (v[i] != was[i]) return false;
	}
	return true;
}

void main()
{
	ifstream in("A-large.in");
	ofstream out("out.txt");
	int t;
	in >> t;
	for (int i = 1; i <= t; i++)
	{
		bool was[2][1001] = {false};
		bool v[1001] = { false };
		int flips = 0;
		char s[1001];
		in >> s;
		int fl;
		in >> fl;
		int length = strlen(s);
		for (int i = 0; i < length; i++)
		{
			if (s[i] == '-') v[i] = false;
			else v[i] = true;
		}
		while (!done(v,length) && flips != -1)
		{
			for (int i = 0; i < length; i++)
			{
				if (!v[i])
				{
					while (i + fl > length) i--;
					for (int p = 0; p < fl; p++)
					{
						v[i + p] = !v[i + p];
					}
					if (same(v,was[0],length)) { flips = -1; break; }
					for (int i = 0; i < length; i++)
					{
						was[0][i] = was[1][i];
						was[1][i] = v[i];
					}
					flips++;
				}
			}
		}
		if(flips != -1)out <<"Case #" <<i << ": " <<flips << endl;
		else out << "Case #" << i << ": IMPOSSIBLE" << endl;
	}
}