#include <bits/stdc++.h>

using namespace std;

const int NMAX = 2000;

ifstream in("test.in");
ofstream out("test.out");

int v[NMAX+2];
string str;
int Ans = 0;

void init() {
	memset( v, 0, sizeof(v) );
	Ans = 0;
}

void solve() {
	int N, K;
	in >> str >> K;
	N = str.size();
	for( int i = 0;  i < N;  ++i ) {
		v[i+1] = (str[i] == '+');
	}
	for( int i = 1;  i <= N-K+1;  ++i ) {
		if( !v[i] ) {
			++Ans;
			for( int j = i;  j < i+K;  ++j ) {
				v[j] ^= 1;
			}
		}
	}
	bool ok = 1;
	for( int i = 1;  i <= N;  ++i ) if( !v[i] ) ok = 0;
	if( !ok ) out << "IMPOSSIBLE\n";
	else out << Ans << '\n';
}

int main()
{
	int T;
	in >> T;
	for( int t = 1;  t <= T;  ++t ) {
        out << "Case #" << t << ": ";
		init();
		solve();
	}
	return 0;
}
