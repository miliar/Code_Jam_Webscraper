/*
 * b.cpp
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
typedef pair<int,string> P;

int main(void){
	            int i;

		      	int T;
		      	cin >> T;
		      	REP(tc,T){

		      		int n,r,o,y,g,b,v;
		      		cin >> n >> r >> o >> y >> g >> b >> v;

		      		b=b-2*o;
		      		r=r-2*g;
		      		y=y-2*v;

		      		cout << "Case #" << tc+1 << ": ";

		      		if(b<0 || r<0 || y<0){
		      			cout <<"IMPOSSIBLE" << endl;
		      			continue;
		      		}


		      		vector<string> bb;
		      		for(i=1;i<=o;i++) bb.push_back("BOB");
		      		for(i=1;i<=b;i++) bb.push_back("B");

		      		vector<string> rr;
		      		for(i=1;i<=g;i++) rr.push_back("RGR");
		      		for(i=1;i<=r;i++) rr.push_back("R");

		      		vector<string> yy;
		      		for(i=1;i<=v;i++) yy.push_back("YVY");
		      		for(i=1;i<=y;i++) yy.push_back("Y");

		      		int x=bb.size(),u=rr.size(),z=yy.size();
		      		vector<P> t;
		      		t.push_back(P(x,"B"));
		      		t.push_back(P(u,"R"));
		      		t.push_back(P(z,"Y"));
		      		sort(t.begin(),t.end());
		      		if(t[2].first>t[0].first+t[1].first){
		      			cout <<"IMPOSSIBLE" << endl;
		      			continue;
		      		}

		      		string ans;
		      		for(i=1;i<=t[0].first+t[1].first-t[2].first;i++){
		      			ans+=t[2].second;
		      			ans+=t[1].second;
		      			ans+=t[0].second;
		      		}

		      		for(i=t[0].first+t[1].first-t[2].first+1;i<=t[1].first;i++){
		      			ans+=t[2].second;
		      			ans+=t[1].second;
		      		}

		      		for(i=t[1].first+1;i<=t[2].first;i++){
		      			ans+=t[2].second;
		      			ans+=t[0].second;
		      		}

		      		cout << ans << endl;


		      	}


	          return 0;
}



