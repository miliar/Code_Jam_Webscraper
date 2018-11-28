#include <bits/stdc++.h>
#define pb push_back
#define NMAX 60005
#define LMAX 1000005
#define ll unsigned long long
#define x first
#define y second
#define INF 0x3f3f3f3f
#define MOD 1000000007

using namespace std;

ifstream fin("fisier.in");
ofstream fout("fisier.out");

ll n,best;

void bkt(ll act) {
	if(act<=n && act>=best)
		best=act;
	if(act>=n) return;

	for(int i=max(act%10,1ULL);i<10;++i)
		bkt(act*10+i);
}

int main() {
	int t,x;

	fin>>t;
	x=t;
	while(t) {
		fin>>n;

		best=0;
		bkt(0);
		fout<<"Case #"<<x-t+1<<": "<<best<<'\n';
		--t;
	}

	return 0;
}
