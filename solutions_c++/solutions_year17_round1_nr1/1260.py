#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <set>
#include <cstdio>
using namespace std;
typedef long long LL;

int T,r,c;
char mp[30][30];
int ll[30],rr[30],uu[30],dd[30];

bool check(int a,int x,int op) {
	if(op==0) {
		for(int i=uu[a];i<=dd[a];i++)
			if(mp[i][x]!='?') return 0;
	}
	else {
		for(int i=ll[a];i<=rr[a];i++)
			if(mp[x][i]!='?') return 0;
	}
	return 1;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		scanf("%d %d",&r,&c);
		for(int i=1;i<=r;i++)
			scanf("%s",mp[i]+1);
		memset(ll,0,sizeof(ll));
		memset(rr,0,sizeof(rr));
		memset(uu,0,sizeof(uu));
		memset(dd,0,sizeof(dd));
		for(int i=1;i<=r;i++) {
			for(int j=1;j<=c;j++) {
				int c=mp[i][j];
				if(c=='?') continue;
				c-='A';
				if(ll[c]==0||j<ll[c]) ll[c]=j;
				if(rr[c]==0||j>rr[c]) rr[c]=j;
				if(uu[c]==0||i<uu[c]) uu[c]=i;
				if(dd[c]==0||i>dd[c]) dd[c]=i;
			}
		}
		for(int k=0;k<26;k++) {
			char c=k+'A';
			if(ll[k]==0) continue;
			for(int i=uu[k];i<=dd[k];i++) {
				for(int j=ll[k];j<=rr[k];j++) {
					mp[i][j]=c;
				}
			}
		}
		for(int k=0;k<26;k++) {
			char c=k+'A';
			if(ll[k]==0) continue;
			while(ll[k]>1) {
				if(!check(k,ll[k]-1,0)) break;
				ll[k]--;
				for(int i=uu[k];i<=dd[k];i++)
					mp[i][ll[k]]=c;
			}
			while(rr[k]<c) {
				if(!check(k,rr[k]+1,0)) break;
				rr[k]++;
				for(int i=uu[k];i<=dd[k];i++)
					mp[i][rr[k]]=c;
			}
			while(uu[k]>1) {
				if(!check(k,uu[k]-1,1)) break;
				uu[k]--;
				for(int i=ll[k];i<=rr[k];i++)
					mp[uu[k]][i]=c;
			}
		}
		for(int k=0;k<26;k++) {
			char c=k+'A';
			if(ll[k]==0) continue;
			while(dd[k]<r) {
				if(!check(k,dd[k]+1,1)) break;
				dd[k]++;
				for(int i=ll[k];i<=rr[k];i++)
					mp[dd[k]][i]=c;
			}
		}
		printf("Case #%d:\n",t);
		for(int i=1;i<=r;i++)
			printf("%s\n",mp[i]+1);
	}
}