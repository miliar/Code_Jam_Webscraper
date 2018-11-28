#include<bits/stdc++.h>
using namespace std;
string s;
long long memo[ 21 ][ 10 ][ 2 ];
int n;
long long dp( int pos , int ult , int menor ){
	if ( pos == n ) return 1;
	if ( memo[ pos ][ ult ][ menor ] != -1 ) return memo[ pos ][ ult ][ menor ];
	long long &ans = memo[ pos ][ ult ][ menor ] = 0;
	if ( menor ){
		for ( int i= 0 ; i < 10 ; i++ ){
			if ( ult <= i ){
				ans += dp( pos + 1 , i , 1 );
			}
		}
	}else{
		for ( int i = 0 ; i <= s[ pos ]-'0'; i++ ){
			if ( ult <= i ){
				ans += dp( pos + 1 , i , i < s[ pos ] -'0' );
			}
		}
	}
	return ans;
}
vector< char > v;
void rec( int pos , int ult , int menor ){
	if ( pos == n ) return;
	if ( menor ){
		for ( int i= 9 ; i >= 0 ; i-- ){
			if ( ult <= i ){
				if ( dp( pos + 1 , i , 1 ) ){ 
					v.push_back( '0'+i );
					rec( pos + 1 , i , 1 );
					return;
				}
			}
		}
	}else{
		for ( int i = s[ pos ]-'0'; i >= 0 ; i-- ){
			if ( ult <= i ){
				if ( dp( pos + 1, i , i < s[ pos ] - '0' ) ){ 
					v.push_back( '0'+i);
					rec( pos + 1,  i , i < s[ pos ] - '0' );
					return ;
				}
			}
		}
	}
}
int main(){
	int cases;
	cin>>cases;
	for ( int tt = 0 ; tt < cases ; tt++ ){
		cin>>s;
		memset( memo , -1, sizeof( memo ) );
		n = (int)s.size();
		v.clear();
		rec( 0 , 0 , 0 );
		
		int pos = 0;
		for ( int i = 0 ; i < (int)v.size(); i++ ){
			if ( v[ i ] != '0' ){
				pos = i;
				break;	
			}	
		}
		printf("Case #%d: ",tt+1);
		for ( int i = pos; i < (int)v.size(); i++ ){
			cout<<v[i];
		}
		cout<<'\n';
	}
}
