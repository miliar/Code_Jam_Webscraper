#include<cstdio>
typedef long long ll;

ll u[20];

ll get_num(ll n,int k){
	for(int i=0;i<k;i++) n /= 10;
	return n % 10;
}

ll dfs(ll &n,int k,int m){
	if(k<0) return n;
	ll s = get_num(n,k);
	if(s<m) n = (n / u[k+1]) * u[k+1] - 1;
	else return dfs(n,k-1,s);
	return -1;
}

void solve(int testcase){
	ll n;
	scanf("%lld",&n);
	while(true){
		if(dfs(n,20,0)>=0) break;
	}
	printf("Case #%d: %lld\n",testcase,n);
}

int main(){
	int t;
	scanf("%d",&t);
	u[0] = 1;
	for(int i=1;i<19;i++) u[i] = u[i-1] * 10;
	for(int i=1;i<=t;i++) solve(i);
}
