/*ckpeteryu Code Jam 2017 Round1C - Problem A */
#include<iostream>
#include<iomanip>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<climits>
#include<cmath>
#include<bitset>
#include<string>
#include<ctime>
#include<typeinfo>
#include<functional>
#include<map>
#include<set>
#include<vector>
#include<stack>
#include<queue>
//#include<regex>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define FOD(i,s,e) for(int i=(s);i>=(int)(e);i--)
#define FORVEC(i,a) for(int i=0;i<(int)((a).size());i++)
#define pb push_back
#define mp make_pair
#define CLR(s,x) memset(s,x,sizeof(s))
#define LL long long int

int nt;

bool comp(pair<LL,LL>& p1, pair<LL,LL> &p2){
	if(p1.first==p2.first){
		return p1.second>p2.second;
	}else{
		return p1.first>p2.first;
	}
}

LL solve(vector< pair<LL,LL> >&vp, int from, int to, int num){
	int nr=to-from+1;
	int nc=num;
	LL dp[nr][nc];
	FOR(i,0,nr){
		fill(dp[i],dp[i]+nc,0);
	}
	FOR(j,0,nc){
		dp[0][j]=2*vp[from].first*vp[from].second;
	}
	
	FOR(i,1,nr){		
		dp[i][0]=2*vp[from+i].first*vp[from+i].second;
		if(dp[i-1][0]>dp[i][0]){
			dp[i][0]=dp[i-1][0];
		}		
	}
		
	/*FOR(i,0,nr){
		FOR(j,0,nc){
			cout<<dp[i][j]<<" ";
		}puts("");
	}	
	puts("");*/
	
	FOR(i,1,nr){
		FOR(j,1,nc){
			dp[i][j]=2*vp[from+i].first*vp[from+i].second+dp[i-1][j-1];
			if(dp[i-1][j]>dp[i][j]){
				dp[i][j]=dp[i-1][j];
			}
		}
	}	
	return dp[nr-1][nc-1];
}

int main(int argc, char **argv){
	//ios_base::sync_with_stdio(false);
	//const clock_t begin_time = clock();
	scanf("%d",&nt);
	FOE(k,1,nt){
		int N,K;
		LL r,h;
		vector< pair<LL,LL> > vp;
		scanf("%d%d",&N,&K);		
		FOR(i,0,N){
			scanf("%lld%lld",&r,&h);
			vp.pb(mp(r,h));			
		}		
		sort(vp.begin(),vp.end(),comp);
		int sz=vp.size();
		LL ret=0;
		FOR(i,0,sz-K+1){			
			LL temp=vp[i].first*vp[i].first+2*vp[i].first*vp[i].second;			
			if(K>1)
				temp+=solve(vp,i+1,sz-1,K-1);
			if(temp>ret){
				ret=temp;
			}
		}
		printf("Case #%d: %.9f\n",k,M_PI*ret);
	}
	//std::cout <<endl<< float( clock () - begin_time ) /  CLOCKS_PER_SEC;
	return 0;
}