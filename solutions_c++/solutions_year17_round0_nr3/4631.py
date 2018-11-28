#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>

#define yeral() (node *)calloc( 1 , sizeof(node) )
#define fi first
#define se second
#define o ((b+e)/2)

using namespace std;

const int MOD=1e9+7;

long long int N,K;

set <long long int > S;
set <long long int > :: iterator it;
map <long long int,long long int> mp;

int main(){
	
	int T;
	cin >> T;

	for( int mask=1 ; mask<=T ; mask++ ){
		S.clear();
		mp.clear();
		cin >> N >> K;
		S.insert( -N );
		mp[N]=1;
		while( K ){
			it=S.begin();
			long long int cur=-(*it);
			S.erase( it );
			if( mp[cur] >= K ){
				printf("Case #%d: %d %d\n",mask,cur/2,cur-1LL-cur/2);
				break;
			}
			K-=mp[cur];
			mp[cur/2]+=mp[cur];
			mp[cur-1LL-cur/2]+=mp[cur];
			S.insert( -(cur/2) );
			S.insert( -(cur-1LL-cur/2) );
		}
	}

	return 0;
}