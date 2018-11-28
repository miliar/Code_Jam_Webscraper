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
typedef double db;
typedef pair<int,int> PII;
typedef pair<db,int> PDI;

const char col[]=" RYOBVG";
int n;
int a[10],_a[10];
string _ans[10],ans[10],res;
bool onecol(int i){
	REP(j,1,7)if(j!=i&&j!=(i^7)&&a[j]>0)return 0;
	return 1;
}
bool check(){
	if(res.size()!=n)return 0;
	if(res[0]==res[n-1])return 0;
	return 1;
}
void solve(){
	scanf("%d%d%d%d%d%d%d",&n,a+1,a+3,a+2,a+6,a+4,a+5);
	REP(_,0,3){int i=1<<_;
		ans[i]="";
		a[i]-=a[i^7];
		if(!(a[i^7]==0||a[i]>0||(a[i]==0&&onecol(i)))){puts("IMPOSSIBLE");return;}
		while(a[i^7]--)ans[i]+=col[i],ans[i]+=col[i^7];
		if(a[i]==0&&onecol(i)){puts(ans[i].c_str());return;}
		ans[i]+=col[i];
		if(a[i]==1&&onecol(i)){puts(ans[i].c_str());return;}
	}
	REP(j,1,7)_ans[j]=ans[j],_a[j]=a[j];
	REP(i,0,3){
		int mxi=1<<i,mxj;
		REP(j,1,7)ans[j]=_ans[j],a[j]=_a[j];
		res="";
		for(;mxi!=-1;){
			mxj=-1;
			REP(j,0,3)if((1<<j)!=mxi&&a[1<<j]>a[mxj])mxj=1<<j;
			if(a[mxi]==0)break;
			--a[mxi];res+=ans[mxi];ans[mxi]=col[mxi];
			mxi=mxj;
		}
		if(check()){puts(res.c_str());return;} 
	}
	puts("IMPOSSIBLE");
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

