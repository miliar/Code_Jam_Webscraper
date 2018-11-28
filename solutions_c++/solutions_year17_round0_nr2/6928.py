#include <bits/stdc++.h>

#define INF 0x3F3F3F3F
#define rep(i, a, b) for(int i = int(a); i < int(b); i++)
#define pb push_back
#define debug(x) cout << #x << " = " << x << endl;
#define debug2(x,y) cout << #x << " = " << x << " --- " << #y << " = " << y << "\n";
#define debugM( x, l, c ) { rep( i, 0, l ){ rep( j, 0, c ) cout << x[i][j] << " "; printf("\n");}}
#define all(S) (S).begin(), (S).end()
#define F first
#define S second
#define mk make_pair

using namespace std;

typedef pair <int, int> ii;
typedef long long int ll;

string ans, aux;

void best( string& a, string& s ){
	if( a == "" ) a = s;
	else if( a.size() < s.size() ) a = s;
	else if( a.size() == s.size() && a < s ) a = s;
}

bool cmp( string& a, string& b ){
	if( a.size() != b.size() ) return a.size() < b.size();
	return a <= b;
}

void back( string s, char last ){
	if( !cmp( s, aux ) ) return;
	best( ans, s );
	for( char c = last; c <= '9'; c++ ){
		back( s+c, c );
	}
}

int main(){
	int t, test = 1;
	freopen("B-small-attempt0.in", "r", stdin );
	freopen("B-small-attempt0.sol", "w", stdout );

	scanf("%d", &t );
	while( t-- ){
		cin >> aux;
		ans = "";
		back( "", '1' );
		printf("Case #%d: %s\n", test++, ans.c_str() );
	}
}

