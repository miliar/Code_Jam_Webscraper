#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#define re(i,a,b) for(int i = a; i <= b; i++)
#define rep(i,a,b) for(int i = a; i >= b; i--) 
using namespace std;
int T;
int n,k;
int flag;
long long r[100010],h[100010];
int a[100010],ord[10010],ord1[10010]; 
int cnt,last,tmp;
long long tot,ans;
int cmp(int x, int y){
	if(r[x]<r[y]) return 1;
	if(r[x]==r[y] && h[x]<h[y]) return 1;
	return 0;
}
int cmp1(int x, int y){
	if(r[x]*h[x]>r[y]*h[y]) return 1;
	return 0;
}
void add(int x){//h 从大到小排。 
	if(cnt<k-1){
		cnt++;
		a[cnt] = x;
		int tmp = cnt;
		while(tmp>1){
			if(r[a[tmp]]*h[a[tmp]]<r[a[tmp>>1]]*h[a[tmp>>1]]){
				a[tmp] ^= a[tmp>>1];
				a[tmp>>1] ^= a[tmp];
				a[tmp] ^= a[tmp>>1];
				tmp = tmp>>1;
			}
			else break;
		}
	}
	else{
		if(r[x]*h[x]<=r[a[1]]*h[a[1]]) return;
		a[1] = x;
		int tmp = 1,t1;
		while((tmp<<1)<=cnt){
			t1 = tmp;
			if(r[a[(tmp<<1)]]*h[a[(tmp<<1)]]<r[a[t1]]*h[a[t1]]) t1 = tmp<<1;
			if(r[a[(tmp<<1)+1]]*h[a[(tmp<<1)+1]]<r[a[t1]]*h[a[t1]]) t1 = (tmp<<1)+1;
			if(t1==tmp) break;
			a[tmp] ^= a[t1];
			a[t1] ^= a[tmp];
			a[tmp] ^= a[t1];
			tmp = t1;
		}
	}
}
int main(){
//	freopen("A-large (5).in","r",stdin);freopen("A.out","w",stdout);
	scanf("%d",&T);
	re(casen,1,T){
		scanf("%d%d", &n, &k);
		re(i,0,n-1){
			scanf("%ld%ld", &r[i], &h[i]);
			ord[i] = i;
			ord1[i] = i;
		}
		sort(ord,ord+n,cmp); //0..n-1 r[i]<..   h[i]<..
		sort(ord1,ord1+n,cmp1);
		ord[n] = n;
		r[n] = r[ord[n-1]]+1;
		ans = 0;
		rep(i,n-1,0){
			//r[ord[i]]
			if(r[ord[i]]!=r[ord[i+1]]){
				cnt = 0;
				tot = r[ord[i]]*h[ord[i]];
				int j = 0;
				while(j<n){
					while(j<n && (r[ord1[j]]>r[ord[i]] || ord1[j]==ord[i])) j++;
					if(j>=n) break;
					cnt++;
					if(cnt==k) break;
					tot+=r[ord1[j]]*h[ord1[j]];
					j++;
				}
				if(cnt<k-1) break;
				tot = tot*2;
				tot += r[ord[i]]*r[ord[i]];
				if(tot>ans) ans = tot;
			}
		}
		printf("Case #%d: %.9lf\n",casen, double(ans)*3.1415926535897932626);
	}
//	fclose(stdin);fclose(stdout);
	return 0;
}
