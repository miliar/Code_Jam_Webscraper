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

void solve(int t)
{
	cout << "Case #" << t << ": ";
	string s;
	cin >> s;
	int K;
	cin >> K;
	int f = 0;
	F0( i, s.size() - K + 1 )
	{
		if( s[i] == '-' )
		{
			f++;
			F0(j,K)
			{
				auto& c = s[i+j];
				c = ( c == '-' ? '+' : '-');
			}
		}
		//cerr << s << endl;
	}
	F0(j,K)
	{
		if( s[ s.size() - K + j ] == '-' )
		{
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << f << endl;
}

int main(int argc, char * argv[] )
{
	//stdin = freopen("A.in", "r", stdin);
	//stdin = freopen("A-small-attempt0.in", "r", stdin); stdout = freopen("A-small.out", "w", stdout);
	stdin = freopen("A-large.in", "r", stdin); stdout = freopen("A-large.out", "w", stdout);
	long T;
	cin >> T;
	F1(t,T)
		solve(t);
	return 0;
}
