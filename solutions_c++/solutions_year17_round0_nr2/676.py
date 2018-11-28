#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define sz(a) ((int)(a).size())
#define rep(i, a, b) for(int (i) = (a); (i) < (b); (i)++)
#define dec(i, a, b) for (int (i) = (a); (i) >= (b); (i)--)
#define clr(a,v) memset(a, v, sizeof(a))
#define all(a) (a).begin(),(a).end()
#define MAXN 101010
#define LOGN 20
#define EPS 1e-10
#define fcin ios_base::sync_with_stdio(false)
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

int t;
char s[MAXN], ans[MAXN];

int main(){
	scanf("%d", &t);
	rep(caso,1,t+1){
		scanf("%s", s+1);
		int n = strlen(s+1)+1, ja=0;
		ans[0] = '0';
		rep(i,1,n){
			if(ja) ans[i] = '9';
			else{
				if(s[i] < ans[i-1]){
					ja=1;
					ans[i-1]--;
					ans[i] = '9';
					dec(j,i-1,1)
						if(ans[j-1] > ans[j]) ans[j-1]--, ans[j] = '9';
				}else ans[i] = s[i];
			}
		}
		printf("Case #%d: ", caso);
		rep(i,0,n) if(ans[i] > '0') printf("%c", ans[i]);
		printf("\n");
	}
}

