#include "bits/stdc++.h"
using namespace std;

# define s(n)                        scanf("%d",&n)
# define sc(n)                       scanf("%c",&n)
# define sl(n)                       scanf("%lld",&n)
# define sf(n)                       scanf("%lf",&n)
# define ss(n)                       scanf("%s",n)

#define R(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

# define INF                         (int)1e9
# define EPS                         1e-9
# define MOD 1000000007


typedef long long ll;

int main()
{
  int t;
  cin >> t;
  R(i,t){
  	int ans=0;
  	bool imp=false;
  	string s; int k;
  	cin >> s;s(k);
  	FORD(j,s.length()-1,0){
  		if(s[j]=='-'){
  			R(f,k){
  				if(j-f<0){
  					j=-5;
  					imp=true;
  					break;
  				}
  				if(s[j-f]=='-')
  					s[j-f]='+';
  				else
  					s[j-f]='-';
  			}
  			ans++;
  		}
  	}
  	if(imp)
  		printf("Case #%d: IMPOSSIBLE\n",i+1);
  	else
  		printf("Case #%d: %d\n",i+1,ans);
  }
	
	return 0;
}
	