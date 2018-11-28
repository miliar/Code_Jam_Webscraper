#include<bits/stdc++.h>
using namespace std;

#define scl(x) scanf("%lld",&x)
#define sc(x)  scanf("%d",&x)
#define ll long long
#define lop(i,n) for(int i=0;i<n;++i)
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;

double EPS = 1e-9;
ii arr[55][55];
int n,p;
int r[55];
int t;
int ptr[55];

int main(){
#ifndef ONLINE_JUDGE
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
#endif
	sc(t);
	lop(C,t){
		sc(n),sc(p);
		lop(i,n)sc(r[i]);
		lop(i,n)lop(j,p){
			int v;
			sc(v);
			double cnt=1.0*v/r[i];
			double s=cnt/1.1;
			double e=cnt/0.9;
			s=ceil(s);
			arr[i][j]=ii(s+EPS,e+EPS);
		}
		lop(i,n)sort(arr[i],arr[i]+p);
		int out=0,d=0;
		memset(ptr,0,sizeof ptr);
		for(int sz=1;!d;sz++){
			bool ok=1;
			lop(i,n){
				ii v=arr[i][ptr[i]];
				while(ptr[i]<p&&v.second<sz){
					ptr[i]++;
					v=arr[i][ptr[i]];
				}
				if(ptr[i]>=p){
					d=1,ok=0;
					break;
				}
				else if(v.first>sz){
					ok=0;
					break;
				}
			}
			if(ok){
				out++;
				lop(i,n){
					++ptr[i];
					if(ptr[i]>=p)d=1;
				}
				sz--;
			}
		}
		printf("Case #%d: %d\n",C+1,out);
	}

}
