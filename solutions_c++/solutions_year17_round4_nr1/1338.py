//Aleksander Łukasiewicz
#include<bits/stdc++.h>
using namespace std;

#define fru(j,n) for(int j=0; j<(n); ++j)
#define tr(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define ALL(G) (G).begin(),(G).end()

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int INF = 1000000009;

int n, p;
int cnt[5];

int Solve(){
	int ret = 0;
	for(int i=1; i<p; i++){
		while(cnt[i] && cnt[p-i]){
			if(i == p-i && cnt[i] <= 1) break;
			cnt[i]--;
			cnt[p-i]--;
			ret++;
		}
	}
	
	int sum = 0;
	int m = 0;
	for(int i=1; i<p; i++) m += cnt[i];
	while(m){
		if(sum == 0) ret++;
		int curr = -1;
		if(cnt[p-sum]){
			curr = p-sum;
		}
		else{
			for(int i=1; i<p; i++)
				if(cnt[i]){
					curr = i;
					break;
				}
		}
		cnt[curr]--;
		sum = (sum+curr)%p;
		m--;
	}
	
	return ret;
}

int main(){
	int t;
	scanf("%d", &t);
	for(int pp=1; pp<=t; pp++){
		scanf("%d %d", &n, &p);
		int ans = 0;
		for(int i=0; i<=p; i++) cnt[i] = 0;
		for(int i=0; i<n; i++){
			int a;
			scanf("%d", &a);
			ans += (a % p == 0);
			cnt[a%p]++;
		}
		printf("Case #%d: %d\n", pp, ans+Solve());
	}
    
    
return 0;
}