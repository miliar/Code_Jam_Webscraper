#include<bits/stdc++.h>
using namespace std;
#define REP(i,a,b)for(int i=(a),i##_end_=(b);i<i##_end_;++i)
#define PER(i,a,b)for(int i=(b)-1,i##_end_=(a);i>=i##_end_;--i)
#define pb push_back
#define fi first
#define se second
template<class T>inline bool umx(T& A,const T& B){return A<B?A=B,1:0;}
template<class T>inline bool umn(T& A,const T& B){return A>B?A=B,1:0;}
typedef long long LL;
typedef long double db;
typedef pair<int,int> PII;
typedef pair<db,int> PDI;

const db pi=acos(-1.);
const int maxn=1010;
int n,k;

struct node{
	int r,h;
	bool operator<(const node&b)const{return r>b.r;}
} a[maxn];
bool cmp(int i,int j){return (LL)a[i].h*a[i].r>(LL)a[j].h*a[j].r;}
int id[maxn];
void solve(){
	scanf("%d%d",&n,&k);
	REP(i,0,n)scanf("%d%d",&a[i].r,&a[i].h);
	sort(a,a+n);
	db res=0.;
	REP(i,0,n){
		int t=0;REP(j,i+1,n)id[t++]=j;
		if(t>=k-1){
			sort(id,id+t,cmp);
			db s=pi*a[i].r*a[i].r+2*pi*a[i].r*a[i].h;
			REP(j,0,min(t,k-1))s+=2*pi*a[id[j]].r*a[id[j]].h;
			umx(res,s);
		}
	}
	printf("%.9f\n",(double)res);
	
}
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int _,__=0;scanf("%d",&_);
	while(_--){
		printf("Case #%d: ",++__);
		solve();
	}
	return 0;
}

