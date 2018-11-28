#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <set>
#include <cstdio>
using namespace std;
typedef long long LL;

int T,n,p,ans;
int tt[100],qq[100][100],ll[100][100],rr[100][100];

int kk,pp[20];

int check() {
	int res=0;
	for(int i=1;i<=p;i++) {
		if(ll[1][i]>rr[1][i]||ll[2][pp[i]]>rr[2][pp[i]]) continue;
		if(ll[1][i]<=ll[2][pp[i]]&&ll[2][pp[i]]<=rr[1][i]) res++;
		else if(ll[1][i]<=rr[2][pp[i]]&&rr[2][pp[i]]<=rr[1][i]) res++;
	}
	return res;
}

void get(int pos)
{
    if(pos==kk+1)
        ans=max(check(),ans);
    else
    {
        for(int i=1;i<=kk;i++)
        {
            int ok=1;
            for(int j=1;j<pos;j++)
                if(pp[j]==i) { ok=0;break;}
            if(ok==1)
            {
                pp[pos]=i;
                get(pos+1);
            }
        }
    }
}

int main() {
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		scanf("%d %d",&n,&p);
		for(int i=1;i<=n;i++)
			scanf("%d",&tt[i]);
		for(int i=1;i<=n;i++) {
			for(int j=1;j<=p;j++) {
				scanf("%d",&qq[i][j]);
				int x=qq[i][j],y=tt[i];
				if((10*x)%(9*y)==0) ll[i][j]=(10*x)/(11*y);
				else ll[i][j]=(int)ceil(((double)10*x)/(11*y));
				rr[i][j]=(int)floor(((double)10*x)/(9*y));
				//printf("i=%d j=%d ll=%d rr=%d\n",i,j,ll[i][j],rr[i][j]);
			}
		}
		if(n==1) {
			ans=0;
			for(int i=1;i<=p;i++)
				if(ll[1][i]<=rr[1][i]) ans++;
		}
		else {
			kk=p;ans=0;
			get(1);
		}
		printf("Case #%d: %d\n",t,ans);
	}
}