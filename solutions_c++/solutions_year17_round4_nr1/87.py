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

int p,n;
int ds[10];

int main(void){
	int qn;
	scanf("%d",&qn);
	reg(qqq,1,qn){
		scanf("%d%d",&n,&p);
		memset(ds,0,sizeof(ds));
		rep(i,n){
			int a;
			scanf("%d",&a);
			ds[a%p]++;
		}
		int ans=-1;
		if(p==2){
			ans=ds[1]/2;
		}
		else if(p==3){
			int mi=min(ds[1],ds[2]),
				ma=max(ds[1],ds[2]);
			ans=mi+((ma-mi)/3)*2;
			ans += max(0,(ma-mi)%3-1);
		}
		else if(p==4){
			ans = ds[2]/2;
			int mi=min(ds[1],ds[3]),
				ma=max(ds[1],ds[3]);
			ans+=mi;
			ma-=mi;
			if(ds[2]%2){
				int x = min(2,ma);
				ans+=x; ma-=x;
			}
			
			ans += (ma/4)*3+max(0,ma%4-1);
		}
		printf("Case #%d: %d\n",qqq,n-ans);	
	}
	return 0;
}




