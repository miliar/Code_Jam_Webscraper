#include <iostream>
#include <vector>
#include <ostream>
#include <algorithm>
#include <iterator>
#include <array>
#include <cmath>

using namespace std;

template <class T> 
std::ostream& operator<<(std::ostream& os, const vector<T>& rhs)
{
	for (const auto& x : rhs)
		os << x;
	return os;
}

template <class IntType>
long InterpretBaseK(long k, const vector<IntType>& bla)
{
	long suma = 0;
	long power = 1;

	for (auto it = bla.rbegin(); it != bla.rend(); ++it)
	{
		suma += power * static_cast<IntType>(*it);
		power *= k;
	}

	return suma;
}

inline vector<int> NumberBaseB(long n, int b)
{
	vector<int> toReturn;

	while (n)
	{
		toReturn.push_back(n % b);
		n /= b;
	}

	std::reverse(toReturn.begin(), toReturn.end());
	return toReturn;
}

template <class Iter>
bool IfFilledWithKWouldItBeSmaller(Iter a, Iter b, int k)
{
	for (auto i = a; i != b; ++i)
	{
		if (*i > k)
			return true;
		if (*i < k)
			return false;
	}
	return true;
}

template <class Iter>
void Solve(vector<int>& result, Iter a, Iter b)
{
	if ((a+1) == b)
	{
		result.push_back(*a);
		return;
	}
	
	if (IfFilledWithKWouldItBeSmaller(a,b,*a))
	{
		result.push_back(*a);
		Solve(result,a+1,b);
		return;
	} else
	{
		if (!result.empty() || *a != 1)
			result.push_back(*a-1);
		for (auto it = a+1; it != b; ++it)
			result.push_back(9);
	}
	
	
}

vector<int> Solve(long N)
{
	if (N < 10)
		return {int(N)};
	vector<int> D = NumberBaseB(N,10);
// 	cout << "D = " << D << endl;
	vector<int> result;
	Solve(result, D.begin(), D.end());
	return result;
}

int main() 
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		cout << "Case #" << i+1 << ": ";
		long N;
		cin >> N;
// 		cout << N << ",";
		cout << Solve(N) << endl;
		
	}
	
	
	return 0;
}
