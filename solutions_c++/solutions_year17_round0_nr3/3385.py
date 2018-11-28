#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <stack>
#include <queue>
#include <list>
#include <utility>
#include <functional>
#include <numeric>
#include <algorithm>

using std::cin; using std::cout; using std::endl; using std::string; using std::vector;

int solve(int testcase);

int main(int argc, char *argv[]){

#ifndef ONLINE_JUDGE
	//freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif 

	::std::ios::sync_with_stdio(false); ::std::cin.tie(0); ::std::cout.tie(0);

	int testcase;
	cin >> testcase;
	for(int t = 1; t <= testcase ; ++ t)
		solve(t);

	return 0;
}

typedef ::std::pair<long long, long long > pii64;


pii64 solve(long long n, long long k)
{

	pii64 r;
	
	::std::set<pii64> s;
	
	s.insert(pii64(-n, 1));

	for(int i = 0; i != k ; ++i)
	{
		if (s.empty())
		{
			r = pii64(0,0);
			break;
		}
		pii64 p = *s.begin();
		s.erase(s.begin());

		long long len = -p.first, start = p.second;
		long long end = start + len - 1;

		long long middle = (start + end)/2;

		long long L = middle - start, R = end - middle;
		r = pii64( std::max(L,R) , ::std::min(L,R));
		
		if (L > 0) s.insert(pii64(-L, start));
		if (R > 0) s.insert(pii64(-R, middle+1));
	}
	return r;
}

 
int solve(int testcase)
{
	
	long long n, k;
	cin >> n >> k;
	 
	 pii64 r = solve(n,k);

	cout << "Case #"<< testcase << ": " << r.first << ' ' << r.second << '\n';
	 

	return 0;
}
