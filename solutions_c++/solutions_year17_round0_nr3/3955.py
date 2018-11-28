#define _CRT_SECURE_NO_WARNINGS
#pragma once
#include<iostream>
#include<string>
#include<xstring>
#include<sstream>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<bitset>
#include<iomanip>
#include<algorithm>
#include<cmath>
#include<map>
#include<functional>

template< class T>
T gcd(T a, T b) { return a == 0 ? b : gcd(b%a, a); }
template< class T>
T lcm(T a, T b) { return b*(a / gcd(a, b)); }
template<class T>
T  t_sum(T a) { return (a*(a + 1)) / 2; }
template<class T>
T left(T x) { return (x << 1); }
template<class T>
T right(T x) { return ((x << 1) + 1); }
template < class T >
T lsb(T x) { return x&(-x); }
template< class  T , class N>
T pw(T a, N b)

{
	T ans = 1;
	while (b != 0)
	{
		if (b % 2 == 1)
		{
			ans *= a;
		}
		a *= a;
		b = b >> 1;
    }
	return ans;
}



#define fo(i,m,n) for(int i = m ; i < n ; i++)
#define pii pair<int ,int>
#define gt(n) scanf("%d",&n)
#define gtl(n) scanf("%lld" ,&n)
#define ii pair<int,int>

using namespace std;
pair <long long ,pair<long, long>> fix(long long x, long long y)
{
	
	priority_queue < pair<long long ,pair<long long, long long > > > q1;
	pair<long long ,pair<long long, long long >> ans;
	ans.first = x + 1;
	ans.second.first = 0;
	ans.second.second = x + 1;
	q1.push(ans);
	while (y--)
	{
		pair<long long, pair<long long, long long >> T = ans = q1.top();
		q1.pop();
		long long sit = (T.second.first + T.second.second)/2;
		q1.push({sit-T.second.first,{T.second.first,sit} });
		q1.push({ T.second.second - sit,{sit,T.second.second} });
	}
	return ans;
}

int main(){

	/*freopen("input.in", "r", stdin);
    freopen("output.txt", "wt", stdout);
	*/
	int cse = 1;
	long long t, k, n;
	cin >> t;
	
	while (t--)
	{
		cin >> n>>k;
		pair<long long ,pair<long long, long long >> ans = fix(n, k);
		long long sit = (ans.second. first + ans.second.second)/2;
		long long t1  = ans.second.first;
		long long t2  = ans.second.second;
		
		cout << "Case #" << cse++ << ": " << max(sit - t1, t2 - sit) - 1 << " " << min(sit - t1, t2 - sit) - 1 << endl;
	}
	return 0;
}