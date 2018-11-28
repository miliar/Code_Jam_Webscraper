#include <bits/stdc++.h>

using namespace std;

ifstream in("test.in");
ofstream out("test.out");

typedef long long I64;

int val[50];

void solve( I64 nr ) {
	memset( val, 0, sizeof(val) );
	if( nr < 10 ) {
		out << nr << '\n';
		return ;
	}

	vector<int> v, sol;
	while( nr ) {
		v.push_back( nr % 10 );
		nr /= 10;
	}
	int N = v.size();
	reverse( v.begin(), v.end() );
	int pos = N - 1;
	for( int i = 1;  i < (int)v.size();  ++i ) {
		if( v[i-1] > v[i] ) {
			pos = i - 1;
			break;
		}
	}
	if( pos < N - 1 ) {
		/// trebuie sa scad pos cu 1
		int val = v[pos];
		while( pos >= 0 && v[pos] == val ) {
			--v[pos];
			--pos;
		}
		++pos;  /// asta ar fi prefixul bun
		if( v[0] < 1 ) {
			for( int i = 1;  i < N;  ++i ) out << '9';
			out << '\n';
			return ;
		}
		for( int i = 0;  i <= pos;  ++i ) out << v[i];
		for( int i = pos+1;  i < N;  ++i )  out << '9';
		out << '\n';
	}
	else {
		for( auto x : v ) out << x;
		out << '\n';
	}
}

int main()
{
   	int T;
   	in >> T;
   	for( int t = 1;  t <= T;  ++t ) {
   		out << "Case #" << t << ": ";
   		I64 nr;
   		in >> nr;
   		solve(nr);
   	}
}
