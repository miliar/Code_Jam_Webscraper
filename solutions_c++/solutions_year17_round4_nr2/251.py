#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cstring>
#include <set>
#include <utility>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <map>
#define ll long long
#define read(x) scanf("%d",&x);
#define readll(x) cin>>x;
#define FOR(x,a,b) for(int x=a;x<b;x++)
#define MP make_pair
#define PB push_back
#define pii pair<int,int>
#define readN(N,X) for(int i=0;i<N;i++) scanf("%d",&X[i]);
using namespace std;
int N, M, C;

int beli[1001];
int pesen[1004];
int sisa[1004];

void solve(){
	read(N);
	read(C);
	read(M);
	memset(beli, 0, sizeof (beli));
	memset(pesen, 0, sizeof (pesen));
	FOR(i,0,M){
		int a,b;
		read(a);
		read(b);
		a--; b--;
		pesen[a]++;
		beli[b]++;
	}
	int mx = 0;
	FOR(i,0,C) mx = max(mx, beli[i]);
	for (int i=mx;i<=1005;i++){
		//cout<<"coba "<<i<<endl;
		int dipindah = 0;
		int wow = 0;
		for (int j=0;j<N;j++){
			sisa[j] = i - pesen[j];
		}
		for (int j=N-1;j>=0;j--){
			if (sisa[j] < 0){ 
				dipindah -= sisa[j];
				wow -= sisa[j];
			}
			else if (sisa[j] > 0){
				dipindah -= sisa[j];
				if (dipindah < 0) dipindah = 0;
			}
		}
		if (dipindah) continue;
		cout<<i<<" "<<wow<<endl;
		return;
	}
}

int main(){
	int T;
	read(T);
	int cn = 1;
	while(T--){
		printf("Case #%d: ", cn++);
		solve();
	}
}
