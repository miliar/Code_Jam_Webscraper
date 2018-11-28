#include <iostream>
#include <vector>
#include <ostream>
#include <algorithm>
#include <iterator>
#include <array>
#include <cmath>
#include <list>

using namespace std;

template <class T> 
std::ostream& operator<<(std::ostream& os, const vector<T>& rhs)
{
	for (const auto& x : rhs)
		os << x;
	return os;
}

struct mM
{
	long m{0};
	long M{0};
};

mM Solve(long N, long K)
{
	list<long> A;
	A.push_back(N);
	mM w;
	for (long i = 0; i < K; ++i)
	{
		auto it = std::max_element(A.begin(), A.end());
		long T = *it;
		double half = (T-1.0)/2;
		long m = floor(half);
		long M = ceil(half);
		A.insert(it,M);
		A.insert(it,m);
		A.erase(it);
		w.m = m;
		w.M = M;
	}
	return w;
}

long BiggestPow2LessThan(long N)
{
	long p = 1;
	while (2*p <= N)
		p *= 2;
	return p;
}

int main() 
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		cout << "Case #" << i+1 << ": ";
		long N,K;
		cin >> N >> K;
// 		auto p = Solve(N,K);
// 		cout << p.M << " " << p.m << endl;
		
		long d = N-K;
		long racha = BiggestPow2LessThan(2*K);
		cout << (d+racha/2)/racha << ' ' << d/racha << endl;
		
	}
	
// 	for (int K = 1; K < 20; ++K)
// 	{
// 		cout << "For k = " << K << endl;
// 		for (int N = K; N < 30; ++N)
// 		{
// 			auto p = Solve(N,K);
// 			cout << p.M << ' ';
// 		}
// 		cout << endl;
// 	}
	
	
	return 0;
}
