#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define fore(i,a,b) for(int i=a,ThxDem=b;i<ThxDem;++i)
using namespace std;
typedef long long ll;

int hd,ad,hk,ak,b,d;

int doit(int nd, int nb){
	int h0=hd,h1=hk,r=0,a0=ad,a1=ak;
	fore(i,0,nd){
		if(a1-d>=h0){
			h0=hd-a1;r++;
			if(a1-d>=h0)return 1<<30;
		}
		r++;
		a1-=d;
		a1=max(a1,0);
		h0-=a1;
		if(h0<0)return 1<<30;
	}
	fore(i,0,nb){
		if(a1>=h0){
			h0=hd-a1;r++;
			if(a1>=h0)return 1<<30;
		}
		r++;
		a0+=b;
		h0-=a1;
		if(h0<0)return 1<<30;
	}
	while(1){
		if(a0>=h1){
			r++;
			break;
		}
		if(a1>=h0){
			h0=hd-a1;r++;
			if(a1>=h0)return 1<<30;
		}
		r++;
		h1-=a0;
		h0-=a1;
	}
	return r;
}

int main(){
	int tn;
	scanf("%d",&tn);
	fore(tc,1,tn+1){
		printf("Case #%d: ",tc);
		scanf("%d%d%d%d%d%d",&hd,&ad,&hk,&ak,&b,&d);
		if(ad>=hk){puts("1");continue;}
		if(ak-d>=hd){puts("IMPOSSIBLE");continue;}
		if(ak<hd&&(2*ad>=hk||ad+b>=hk)){puts("2");continue;}
		if(2*ak-3*d>=hd){puts("IMPOSSIBLE");continue;}
		int r=1<<30;
		fore(nd,0,103)fore(nb,0,103)r=min(r,doit(nd,nb));
		if(r==(1<<30))puts("IMPOSSIBLE");
		else printf("%d\n",r);
	}
	return 0;
}
