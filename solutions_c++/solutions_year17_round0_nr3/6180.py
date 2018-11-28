#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<numeric>
#include<functional>
#include<algorithm>
#include<bitset>
#include<tuple>
#include<unordered_set>
#include<random>
#include<array>
#include<cassert>
using namespace std;
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define all(v) v.begin(),v.end()
#define uniq(v) v.erase(unique(all(v)),v.end())




int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin>>t;
	rep(i,t){
		int n,k,v;
		cin>>n>>k;
		priority_queue<int> pq;
		pq.push(v=n);
		rep(j,k-1){
			v = pq.top();
			pq.pop();
			pq.push((v-1)/2);
			pq.push((v-1+1)/2);
		}
		v=pq.top();
		cout << "Case #" << (i + 1) << ": " << (v)/2<<' '<<(v-1)/2 << endl;
	}

	return 0;
}