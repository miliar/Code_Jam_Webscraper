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

string cake;

void Flip(int s, int k){
	for(int i=0; i<k; i++)
		cake[s+i] = (cake[s+i] == '+') ? '-' : '+';
}

bool Check(){
	return cake.find("-") == string::npos;
}

int main(){
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	for(int pp=1; pp<=t; pp++){
		int k;
		cin>>cake>>k;
		int n = cake.size();
		int ans = 0;
		for(int i=0; i<n-k+1; i++)
			if(cake[i] == '-'){
				Flip(i, k);
				ans++;
			}
			
		printf("Case #%d: ", pp);
		if(Check())
			printf("%d\n", ans);
		else
			puts("IMPOSSIBLE");
	}
    
    
return 0;
}