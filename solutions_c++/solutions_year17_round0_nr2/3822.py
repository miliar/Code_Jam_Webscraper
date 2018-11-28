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


int main(){
	freopen("input.in", "r", stdin);
    freopen("output.txt", "wt", stdout);

	int t;
	string s;
	int cse = 1;
	cin >> t;

	while (t--)
	{
		cin >> s;
		
		for (int j = 0; j < s.size(); j++)
		{
			bool flag = false;
			for (int i = 0; i <s.size()-1; i++)
			{
				if (s[i] > s[i + 1])
				{
					if (!flag)
					{
						flag = true;
						s[i]--;
						s[i+1] = '9';
					}
					else
					{
						s[i+1] = '9';
					}
				}
			}
			
		}
		for (int i = 0; i < (int)s.size(); i++)
		{
			if (s[i] == '0')
				s.erase(s.begin() + i, s.begin() + i + 1);
			else
				break;
		}
		cout << "Case #" << cse++ << ": " << s << endl;
	}
	return 0;
}