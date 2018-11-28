#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

void get(long x, long *a, long *b){
	*a = x/2;
	*b = x-*a-1;
	if(*a<*b) swap(*a, *b);
}

void ans(long n){
	long l, r;
	get(n, &l, &r);
	printf("%ld %ld\n", l, r);
}

void solve(){
	long n, m;
	scanf("%ld %ld", &n, &m);
	map<long, long, greater<long> > h;
	map<long, long, greater<long> >::iterator i;
	h[n] = 1;
	while(m>1){
		map<long, long, greater<long> > t;
		for(i=h.begin(); i!=h.end();i++){
			long l, r;
			long nn = i->first;
			long mm = i->second;
			
			if(m<=mm){
				ans(nn);
				return;
			}

			m-=mm;
			get(nn, &l, &r);
			if(l>0) {if(t[l]) t[l]+=mm; else t[l]=mm;}
			if(r>0) {if(t[r]) t[r]+=mm; else t[r]=mm;}
		}
		h = t;
	}
	ans(h.begin()->first);
}

int main(){
	int cs, lp;
	scanf("%d", &cs);
	for(int lp = 1; lp <=cs; lp++){
		printf("Case #%d: ", lp);
		solve();
	}
	return 0;
}
