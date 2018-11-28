#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int a[8],id[5],ans[110];
bool cmp(int x,int y) {
	return a[x]<a[y];
}
int last;
void print(int x) {
			switch(x) {
				case 1: 
					printf("R");
					while (a[4]) printf("GR"),a[4]--;
					break;
				case 2: 
					printf("Y");
					while (a[5]) printf("VY"),a[5]--;
					break;
				case 3: 
					printf("B");
					while (a[6]) printf("OB"),a[6]--;
					break;
				case 4:
					printf("G");break;
				case 5:
					printf("V");break;
				case 6:
					printf("O");break;
			}
			last =x;
}
void fail(){
	printf("IMPOSSIBLE\n");
}
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T,n,r,o,y,g,b,v;
	scanf("%d",&T);
	for (int _=1;_<=T;_++) {
		printf("Case #%d: ",_);
		scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
		a[1]=r,a[2]=y,a[3]=b,a[4]=g,a[5]=v,a[6]=o;
		for (int i=1;i<=3;i++) id[i]=i;
		sort(id+1,id+1+3,cmp);
		if (a[id[3]]+a[id[3]+3]==n){ 
			if (n%2==0 && a[id[3]]==a[id[3]+3]) {
				a[id[3]+3]=0;
				for (int i=1;i<=n/2;i++) {
					print(id[3]);print(id[3]+3);
				}
				puts("");
				continue;
			}else {
				fail();
				continue;
			}
		}
		bool flag=0;
		for (int i=1;i<=3;i++) 
			if (a[id[i]]&&a[id[i]]<=a[id[i]+3]) {
				fail();
				flag=1;
				break;
			}else a[id[i]]-=a[id[i]+3];
		if (flag) continue;
		sort(id+1,id+4,cmp);
		int sum=0;
		for (int i=1;i<=3;i++) sum+=a[id[i]];
		if (a[id[3]]>a[id[1]]+a[id[2]]) {
			fail();
			continue;
		}
		for (;;) {
			if (a[id[3]]==a[id[2]]&&a[id[2]]==a[id[1]]) {
				if (last==id[1]) swap(id[1],id[2]);
				while (a[id[3]]) {
					print(id[1]);
					print(id[3]);
					print(id[2]);
					a[id[3]]--;
				}
				break;
			}
			print(id[3]);a[id[3]]--;
			if (a[id[2]]<a[id[1]]) {
				print(id[1]);a[id[1]]--;
			}else {
				print(id[2]);a[id[2]]--;
			}
		}
		puts("");
	}
	return 0;
}
