/*
 * a.cpp
 *
 *  Created on: 2017/04/16
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
typedef pair<ll,ll> P;

int main(void){
	        int i;

	      	int T;
	      	cin >> T;
	      	REP(tc,T){

	      		int N;
	      		ll D;
	      		cin >> D >> N;
	      		vector<P> v(N);
	      		for(i=1;i<=N;i++){
	      			int K,S;
	      			cin >> K >> S;
	      			v.push_back(P(K,S));
	      		}

	      		sort(v.begin(),v.end());
	      		reverse(v.begin(),v.end());

	      		double t=1.0*(D-v[0].first)/(1.0*v[0].second);
	      		for(i=1;i<N;i++){
	      			double u=1.0*(D-v[i].first)/(1.0*v[i].second);
	      			if(t<u) t=u;
	      		}

	      		double ans=1.0*D/t;


	      		cout << "Case #" << tc+1 << ": ";
	      		printf("%.12f\n",ans);


	      	}


	          return 0;
}



