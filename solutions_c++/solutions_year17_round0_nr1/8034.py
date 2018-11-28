#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
	int j = 1;
	ifstream inp  ("input.txt");
	ofstream out ("output.txt");
	int t;
	inp >> t;
	string s; int k;
	long long ans;
	bool x;
	int w;
	while (t != 0)
	{
		ans = 0;
		x = true;
		inp >> s; inp >> k;
		 w = s.size();
		for (int i = 0; i <w; ++i)
		{
			if (s[i] =='-')
			{
				if (i + k > w)
				{
					x = false; break;
				}
				for (int j = i; j < i + k ; ++j)
				{
					if (s[j] == '+')
					{
						s[j] = '-';
					}
					else
						s[j] = '+';
				}
				ans ++ ;
			}
			
		}
		
		if(!x)
			out << "Case #" << j << ": " << "IMPOSSIBLE" << endl;
		else
		out << "Case #" << j << ": " <<ans<<endl;
		++j;
		--t;
	}
	

}