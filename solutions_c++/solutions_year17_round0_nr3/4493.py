#include<bits/stdc++.h>
using namespace std;
int main(){
	int cases;
	cin>>cases;
	for ( int tt = 0 ; tt < cases ; tt++ ){
		long long n , k;
		cin>>n>>k;
		multiset< long long > v;
		v.insert( n );
		multiset< long long >:: iterator it;
		long long  ans1 = 0  , ans2 = 0 , num;
		for ( int i = 0 ; i < k ; i++ ){
			it = v.end();
			it--;
			num = (*it);
			v.erase( it );
			if ( i == k - 1 ){
				if ( num % 2 == 0 ){
					ans1 = num/2;
					ans2 = num/2 - 1;
				}else{
					ans1 = ans2 = num/2;
				}
			}
			if ( num % 2 == 0 ){
				if ( num/2 ) v.insert( num/2  );
				if( num /2 - 1 )v.insert( num/2 - 1 );
			}else{
				if ( num/2 ){ 
					v.insert( num/2 );
					v.insert( num/2 );
				}
			}	
		}
		printf("Case #%d: %lld %lld\n",tt+1,ans1 , ans2);
	}
}
