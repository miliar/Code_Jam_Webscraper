#include <iostream>
#include <cstdio>

using namespace std;

typedef unsigned long long ull;

int T;
ull N, ans;

ull solve( ull N ){

	ull curN = N, ans = 0, curPow = 1;
	int curD, lastChange = -1, i = 0, lastD = 9;

	while( curN ){
		curD = curN % 10ULL;
		if( curD > lastD ){
			lastChange = i;
			curD--;
			ans = 0;
		}
		ans += curD * curPow;
		curPow *= 10ULL;
		lastD = curD;
		curN /= 10ULL;
		++i;
	}

	curPow = 1;
	while( lastChange > 0 ){
		ans += curPow * 9ULL;
		curPow *= 10ULL;
		--lastChange;
	}

	return ans;

}

int main(){
	
	ios_base::sync_with_stdio( 0 );
	cin.tie( 0 );
	freopen( "/home/vg/Programacion/input", "r", stdin );
	freopen( "/home/vg/Programacion/output", "w", stdout );

	cin >> T;

	for( int tc = 1; tc <= T; ++tc ){
		cin >> N;
		cout << "Case #" << tc << ": " << solve( N ) << "\n";
	}

	return 0;
}