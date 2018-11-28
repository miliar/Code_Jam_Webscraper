#include <iostream>
#include <vector>
#include <map>
#include <cmath>

#include <sstream>

using namespace std;

bool is_tidy(int n)
{
	stringstream ss;
	ss << n;
	string s = ss.str();
	for(int i = 1; i < s.size(); i++)
	{
		if(s[i - 1] > s[i])
			return false;
	}
	return true;
}

string digits(int n)
{
	stringstream ss;
	ss << n;
	return ss.str();
}

map<unsigned long long, unsigned long long> spots;

int main()
{
	int c;
	cin >> c;
	for(int i = 1; i <= c; i++)
	{
		unsigned long long n, k, val, key, s, l;
		cin >> n >> k;

		spots[n] = 1;
		key = n;
		val = 1;

		while(k > val)
		{
			k -= val;
			spots.erase(key);
			spots[(key - 1) / 2] += val;
			spots[key / 2] += val;
			key = spots.rbegin()->first;
			val = spots.rbegin()->second;
			// cout << key << " " << val << endl;
		}

		s = (key - 1) / 2;
		l = key / 2;

		cout << "Case #" << i << ": " << l << " " << s << endl;
		spots.clear();
	}
	return 0;
}