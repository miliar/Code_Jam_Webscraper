#include <bits/stdc++.h>

using namespace std;

typedef long long ll;




string tidifyIt(string s)
{
	string newS;
	bool nineIt = false;
	for(int i = 0; i < s.size(); i++)
	{
		if(nineIt)
		{
			newS.push_back('9');
		}else if(i == s.size() - 1)
		{
			newS.push_back(s.at(i));
		}else
		{
			if(s.at(i) > s.at(i + 1))
			{
				nineIt = true;
				newS.push_back(s.at(i) - 1);
			}else
			{
				newS.push_back(s.at(i));
			}
		}
	}
	return newS;

}

string removeLeading(string s)
{
	string newS;
	bool addIt = false;
	for(int i = 0; i < s.size(); i++)
	{
		if(s.at(i) != '0')
		{
			addIt = true;
		}
		if(addIt)
		{
			newS.push_back(s.at(i));
		}
		
	}
	if(newS == "")
	{
		return "0";
	}else
	{
		return newS;
	}
}

int main()
{
	
	ll casses;
	cin >> casses;
	for(int caseNum = 0; caseNum < casses; caseNum++)
	{
		string s;
		cin >> s;
		for(int i = 0; i < 50; i++)
		{
			s = tidifyIt(s);
		}
		cout << "Case #" << caseNum + 1 << ": " << removeLeading(s) << endl;
	}	
	return 0;
}










