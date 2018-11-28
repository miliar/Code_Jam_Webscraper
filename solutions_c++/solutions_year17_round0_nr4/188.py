#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
const int N=1000;
int n, nd, vert[N], hor[N], dp[N], dm[N], buf1[N], buf2[N];
vector<vi> adj;
vi v, ma, mb;

char symbol(int val) {
	if(val==1) return '+';
	if(val==2) return 'x';
	return 'o';
}

int dfs(int i) {
	if(v[i]) return 0;
	v[i]=1;
	for(int j:adj[i]) if(mb[j]==-1 || dfs(mb[j])) {
		ma[i]=j;
		mb[j]=i;
		return 1;
	}
	return 0;
}


int main() {
	int ncase, icase, x, y, i, j, m, score;
	char ch;
	map<int, int> ib, bc;
	scanf("%d", &ncase);
	for(icase=1; icase<=ncase; icase++) {
		scanf("%d%d", &n, &m);
		nd=2*n-1;
		ib.clear();
		score=0;
		for(i=1; i<=n; i++) vert[i]=hor[i]=0;
		for(i=1; i<=nd; i++) dp[i]=dm[i]=0;
		for(i=0; i<m; i++) {
			scanf(" %c%d%d", &ch, &x, &y);
			score++;
			if(ch=='o') score++;
			if(ch!='+') {
				hor[x]=vert[y]=1;
				ib[N*x+y]|=2;
			}
			if(ch!='x') {
				dp[x+y-1]=dm[x-y+n]=1;
				ib[N*x+y]|=1;
			}
		}
		bc.clear();

		int n1=0, n2=0;
		for(i=1; i<=n; i++) {
			if(hor[i]==0) buf1[n1++]=i;
			if(vert[i]==0) buf2[n2++]=i;
		}
		for(i=0; i<n1; i++) {
			bc[N*buf1[i]+buf2[i]]|=2;
			score++;
		}

		n1=n2=0;
		adj.assign(nd+1, vi(0));
		for(i=1; i<=n; i++) for(j=1; j<=n; j++) {
			if(dp[i+j-1]==0 && dm[i-j+n]==0)
				adj[i+j-1].push_back(i-j+n);
		}
		ma.assign(nd+1, -1);
		mb.assign(nd+1, -1);
		for(i=1; i<=nd; i++) if(ma[i]==-1) {
			v.assign(nd+1, 0);
			dfs(i);
		}
		for(i=1; i<=nd; i++) if(ma[i]!=-1) {
			x=(i+ma[i]-n+1)/2;
			y=(i-ma[i]+n+1)/2;
			bc[N*x+y]|=1;
			score++;
		}

		printf("Case #%d: %d %d\n", icase, score, (int)bc.size());
		for(auto t:bc) {
			x=t.first/N;
			y=t.first%N;
			printf("%c %d %d\n", symbol(ib[t.first]|bc[t.first]), x, y);
		}
	}
	return 0;
}