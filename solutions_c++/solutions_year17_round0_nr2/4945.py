#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <string>
#include <vector>
#include <array>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <deque>
#include <tuple>

#define F0(i,N) for(int i=0; i<N; ++i)
#define F1(i,N) for(int i=1; i<=N; ++i)

using namespace std;

template<class T> inline ostream& operator<<( ostream& os, const vector<T>& v )
{
	for( auto& e:v )
		os << ' ' << e;
	return os;
}

void decrement( string& s, size_t pos )
{
	if( s[pos] != '0' )
	{
		s[pos]--;
		return;	
	}
	s[pos] = '9';
	assert( pos > 0 );
	return decrement(s, pos - 1);
}

bool decrement2tidy( string& s )
{
	char prev = 0;
	F0(i, s.size())
	{
		if( s[i] < prev )
		{
			F0(j, s.size() - i )
			{
				s[i+j] = '0';
			}
			decrement(s,s.size() - 1);
			return false;
		}
		prev = s[i];
	}
	return true;
}

void solve(int t)
{
	cout << "Case #" << t << ": ";
	string s;
	cin >> s;
	assert( ! s.empty() );
	while( ! all_of( s.begin(), s.end(), [](char& c){ return c == '0';} ) )
	{
		if( decrement2tidy(s) )
		{
			cout << stoll(s) << endl;
			return;
		}
	}
}

int main(int argc, char * argv[] )
{
	//stdin = freopen("B.in", "r", stdin);
	//stdin = freopen("B-small-attempt0.in", "r", stdin); stdout = freopen("B-small.out", "w", stdout);
	stdin = freopen("B-large.in", "r", stdin); stdout = freopen("B-large.out", "w", stdout);
	long T;
	cin >> T;
	F1(t,T)
		solve(t);
	return 0;
}
