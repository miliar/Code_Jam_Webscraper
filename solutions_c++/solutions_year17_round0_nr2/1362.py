/*
 * b.cpp
 *
 *  Created on: 2017/04/08
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

int main(void){
	          int i,j;

	      	  int T;
	      	  cin >> T;
	      	  REP(tc,T){

	      		  string x;
	      		  cin >> x;
	      		  int n=x.size();

	      		  while(1){

	      			  bool f=true;
	      			  for(i=0;i<n-1;i++){
	      				  if(x[i+1]>=x[i]) continue;
	      				  f=false;
	      				  int p=x[i]-'0'-1;
	      				  x[i]=(char)('0'+p);
	      				  for(j=i+1;j<n;j++) x[j]='9';
	      			  }
	      			  if(f) break;
	      		  }

	      	       cout << "Case #" << tc+1 << ": ";
	      	       for(i=0;i<n;i++){
	      	    	   if(x[i]=='0') continue;
	      	    	   cout << x[i];
	      	       }
	      	       cout << endl;

	      	  }

	          return 0;
}



