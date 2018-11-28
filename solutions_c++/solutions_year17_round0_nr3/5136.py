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
#include <queue>
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
	int N,K;
	cin >> N >> K;
	priority_queue<long long> slots;
	slots.push(N);
	int minS = N;
	int maxS = N;
	F1( k, K )
	{
		auto maxGlobal = slots.top();
		slots.pop();
		minS = (maxGlobal - 1) / 2;
		maxS = maxGlobal / 2;
		slots.push( maxGlobal / 2 );
		slots.push( (maxGlobal - 1) / 2 );
	}
	cout << maxS << ' ' << minS << endl;
}

int main(int argc, char * argv[] )
{
	//stdin = freopen("C.in", "r", stdin);
	stdin = freopen("C-small-2-attempt0.in", "r", stdin); stdout = freopen("C-small.out", "w", stdout);
	//stdin = freopen("C-large.in", "r", stdin); stdout = freopen("A-large.out", "w", stdout);
	long T;
	cin >> T;
	F1(t,T)
		solve(t);
	return 0;
}
