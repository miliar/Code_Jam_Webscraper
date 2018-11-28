#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long ll;
#define INF 2000000000
#define MOD 1000000007
#define endl '\n'

bool comp(pair<int,int> x,pair<int,int> y){
	return (x.second-x.first)>(y.second-y.first);
}

int main(){
	ios::sync_with_stdio(false);
	int t,tc,n,k,i,j,start,end,l,r,mid;
	vector<pair<int,int> > q;
	cin >> t;
	tc = t;
	while(tc--){
		cout << "Case #" << t-tc << ": ";
		cin >> n >> k;
		q.clear();
		q.push_back(make_pair(0,n-1));
		start = 0;
		end = n-1;
		for(i=0;i<k;++i){
			start = q.front().first;
			end = q.front().second;
			q.erase(q.begin());
			mid = start+(end-start)/2;
			l = mid-1;
			r = mid+1;
			if(l-start >= end-r){
				if(start <= l)
				q.push_back(make_pair(start,l));
				if(end >= r)
				q.push_back(make_pair(r,end));
			}else{
				if(end >= r)
				q.push_back(make_pair(r,end));
				if(start <= l)
				q.push_back(make_pair(start,l));
			}
			sort(q.begin(),q.end(),comp);
			l = mid-start;
			r = end-mid;
			//cout << start << end << l << r << endl;
		}
		cout << max(l,r) << " " << min(l,r) << endl;
	}
	return 0;
}

