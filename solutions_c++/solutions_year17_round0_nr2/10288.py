#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#define pb push_back
using namespace std;

bool is(int x){
	if(x < 10) return true;
	if( (x %10) == 0){
		return false;
	}
	vector< int > v;
	while(x > 0){
		v.pb(x%10);
		x/=10;
	}
	reverse(v.begin(),v.end());
	for(int i = 1;i<v.size();i++){
		if( v[i] < v[i-1] )
		 	return false;
	}
	return true;
}

int solve(int x ){

	while( true ){

		if( is(x) )
			return x;
		x--;
	}

}

int main(){
	
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int x;
		scanf("%d",&x);

		printf("Case #%d: %d \n",t,solve( x));
	}

	return 0;
}