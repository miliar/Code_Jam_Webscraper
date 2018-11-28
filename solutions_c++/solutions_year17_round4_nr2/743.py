#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<iomanip>
#include<vector>
#include<list>
#include<iterator>
#include<stack>
#include<queue>
using namespace std;

#include<fstream>
FILE *fin=freopen("a.in","r",stdin);
FILE *fout=freopen("a.out","w",stdout);

int T,t,n,c,q,i,j,k,a[3][1100],m[3],l[1100],s;
bool v[1100];
vector <int> g[12100];

bool dfs(int x) {
	if (v[x])
	return 0;
	v[x]=1;
	int k;
	for (k=0;k<g[x].size();k++) {
		if (!l[g[x][k]] || dfs(l[g[x][k]])) {
			l[g[x][k]]=x;
			return 1;
		}
	}
	return 0;
}

int main() {
	cin>>T;
	for (t=1;t<=T;t++) {
		cin>>n>>c>>q;
		memset(m,0,sizeof(m));
		for (i=1;i<=q;i++) {
			scanf("%d%d",&j,&k);
			m[k]++;
			a[k][m[k]]=j;
		}
		for (i=1;i<=q;i++) {
			g[i].clear();
		}
		for (i=1;i<=m[1];i++) {
			for (j=1;j<=m[2];j++) {
				if (a[1][i]!=a[2][j]) {
					g[i].push_back(m[1]+j);
				}
			}
		}
		memset(l,0,sizeof(l));
		s=0;
		for (i=1;i<=m[1];i++) {
			memset(v,0,sizeof(v));
			if (dfs(i)) {
				s++;
			}
		}
		if (s<m[2]) {
			for (k=1;k<=m[2];k++)
			if (!l[k+m[1]])
			break;
			if (k<=m[2])
			k=a[2][k];
		}
		else {
			memset(v,0,sizeof(v));
			for (k=1;k<=m[2];k++)
			v[l[k+m[1]]]=1;
			for (k=1;k<=m[1];k++)
			if (!v[k])
			break;
			if (k<=m[1])
			k=a[1][k];
		}
		if (m[1]==m[2] && s==m[1]) {
			printf("Case #%d: %d %d\n",t,s,0);
		}
		else {
			m[1]-=s;
			m[2]-=s;
			if (k==1) {
				printf("Case #%d: %d %d\n",t,s+m[1]+m[2],0);
			}
			else {
				q=min(m[1],m[2]);
				i=(m[1]==q?m[2]-q:m[1]-q);
				printf("Case #%d: %d %d\n",t,s+q+i,q);
			}
		}
	}
    return 0;
}
