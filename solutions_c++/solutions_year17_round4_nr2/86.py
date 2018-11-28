#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>
#include<cmath>
#include<climits>
#include<string>
#include<set>
#include<map>
#include<iostream>
using namespace std;
#define rep(i,n) for(int i=0;i<((int)(n));i++)
#define reg(i,a,b) for(int i=((int)(a));i<=((int)(b));i++)
#define irep(i,n) for(int i=((int)(n))-1;i>=0;i--)
#define ireg(i,a,b) for(int i=((int)(b));i>=((int)(a));i--)
typedef long long int lli;
typedef pair<int,int> mp;
#define fir first
#define sec second
#define IINF INT_MAX
#define LINF LLONG_MAX
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#define pque(type) priority_queue<type,vector<type>,greater<type> >
#define memst(a,b) memset(a,b,sizeof(a))
#define iter(v,ite) for(auto ite=(v).begin();ite!=(v).end();ite++)
#define mimunum(v,x) distance((v).begin(),lower_bound((v).begin(),(v).end(),x))


int n,c,m;

int tn[1005];
int rop[1005];


int main(void){
	int qn;
	scanf("%d",&qn);
	reg(qqq,1,qn){
		scanf("%d%d%d",&n,&c,&m);
		memst(rop,0);
		memst(tn,0);
		rep(i,m){
			int a,b;
			scanf("%d%d",&a,&b); a--; b--;
			rop[a]++; tn[b]++;
		}
		int rn=0;
		rep(i,c)rn=max(rn,tn[i]);
		int r=0;
		rep(i,n){
			r+=rop[i];
			rn=max(rn,(r+i)/(i+1));
		}
		
		int hon=0;
		rep(i,n){
			hon+=max(0,rop[i]-rn);
		}
		printf("Case #%d: %d %d\n",qqq,rn,hon);	
	}
	return 0;
}




