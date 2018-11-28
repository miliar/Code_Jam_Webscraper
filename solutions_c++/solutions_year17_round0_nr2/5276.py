#include<iostream>

using namespace std;

string s;
void f()
{
	for (int i = 0; i < s.size()-1; i++)
	{
		if (s[i] > s[i+1]) 
		{
			s[i]--;
			for (int j = i+1; j < s.size(); j++)
				s[j] = '9';
			return;
		}
	}
}

bool check()
{
	for (int i = 0; i < s.size()-1; i++)
		if (s[i] > s[i+1]) return false;
	return true;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int tt;
	cin >> tt;
	for (int t = 1; t <= tt; t++)
	{
		cin >> s;
		if (s.size() == 1)
		{
			cout << "Case #" << t << ": " << s << "\n";
			continue;
		}
		while(!check()) f();
		cout << "Case #" << t << ": ";
		int pos = 0;
		while(s[pos] == '0') pos++;
		if (pos == s.size()) 
		{
			cout << "0\n";
			continue;
		}
		for(int i = pos; i < s.size(); i++)
		{
			cout << s[i];
		}
		cout << "\n";
	}
	return 0;
}
