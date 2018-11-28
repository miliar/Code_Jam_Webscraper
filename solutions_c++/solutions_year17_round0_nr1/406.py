#include <iostream>
#include <vector>
#include <ostream>
#include <algorithm> // for copy
#include <iterator>
#include <array>

using namespace std;

template <class T> 
std::ostream& operator<<(std::ostream& os, const vector<T>& rhs)
{
	os << "[ ";
	for (const auto& x : rhs)
		os << x << " ";
	os << "]";
	return os;
}

void flip(char& a)
{
	if (a == '+')
		a = '-';
	else
		a = '+';
}

int solve(string& s, int k)
{
	int numtimes = 0;
	for (int i = 0; i < s.size(); ++i)
	{
		if (s[i] == '-')
		{
			if (i + k > s.size())
				return -1;
			for (int j = 0; j < k; ++j)
			{
				flip(s[i+j]);
			}
			++numtimes;
// 			cout << "flipping to " << s << endl;
		}
	}
	return numtimes;
}

int main() 
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		cout << "Case #" << i+1 << ": ";
		string s;
		int k;
		cin >> s >> k;
		int x = solve(s,k);
		if (x == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << x << endl;
	}
	
	
	return 0;
}
