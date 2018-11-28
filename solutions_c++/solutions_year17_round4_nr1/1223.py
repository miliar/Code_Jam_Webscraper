#include<cstdio>
#include<cstdlib>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<algorithm>
#include<iostream>
#include<cmath>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

int T,n,p;
int mod[5];
int dp[4][101][101][101][101];

int solve(int l,int z,int o,int t,int th){
   // cout << l << " " << z << " " << o << " " << t << endl;
    if(z == 0 && o == 0 && t == 0 && th == 0)
	return 0 ;

    if(dp[l][z][o][t][th] != -1)
	return dp[l][z][o][t][th];

    int res = 105;
    if(z)
	res = min(res,solve(l,z-1,o,t,th));
    if(o){
	int nl =(( l - 1) +p ) %p;
	res = min(res,solve(nl,z,o-1,t,th));
    }

    if(t){
	int nl = ((l - 2)+p) % p ;
	res = min(res,solve(nl,z,o,t-1,th));
    }

    if(th){
	int nl = ((l - 3)+p) % p ;
	res = min(res,solve(nl,z,o,t,th-1));
    }
    if(l)
	res++;

    return dp[l][z][o][t][th] = res; 
}

void read_input(){
    cin >> T ;
    for(int t = 0 ; t < T ; ++t){

	memset(mod,0,sizeof mod);
	memset(dp ,-1, sizeof dp);
	
	int g;
	cin >> n >> p; 
	for(int i = 0 ; i < n; ++i){
	    cin >> g;
	    mod[ g % p ] ++; 
	}

	cout << "Case #" << t+1 << ": " << n  - solve(0,mod[0],mod[1],mod[2],mod[3]) << endl;
    }
}

int main(){
    read_input();
    return 0;
}
