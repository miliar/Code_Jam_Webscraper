#include <iostream>
#include <vector>
#include <string>
#include <ostream>
#include <algorithm>
#include <iterator>
#include <array>
#include <set>
#include <cassert>

using namespace std;

template <class T> 
std::ostream& operator<<(std::ostream& os, const vector<T>& X)
{
	for (const auto& x : X)
		os << x << " ";
	return os;
}

void Solve(vector<string>& A)
{
	
	for (int x = 0; x < A.size(); ++x)
	{
		bool seenfirst = false;
		char current = '*';
		for (int y = 0; y < A[0].size(); ++y)
		{
			if (A[x][y] == '?')
			{
				if (seenfirst)
					A[x][y] = current;
			} else
			{
				seenfirst = true;
				current = A[x][y];
			}
		}
	}
	
	for (int x = 0; x < A.size(); ++x)
	{
		bool seenfirst = false;
		char current = '*';
		for (int y = A[x].size()-1; y >= 0; --y)
		{
			if (A[x][y] == '?')
			{
				if (seenfirst)
					A[x][y] = current;
			} else
			{
				seenfirst = true;
				current = A[x][y];
			}
		}
	}
	
	for (int y = 0; y < A[0].size(); ++y)
	{
		bool seenfirst = false;
		char current = '*';
		for (int x = 0; x < A.size(); ++x)
		{
			if (A[x][y] == '?')
			{
				if (seenfirst)
					A[x][y] = current;
			} else
			{
				seenfirst = true;
				current = A[x][y];
			}
		}
	}
	
	for (int y = 0; y < A[0].size(); ++y)
	{
		bool seenfirst = false;
		char current = '*';
		for (int x = A.size()-1; x >= 0; --x)
		{
			if (A[x][y] == '?')
			{
				if (seenfirst)
					A[x][y] = current;
			} else
			{
				seenfirst = true;
				current = A[x][y];
			}
		}
	}
	
	
	
	
	for (auto& s : A)
		cout << s << endl;
}

int main() 
{
	int T;
	cin >> T;

	for (int t = 0; t < T; ++t)
	{
		cout << "Case #" << t+1 << ':' << endl;
		int R,C;
		cin >> R >> C;
		vector<string> A(R);
		for (int x = 0; x < R; ++x)
		{
			cin >> A[x];
		}
			Solve(A);
	}
	
	return 0;
}
