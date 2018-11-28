/*
 * c.cpp
 *
 *  Created on: 2017/04/05
 *      Author: DO
 */

#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<algorithm>
#include<functional>
#include<utility>
#include<bitset>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<cstdio>

using namespace std;

#define REP(i,n) for(int i=0;i<int(n);i++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
typedef long long ll;
typedef pair<int,int> P;

ll c[65],d[65];

int main(void){
	          int i;

	      	  int T;
	      	  cin >> T;
	      	  REP(tc,T){

	      		  ll N,K;
	      		  cin >> N >> K;

	      		  d[0]=1;
	      		  for(i=1;i<=60;i++) d[i]=2*d[i-1];
	      		  int p=1;
	      		  for(i=1;;i++){
	      			  c[i]=d[i]-1;
	      			  if(c[i]>=K){
	      				  p=i;
	      				  break;
	      			  }
	      		  }

	      		  p--;
	      		  ll a=N/d[p],b=a-1;
	      		  ll y=a*d[p]-N+c[p];
	      		  ll x=d[p]-y;
	      		  ll r=K-c[p];
	      		  ll mx,mn;
	      		  if(x>=r){
	      			  if(a%2==0){
	      				  mx=a/2;
	      				  mn=a/2-1;
	      			  }else{
	      				  mx=(a-1)/2;
	      				  mn=mx;
	      			  }
	      		  }else{
	      			  if(b%2==0){
	      				  mx=b/2;
	      				  mn=b/2-1;
	      			  }else{
	      				  mx=(b-1)/2;
	      				  mn=mx;
	      			  }
	      		  }

	      	  cout << "Case #" << tc+1 << ": ";
	      	  cout << mx << ' ' << mn << endl;


	      	}

	          return 0;
}



