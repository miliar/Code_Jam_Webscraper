/*
 *	
 *	Created by Ziyi Tang
 *
 */

//#include <bits/stdc++.h>
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <list>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pi;
typedef vector<pi> vpi;
typedef vector<vpi> vvpi;
const int INF = 0x3f3f3f;
const ll INFL = (ll)1E18;
const int dir[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};
#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))
#define MAXN 110
#define MOD 1000000007

vvpi all;
vpi hor;
map<vi, double> mm;
priority_queue<pair<double, vi> > pq; //min-time, <idx, horse#, rem-dis>

double dij(int s, int t){
	double re = 1e18;
	while(!pq.empty()) pq.pop();
	mm.clear();
	vi tmp;
	tmp.push_back(s);
	tmp.push_back(-1);
	tmp.push_back(hor[s].first);
	pq.push(make_pair(0.0, tmp));
	mm[tmp] = 0.0;
	while(!pq.empty()){
		pair<double, vi> now = pq.top();pq.pop();
		double nowtime = now.first;
		if(nowtime > mm[now.second]) continue;
		int idx = (now.second)[0];
		if(idx == t) re = min(re, nowtime);
		int horse = (now.second)[1];
		int rem = (now.second)[2];
		int tsz = all[idx].size();
		//cout << idx << " " << horse << " "  << rem << " " << nowtime << endl;
		REP(i,0,tsz){
			int nxtidx = all[idx][i].first;
			int dis = all[idx][i].second;
			// Still the current house
			if(horse != -1 && rem >= dis){
				double nxttime = nowtime + (double)dis/hor[horse].second;
				tmp.clear();
				tmp.push_back(nxtidx);
				tmp.push_back(horse);
				tmp.push_back(rem-dis);
				if(mm.find(tmp) == mm.end() || mm[tmp] > nxttime){
					mm[tmp] = nxttime;
					pq.push(make_pair(nxttime,tmp));
				}
			}
			double nxttime = nowtime + (double)dis/hor[idx].second;
			tmp.clear();
			tmp.push_back(nxtidx);
			tmp.push_back(idx);
			tmp.push_back(hor[idx].first-dis);
			if(mm.find(tmp) == mm.end() || mm[tmp] > nxttime){
				mm[tmp] = nxttime;
				pq.push(make_pair(nxttime,tmp));
			}

		}
	}
	return re;
}
int main(){
	int T;
	cin >> T;
	REP(test,1,T+1){
		int n,q;
		cin >> n >> q;
		all.clear();
		hor.clear();
		all.assign(n, vpi(0, pi(0,0)));
		REP(i,0,n){
			int e,s; cin >> e >> s;
			hor.push_back(make_pair(e,s));
		}
		REP(i,0,n){
			REP(j,0,n){
				int tmp;
				cin >> tmp;
				if(tmp != -1){
					all[i].push_back(make_pair(j,tmp));
				}
			}
		}
		printf("Case #%d:", test);
		REP(i,0,q){
			int s,t;
			cin >> s >> t;
			s--;t--;
			double re = dij(s,t);
			printf(" %.7f", re);
		}
		printf("\n");
	}
	return 0;
}