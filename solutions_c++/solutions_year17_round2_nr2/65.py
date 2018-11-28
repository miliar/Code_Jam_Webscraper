#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define ii pair<int,int>
#define INF 2000000000.0
#define M 1000000007ll
#define INFLL 1000000000000000010ll
#define UQ(x) (x).resize(distance((x).begin(),unique(all((x)))))
#define mid(x,y) (((x)+(y))>>1)
int tc;
int n,r,o,y,g,b,v;
char s[20005];
bool test(int r,int y,int b) {
	memset(s,0,sizeof(s));
	int m=r+y+b;
	if (r>y+b) return 0;
	if (y>r+b) return 0;
	if (b>r+y) return 0;
	vector<pair<int,char> > v;
	v.pb(mp(r,'R'));
	v.pb(mp(y,'Y'));
	v.pb(mp(b,'B'));
	sort(all(v));
	int x=v.back().first;
	char c=v.back().second;
	for (int i=0;i<x;i++) {
		s[i*2]=c;
	}
	v.pop_back();
	int d=v[1].first-v[0].first;
	for (int i=0;i<d;i++) {
		s[i*2+1]=v[1].second;
	}
	int w=0;
	for (int i=0;i<m;i++) {
		if (s[i]==0) {
			s[i]=v[w].second;
			w=!w;
		}
	}
	int cr=0,cb=0,cy=0;
	for (int i=0;i<m;i++) {
		if (s[i]=='R') cr++;
		if (s[i]=='B') cb++;
		if (s[i]=='Y') cy++;
		assert(s[i]!=0);
		if (i) assert(s[i]!=s[i-1]);
	}
	assert(s[0]!=s[m-1]);
	assert(cr==r);
	assert(cy==y);
	assert(cb==b);
	return 1;
	/*
	if (r>=y && r>=b) s[0]='R',r--;
	else if (y>=r && y>=b) s[0]='Y',y--;
	else s[0]='B',b--;
	for (int i=1;i<n;i++) {
		if (s[i-1]=='R') s[i]=((b>y)?'B':'Y');
		else if (s[i-1]=='Y') s[i]=((b>r)?'B':'R');
		else if (s[i-1]=='B') s[i]=((r>y)?'R':'Y');
		if (s[i]=='R') r--;
		else if (s[i]=='B') b--;
		else y--;
	}
	assert(s[m-1]!=s[0]);
	return 1;
	*/
}
int main() {
	scanf("%d",&tc);
	for (int kk=1;kk<=tc;kk++) {
		scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
		if (n==1) {
			printf("Case #%d: ",kk);
			if (r) printf("R");
			else if (o) printf("O");
			else if (y) printf("Y");
			else if (g) printf("G");
			else if (b) printf("B");
			else if (v) printf("V");
			printf("\n");
			continue;
		}
		bool can=1;
		if (b<o) can=0;
		else if (b==o && o>0) {
			if (b+o==n) {
				printf("Case #%d: ",kk);
				for (int i=0;i<n/2;i++) printf("BO");
				printf("\n");
				continue;
			} else can=0;
		} else b-=o;

		if (r<g) can=0;
		else if (r==g && g>0) {
			if (r+g==n) {
				printf("Case #%d: ",kk);
				for (int i=0;i<n/2;i++) printf("RG");
				printf("\n");
				continue;
			} else can=0;
		} else r-=g;

		if (y<v) can=0;
		else if (y==v && v>0) {
			if (y+v==n) {
				printf("Case #%d: ",kk);
				for (int i=0;i<n/2;i++) printf("YV");
				printf("\n");
				continue;
			} else can=0;
		} else y-=v;

		if (!can) {
			printf("Case #%d: IMPOSSIBLE\n",kk);
			continue;
		}
		
		if (!test(r,y,b)) {
			printf("Case #%d: IMPOSSIBLE\n",kk);
			continue;
		}
		printf("Case #%d: ",kk);
		bool br=0,by=0,bb=0;
		for (int i=0;i<r+y+b;i++) {
			printf("%c", s[i]);
			if (s[i]=='R' && !br) {
				br=1;
				for (int j=0;j<g;j++) printf("GR");
			}
			if (s[i]=='Y' && !by) {
				by=1;
				for (int j=0;j<v;j++) printf("VY");
			}
			if (s[i]=='B' && !bb) {
				bb=1;
				for (int j=0;j<o;j++) printf("OB");
			}
		}
		printf("\n");
	}
}