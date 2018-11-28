#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#define re(i,a,b) for(int i = a; i <= b; i++)
using namespace std;
int T; 
int ac,aj;
int c[300],d[300],type[300],ord[300];
int ans;
int n;
int nj,nc,lj,lc,cc,cj;
int kc[300],kj[300];
int cmp1(int x, int y){
	return c[x]<c[y];
}
int cmp(int x, int y){
	return x<y;
}
int main(){
//	freopen("B.in","r",stdin);freopen("B.out","w",stdout);
	scanf("%d", &T);
	re(casen, 1, T){
		scanf("%d%d", &ac, &aj);
		re(i,0,ac-1){
			scanf("%d%d", &c[i],&d[i]); 
			type[i] = 0;
			ord[i] = i;
		}
		re(i,0,aj-1){
			scanf("%d%d", &c[i+ac], &d[i+ac]);
			type[i+ac]=1;
			ord[i+ac] = i+ac;
		}
		n = ac+aj;nj=nc=0;
		ans = 0;
		sort(ord,ord+n,cmp1);
		re(i,0,n-1){
			if(type[ord[i]]==type[ord[(i+1)%n]])
			{
				ans+=2;
				if(type[ord[i]]){
					kj[nj] = c[ord[(i+1)%n]]-d[ord[i]];
					if(kj[nj]<0) kj[nj]+=1440;
					nj++;
				}
				else{
					kc[nc] = c[ord[(i+1)%n]]-d[ord[i]];
					if(kc[nc]<0) kc[nc]+=1440;
					nc++;
				}
			}
			else ans+=1;
		}
		lc = lj = 720;
		re(i,0,ac-1)
			lc-=(d[i]-c[i]);
		re(i,ac,ac+aj-1)
			lj-=(d[i]-c[i]);
		cc=cj=0;
		sort(kj,kj+nj,cmp);
		sort(kc,kc+nc,cmp);
		re(i,0,nj-1)
		{
			if(lj>=kj[i]){
				lj-=kj[i];
				cj++;
			}
			if(lj<=0) break;
		}
		re(i,0,nc-1){
			if(lc>=kc[i]){
				lc-=kc[i];
				cc++;
			}
			if(lc<=0) break;
		}
		ans = ans-2*(cc+cj);
		printf("Case #%d: %d\n", casen, ans);
	}
//	fclose(stdin);fclose(stdout);
	return 0;
}
