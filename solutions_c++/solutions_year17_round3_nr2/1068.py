#include <bits/stdc++.h>
#define LL long long
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
using namespace std;

typedef pair<LL,LL> ii;
int T;
int n,m,memo[10][10][1500][800][2][2];
ii c[1010],j[1010];

int solve(int x, int y, int ti, int used, int last, int first){
	if(ti==1440){
		if(first==last) return -1;
		return 0;
	}
	if(ti>c[x].sc && x<n) x++;
	if(ti>j[y].sc && y<m) y++;
	int ti2 = used;
	int ti1 = ti-ti2;
	if(memo[x][y][ti][used][last][fi]!=-1) return memo[x][y][ti][used][last][fi];
	int ret = 1e8;
	if(ti==0){
		if(ti2<720 && ti>=c[x].fi && ti<=c[x].sc) ret = min(ret, solve(x, y, ti+1, ti2+1, 1, 1)+1);
		else if(ti1<720 && ti>=j[y].fi && ti<=j[y].sc) ret = min(ret, solve(x, y, ti+1, ti2, 0, 0)+1);
		else{
			if(ti2<720) ret = min(ret, solve(x, y, ti+1, ti2+1, 1, 1)+1);
			if(ti1<720) ret = min(ret, solve(x, y, ti+1, ti2, 0, 0)+1);
		}
	}
	else{
		if(x<n && ti>=c[x].fi && ti<=c[x].sc){
			if(ti2<720){
				if(last!=1) ret = min(ret, solve(x, y, ti+1, ti2+1, 1, first)+1);
				else ret = min(ret, solve(x, y, ti+1, ti2+1, 1, first));
			}
		}
		else if(y<m && ti>=j[y].fi && ti<=j[y].sc){
			if(ti1<720){
				if(last!=0) ret = min(ret, solve(x, y, ti+1, ti2, 0, first)+1);
				else ret = min(ret, solve(x, y, ti+1, ti2, 0, first));
			}
		}
		else{
			if(ti2<720){
				if(last!=1) ret = min(ret, solve(x, y, ti+1, ti2+1, 1, first)+1);
				else ret = min(ret, solve(x, y, ti+1, ti2+1, 1, first));
			}
			if(ti1<720){
				if(last!=0) ret = min(ret, solve(x, y, ti+1, ti2, 0, first)+1);
				else ret = min(ret, solve(x, y, ti+1, ti2, 0, first));
			}
		}
	}
//	cout<<c[x].fi<<" "<<c[x].sc<<endl;
//	cout<<x<<" "<<y<<" "<<ti<<" "<<ti1<<" "<<ti2<<" "<<last<<" "<<ret<<endl;
	return memo[x][y][ti][used][last][first] = ret;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	scanf("%d",&T);
	for(int tc=1;tc<=T;tc++){
		scanf("%d %d",&n,&m);
		int x,y;
		
		for(int i=0;i<n;i++){
			scanf("%d %d",&x,&y);
			c[i] = mp(x,y-1);
		}
		for(int i=0;i<m;i++){
			scanf("%d %d",&x,&y);
			j[i] = mp(x,y-1);
		}
		sort(c, c+n);
		sort(j, j+m);
		memset(memo,-1,sizeof(memo));
		int ans = solve(0, 0, 0, 0, 0, 0);
		
		
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}
