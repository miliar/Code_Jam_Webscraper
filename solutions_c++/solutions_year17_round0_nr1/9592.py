#include <bits/stdc++.h>
#define FOR(i,n) for(size_t i=0;i<n;++i)
#define FOR1(i,n) for(size_t i=1;i<=n;++i)
#define endl '\n'
#define ll int64_t
#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()
using namespace std;

ll gcd(ll a , ll b){return a==0?b:gcd(b%a,a);}


int flips(int a[], int M, int N) {
  int s[M]; FOR(i,M) s[i] = 0;
  int sum=0, ans=0;
  FOR(i,M) {
    s[i] = (a[i]+sum)%2 != 1;
    sum += s[i] - (i>=N-1?s[i-N+1]:0);
    ans += s[i];
    if(i>M-N and s[i]!=0) return -10;
  }
  return ans;
}

int main(){
	#ifndef ONLINE_JUDGE	
    freopen("input.txt", "r", stdin);	
    freopen("output.txt", "w", stdout);
	#endif
	int i,j;
	ios::sync_with_stdio(false);	
	cin.tie(NULL);
	int t,len,k,a[1005];
	char s[1005];
	cin>>t;
	FOR1(j,t){
		cin>>s>>k;
		int M = strlen(s);
		FOR(i,M)
			s[i]=='-'?a[i]=0:a[i]=1;
		int ans = flips(a,M,k);
		if(ans==-10) cout<<"Case #"<<j<<": IMPOSSIBLE\n";
		else cout<<"Case #"<<j<<": "<<ans<<"\n";
	}	
	return 0;
}