#include<bits/stdc++.h>
using namespace std;
int main(){
  int test;
  scanf("%d",&test);
  for(int t = 1; t <= test; t ++ ){
	int n,k;
	scanf("%d %d", &n, &k);
	vector<pair<int,long long> > v;
	for(int i = 1; i <= n; i ++ ){
	  int r,h;
	  scanf("%d %d", &r, &h);
	  long long bok = 2LL * r * h; // razy pi !
	  v.push_back(make_pair(r, bok));
	}
	sort(v.begin(), v.end());
	priority_queue<long long> q;
	long long suma = 0;
	long long maxi = 0;
	for(int i = 0; i < n; i ++ ){
	  int r = v[i].first;
	  long long b = v[i].second;
	  if ( q.size() >= k ) {
		suma += q.top();
		q.pop();
	  }
	  suma += b;
	  q.push(-b);  
	  long long gora = 1LL * r * r; // razy pi!
	  long long boki = suma;
	  maxi = max ( maxi, gora + boki );
	}
	printf("Case #%d: %.7lf\n", t, maxi * M_PI );
  }
  return 0;
}