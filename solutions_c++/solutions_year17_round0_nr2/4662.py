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

bool Check(int n){
	int prev = 9;
	while(n){
		if(n%10 > prev) return false;
		prev = n%10;
		n/=10;
	}
	
	return true;
}

int main(){
	//ios_base::sync_with_stdio(0);
	int t;
	scanf("%d", &t);
	for(int pp=1; pp<=t; pp++){
		int n;
		scanf("%d", &n);
		int ans;
		//printf("%d\n", n);
		for(ans = n; ans>=1; ans--){
			if(Check(ans)) break;
		}
			
		printf("Case #%d: %d\n", pp, ans);
	}
    
    
return 0;
}