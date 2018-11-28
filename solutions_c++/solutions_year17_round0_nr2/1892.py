#define _CRT_SECURE_NO_WARNINGS
#include <unordered_map>
#include <unordered_set>
#include <functional>
#include <algorithm>
#include <memory.h>
#include <iostream>
#include <iterator>
#include <ostream>
#include <iomanip>
#include <cstring>
#include <sstream>
#include <cassert>
#include <cstdlib>
#include <istream>
#include <fstream>
#include <climits>
#include <complex>
#include <memory>
#include <string>
#include <bitset>
#include <vector>
#include <cstdio>
#include <ctime>
#include <cmath>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef complex <ld> cd;

const bool db = false;

#define fs first
#define X first 
#define ft first

#define sd second
#define Y second
#define sc second

#define mp make_pair
#define pb push_back
#define ppb pop_back

#define inf 1000000007
#define nmax 100100
#define mmax 100100
#define eps 1e-12
const int mod7 = 1e9 + 7;
ll brute(ll x)
{
	for(;;x--){
		string s = to_string(x);
		bool isPretty = true;
		for (int i = 0; i + 1 < s.length(); i++)
		{
			if (s[i] > s[i + 1])
			{
				isPretty = false;
			}
		}
		if (isPretty)
			return x;
	}
}

ll solve(ll x)
{
	string s = to_string(x);
	bool isPretty = true;
	for(int i = 0; i + 1 < s.length(); i++)
	{
		if (s[i] > s[i + 1])
		{
			isPretty = false;
		}
	}
	if (isPretty)
		return x;
	for(int i = 1; i < s.length(); i++)
	{
		if(s[i] < s[i-1])
		{
			int j = i-1;
			while (j > 0 && s[j - 1] == s[i-1])
				j--;
			ll pw = 1;
			for (int step = 0; step < s.length()-j-1; step++)
				pw *= 10;
			x = (x / pw) * pw;
			return x - 1;
		}
	}
}

int main() {
#ifdef LOCAL
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		ll x;
		cin >> x;
		cout << "Case #"<<i <<": " << solve(x) << endl;
		
	}
}