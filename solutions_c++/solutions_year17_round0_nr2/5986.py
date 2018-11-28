#include <bits/stdc++.h>
using namespace std;

string s;
int dp[ 20 ][ 2 ][ 10 ], caso = 0;

int f( int pos, int flag, int last ){
	if( pos == s.size() ) return 1;
	int &ret = dp[ pos ][ flag ][ last ]; 
	if( ret != -1 ) return ret;
	ret = 0;
	if( flag == 0 ){
		int d = s[ pos ] - '0';
		for( int i = last; i <= d; ++i ) ret = ret or f( pos+1, ( i == d )? 0 : 1, i );
	}
	else{
		for( int i = last; i <= 9; ++i ) ret = ret or f( pos+1, 1, i );
	}
	return ret;
}

string rec( int pos, int flag, int last ){
	if( pos == s.size() ) return "";
	if( flag == 0 ){
		int d = s[ pos ] - '0';
		for( int i = d; i >= last; i-- ){
			int val = f( pos+1, ( i == d )? 0 : 1, i );
			if( val == 1 ){
				char c = i + '0';
				string dig = "";
				dig += c;
				return dig + rec( pos+1, ( i == d )? 0 : 1, i );
			}
		} 
	}
	else{
		for( int i = 9; i >= last; i-- ){
			int val = f( pos+1, 1, i );
			if( val == 1 ){
				char c = i + '0';
				string dig = "";
				dig += c;
				return dig + rec( pos+1, 1, i );
			}	
		}
	}
}

void doit(){	
	cin >> s;
	int sz = s.size();
	memset( dp, -1, sizeof( dp ) );
	int sol = f( 0, 0, 0 );
	string cad = rec( 0 , 0, 0);
	long long ans = 0;
	for( int i = 0; i < cad.size(); ++i ){
		ans = ans * 10 + (cad[ i ]-'0');
	}
	printf("Case #%d: %lld\n", ++caso, ans);
}

int main(){
	int tc;
	cin >> tc;
	while( tc -- ) doit();
	return 0;
}
