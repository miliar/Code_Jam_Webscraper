#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>


using namespace std;
int T;
vector < pair <string,int> > strs;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	cin >> T;
	strs.resize(T,make_pair("",0));
	string s;
	for (int i = 0; i < T; ++i)
	{
		getline(cin, s);

		
		if (s != "")
		{
			strs[i].first = s;
			int tmk = 0;
			int cntr = 0;
			for (int j = 0; j < s.size(); ++j)
			{
				if (((s[j] - 48) >= 0) && (s[j] - 48 <= 9))
				{
					cntr++;
					if (cntr > 1)
					{
						tmk = tmk * 10 +(s[j] - 48);
					}
					else if (cntr == 1)
					{
						tmk = s[j] - 48;
					}
				}
					
			}
			strs[i].second = tmk; ;
			for (int j = 0; j < cntr + 1; ++j)
			{
				strs[i].first.pop_back();
			}
			
			
		}
		else i--;
	}

	
	for (int i = 0; i < strs.size(); ++i)
	{
		string tmp = strs[i].first;
		string ideal;
		for (int j = 0; j < tmp.size(); ++j)
		{
			ideal.append("+");
		}

		int k = strs[i].second;
		int steps = 0;

		while (true)
		{
			bool flag = 0;
			for (int j = 0; j < ideal.size(); ++j)
			{
				if ((tmp[j] != ideal[j]) && (j < (ideal.size() - k+1)))
				{
					steps++;
					for (int z = j; z < j + k ; ++z)
					{
						
						if (ideal[z] == '-') ideal[z] = '+';
						else if(ideal[z] == '+') ideal[z] = '-';
						
					}
					if (ideal == tmp) { flag = true; break; }
					j = 0;
				}
				if (j >= (ideal.size() - k+1)) { flag = true; break; }
				
			}
			if (flag) break;
		}
		if (ideal == tmp)
			cout << "Case #"<<i+1<<": "<< steps << endl;
		else
			cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
		
		
	}


}