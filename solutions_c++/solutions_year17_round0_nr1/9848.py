

#include<bits/stdc++.h>
using namespace std;


typedef long long ll;

bool check(ll n){

	int t1,t2;

	t1=n%10;

	n/=10;

	while(n>0){

		t2=n%10;

		if(t2>t1) return 0;

		t1=t2;

		n/=10;

	}



return 1;

}




void syncOff(){ ios_base::sync_with_stdio(0); cin.tie(NULL); }


int main(){

  syncOff();

  ll t,i,j,k;

  cin>>t;
 
  for(i=t;i>0;--i){

  if(check(i)) {cout<<i<<"\n";break;}


  }
  

  return 0;

}







