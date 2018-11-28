#include <bits/stdc++.h>
#define loop(i,a,b) for(int i=a; i<b; i++)
#define rev(i,a,b) for(int i=a; i>=b; i--)
#define iter(x,a,type) for(type::iterator x=a.begin(); x!=a.end(); ++x)
#define setmem(m,x) memset(m,x,sizeof(m))
#define len(a) ((int) a.size())
#define append(x) push_back(x)
#define x first
#define y second

using namespace std;
typedef long long large;
typedef pair<int,int> ii;
typedef vector<int> vi;

int main(){
	freopen("A.txt","r",stdin);
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int ntc;
	double d, n, ans, a, b;
	scanf("%d", &ntc);
	loop(tc,1,ntc+1){
		scanf("%lf %lf",&d, &n);
		ans = 1e30;
		loop(i,0,n){
			scanf("%lf %lf",&a, &b);
			ans = min(ans, b*d/(d-a));
		}
		printf("Case #%d: %lf\n",tc, ans);
	}
	return 0;
}
