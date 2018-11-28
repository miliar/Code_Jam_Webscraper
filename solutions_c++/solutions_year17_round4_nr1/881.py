//#include<stdio.h>
//#include<stdlib.h>
#include<bits/stdc++.h>
//#define Min(a,b,c) min((a),min((b),(c)))
#define mp(a,b) make_pair((a),(b))
#define pii pair<int,int>
#define pdd pair<double,double>
#define pll pair<LL,LL>
#define pb(x) push_back(x)
#define x first
#define y second
#define sqr(x) ((x)*(x))
#define EPS 1e-11
#define MEM(x) memset(x,0,sizeof(x))
#define N 100005
#define pi 3.14159265359
using namespace std;
typedef long long LL;
int solve(){
	
}
int main() {
	int t;
	scanf("%d",&t);
	for(int T=1;T<=t;T++){
		int n,p;
		scanf("%d %d",&n,&p);
		int g[105];
		for(int i=0;i<n;i++)
		scanf("%d",&g[i]);
		int sub[4];
		MEM(sub);
		for(int i=0;i<n;i++)
		sub[g[i]%p]++;
		int ans=0;
		ans+=sub[0];
		if(p==2)
		ans+=sub[1]/2+(sub[1]%2==1);
		else if(p==3){
			ans+=min(sub[1],sub[2]);
			int kk=sub[1]-sub[2];
			if(kk<0)
			kk=-kk;
			ans+=kk/3+(kk%3!=0); 
		}
		else if(p==4){
			ans+=sub[2]/2;
			sub[2]%=2;
			ans+=min(sub[1],sub[3]);
			int kk=sub[3]-sub[1];
			if(kk<0)
			kk=-kk;
			if(sub[2]==1&&kk>=2){
				ans++;
				sub[2]=0;
				kk-=2;
			}
			ans=ans+kk/4;
			kk%=4;
			if(kk!=0||sub[2]!=0)
			ans++;
		}
		printf("Case #%d: %d\n",T,ans);
	}
} 
//1 1 2 6 3 8 4 11 5 17 6 15 7 13 8 25 9 22 10 27
//1
//2 4 6 8 10
//3 6 9
//4 2 6 8 10
//5 5 10
//6 2 3 4 6 8 10
