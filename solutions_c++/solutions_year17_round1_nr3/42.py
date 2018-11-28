#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <utility>
#include <cstring>

using namespace std;

int tt;
int Hd,Ad,Hk,Ak,B,D;
int ans;

void go(int x,int y,int last,int hd,int ad,int hk,int ak,int cur) {
	if (hk<=ad) {
		if (hk>0) cur++;
		ans=min(ans,cur);
		return;
	}
	if (hd<=0) return;
	if (x>0) {
		if (last==1 && hd<=ak-D) return;
		if (hd<=ak-D) go(x,y,1,Hd-ak,ad,hk,ak,cur+1);
		else {
			ak=max(0,ak-D);
			go(x-1,y,0,hd-ak,ad,hk,ak,cur+1);
		}
	} else if (y>0) {
		if (last==1 && hd<=ak) return;
		if (hd<=ak) go(x,y,1,Hd-ak,ad,hk,ak,cur+1);
		else go(x,y-1,0,hd-ak,ad+B,hk,ak,cur+1);
	} else {
		if (last==1 && hd<=ak) return;
		if (hd<=ak) go(x,y,1,Hd-ak,ad,hk,ak,cur+1);
		else go(x,y,0,hd-ak,ad,hk-ad,ak,cur+1);
	}
}

int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

	scanf("%d",&tt);

	for (int ii=1;ii<=tt;++ii) {
		scanf("%d%d%d%d%d%d",&Hd,&Ad,&Hk,&Ak,&B,&D);

		printf("Case #%d: ",ii);
		int up1=0,up2=0;
		if (D!=0) up1=Ak/D+1;
		if (B!=0) up2=Hk/B+1;
		ans=100000;
		for (int i=0;i<=up1;++i)
			for (int j=0;j<=up2;++j)
				go(i,j,0,Hd,Ad,Hk,Ak,0);

		if (ans<100000) printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}

}