#include <iostream>
#include <memory.h>
using namespace std;

int dp[105][105][105][5];
int n, p;

int solve( int r1, int r2, int r3, int curRem ){
	if( r1 == 0 && r2 == 0 && r3 == 0 )
		return 0;
	int& ref = dp[r1][r2][r3][curRem];
	if( ref != -1 )
		return ref;
	ref = 0;
	int pl = 0;
	if( curRem == 0 )
		pl++;
	if( r1 )
		ref = max( solve( r1 - 1, r2, r3, ( curRem + 1 ) % p ), ref );
	if( r2 )
		ref = max( solve( r1, r2 - 1, r3, ( curRem + 2 ) % p ), ref );
	if( r3 )
		ref = max( solve( r1, r2, r3 - 1, ( curRem + 3 ) % p ), ref );
	ref += pl;
	return ref;
	
}

int main()
{
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		cin >> n >> p;
		int arr[4] = {0};
		int res = 0;
		memset( dp, -1, sizeof dp );
		for( int i = 0; i < n; i++ ){
			int a;
			cin >> a;
			if( a % p == 0 )
				res++;
			else arr[a % p]++;
		}
		//cout << arr[1] << ' ' << arr[2] << ' ' << arr[3] << endl;
		res += solve( arr[1], arr[2], arr[3], 0 );
		cout << "Case #" << T << ": " << res << endl;
	}
	return 0;
}