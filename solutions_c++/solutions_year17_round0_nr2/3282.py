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


long long solve(long long n)
{
	if (n < 10)
		return n;

	int d[32];
	int m = 0;
	long long t = n;
	do d[m++] = t % 10; while(t/=10);
	
	
	// d[0] - last digit, d[1] - pre-last digit, ... d[m-1] - first digit
	bool yes = true;
	for(int i = m-1; i > 0; --i)
		yes = yes && d[i] <= d[i-1];
	if(yes)
		return n;

	// 7182
	// 6282 --> 5382  4482 
	for(int i = m - 1; i > 0; --i)
	{
		if (d[i] > d[i-1])
		{
			d[i]--;
			for(int j = i - 1; j >= 0; --j)
				d[j] = 9;
			break;
			//while(d[i] > d[i-1])++d[i-1], --d[i];
		}
	}
	
	 
	t = 0;
	for(int i = m-1; i >=0; --i)
		t = t * 10 + d[i];

	return solve( t );//call recursive.
}
 
int solve(int testcase)
{
	
	long long n;
	cin >> n;
	//for(int i)
	 
	cout << "Case #"<< testcase << ": " << solve(n) << '\n';
	 

	return 0;
}
