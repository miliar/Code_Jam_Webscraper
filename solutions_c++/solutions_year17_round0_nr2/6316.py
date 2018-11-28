#include<bits/stdc++.h>

using namespace std;

int n;
string res ; 
bool ans = false ;
char a[22];

void recurse(int dig , int prevDig , string tempans ){
	if( dig == n ){
		ans = true;
		res = tempans;
	}
	if( a[dig] - '0' >= prevDig ){
		recurse(dig + 1,a[dig] - '0',tempans + a[dig]);
	}
	if( ans == false && int(a[dig] - '0') - 1 >= prevDig ){
		ans = true;
		tempans += char(a[dig] - 1);
		for( int i = dig + 1 ; i < n ; i++ ){ 
			tempans += '9';
		}
		res = tempans;
	}
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for( int t = 1 ; t <= T ; t++ ){
		ans = false;
		res = "";
		scanf("%s",a);
		n = strlen(a);
		recurse(0,0,"");
		stringstream ss(res);
		long long int final;
		ss >> final;
		printf("Case #%d: %lld\n",t,final);
		
	}
}