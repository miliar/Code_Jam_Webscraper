#include<bits/stdc++.h>

#define s(a) scanf("%d",&a)
#define ss(a) scanf("%s",a)

#define MP           make_pair
#define PB           push_back
#define REP(i, n)    for(int i = 0; i < n; i++)
#define INC(i, a, b) for(int i = a; i <= b; i++)
#define DEC(i, a, b) for(int i = a; i >= b; i--)
#define CLEAR(a)     memset(a, 0, sizeof a)

using namespace std;

typedef long long          LL;
typedef unsigned long long ULL;
typedef vector<int>        VI;
typedef pair<int, int>     II;
typedef vector<II>         VII;

int solve(){
	char inp[2000];
	int msum[2000];
	ss(inp);
	int k;
	s(k);
	int csum = 0;
	int l = strlen(inp);
	CLEAR(msum);
	for(int i=0;i<l;i++){
		int prev = csum;
		if(i>=k)
			prev-=msum[i-k];
		if((prev%2==0 && inp[i]=='-')|| (prev%2==1 && inp[i]=='+')){
			if((i+k-1)<l)
				csum++;
			else return -1;
		}
		msum[i] = csum;
	}
	return csum;
}
int main()
{
      int t;
      s(t);
      REP(tt,t){
      	printf("Case #%d: ",tt+1);
      	int ans = solve();
      	if(ans==-1)
      		printf("IMPOSSIBLE\n");
      	else printf("%d\n",ans);
      }
      return 0;
}
