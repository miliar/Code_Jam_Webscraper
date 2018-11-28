// Author: Xujie Si
// Email: six@gatech.edu
#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
using namespace std;

#define FOR(i,X) for(int i=0;i<(X);++i)
#define PB(X) push_back( (X) )

typedef long long LL;
typedef vector<int> VI;

priority_queue<int> maxQ; // largest on the top
priority_queue<int, VI, greater<int> > minQ; // smallest on the top

auto cmp1 = [](int& a, int& b) -> bool {return a>b;};
auto dbg = ostream_iterator<int>(cerr, ",");

const int N = 1100;
LL R[N], H[N];
LL d[N];
LL td[N];


void solve(){
	// exact implementation appears here

	int n, K;
	cin >> n >> K;

	for(int i=0;i<n;++i) {
		d[i] = 0;
		td[i] = 0;
		H[i] = R[i] = 0;
	}

	vector< pair<LL,LL> > v;
	for(int i=0;i<n;++i) {
		cin >> R[i] >> H[i];
		v.push_back( make_pair(R[i], H[i]) );
	}

	sort(v.begin(), v.end());

	for(int i=0;i<n;++i){
		d[i] = v[i].first * v[i].second;
		//cerr<<"d["<<i <<"]=" <<d[i] << endl;
	}

	LL res = 0;
	int j = n;
	while(j>= K){
		LL t_res = v[j-1].first * v[j-1].first;
		t_res += 2 * d[j-1];
		//t_res += 2* v[j-1].first * v[j-1].second;
		//std::cerr<< "1, j=" <<j<<" K="<<K << "  t_res=" << t_res << endl;
		for(int i=0;i<j-1; ++i) {
			td[i] = d[i];
			//std::cerr << "copy td[" << i << "]=" << td[i] << endl;
		}

		sort(td, td+(j-1));

		for(int i=1;i<K; ++i) {
			t_res += 2 * td[j-1-i];
			//std::cerr << "td[" << j-i << "]=" << td[j-i] << endl;
		}

		//std::cerr<< "2, j=" <<j<<" K="<<K << "  t_res=" << t_res << endl;

		if(res < t_res) {
			res = t_res;
		}
		--j;
	}
	//double res = v[n-1].first * v[n-1].first;
	//for(int i=1;i<=K; ++i) {
	//		res += 2.0 * (double) v[n-i].first * (double) v[n-i].second;
	//}

	double PI = acos(-1.0);
	printf("%.9f\n", (double)res * PI);
}


int main()
{
  int cs = 0, T;
  scanf("%d",&T);
  while(++cs <= T){
    printf("Case #%d: ", cs);
    solve();
  }
  return 0;
}
