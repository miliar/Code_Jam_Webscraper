#include<bits/stdc++.h>
using namespace std;
int main(){
  int test;
  scanf("%d",&test);
  for(int t = 1; t <= test; t ++ ){
	long long n;
	scanf("%lld", &n);
	vector<int> v;
	while(n){
	  v.push_back(n % 10);
	  n /= 10;
	}
	reverse(v.begin(),v.end());
	for(int i = 0; i + 1 < v.size(); i ++ ){
	  if ( v[i] > v[i + 1] ){
		for(int j = i + 1; j < v.size(); j ++ ) v[j] = 9;
		int next = i + 1;
		for(int j = i - 1; j >= 0; j -- ){
		  if ( v[j] == v[i] ) {
			v[j] --;
			next = j + 1;
		  }
		  else break;
		}
		v[i]--;
		for ( int j = next; j <= i; j ++ ) v[j] = 9;
		break;
	  }
	}
	printf("Case #%d: ", t);
	bool ok = 0;
	for(int i = 0; i < v.size(); i ++ ) {
	  if ( v[i] != 0 ) ok = 1; 
	  if ( ok ) printf("%d", v[i]);
	}
	puts("");
  }
}