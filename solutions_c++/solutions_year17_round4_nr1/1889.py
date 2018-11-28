#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#define re(i,a,b) for(int i = a; i <= b; i++)
using namespace std;
int T;
int n,p;
int a[110],cnt[10]; 
int ans;
int min(int x, int y){
	if(x<y) return x;
	return y;
}
int main(){
//	freopen("A.in", "r",stdin);freopen("A.out","w",stdout);
	scanf("%d", &T); 
	re(casen, 1, T){
		scanf("%d%d", &n, &p);
		re(i,0,n-1) {
			scanf("%d", &a[i]);
			a[i] = a[i] % p;
		}
		memset(cnt,0,sizeof(cnt));
		re(i,0,n-1)
			cnt[a[i]]++;
		ans = cnt[0];//1..p-1
		for(int i = 1; i <        p-i; i++)
			ans += min(cnt[i], cnt[p-i]);
		//if(p%2==0) ans+= cnt[p/2]/2;
		switch(p){
			case 2:{
				ans += cnt[1]/2 + (cnt[1]%2!=0);
				break;
			}
			case 3:{
				if(cnt[1]>cnt[2]){
					ans += (cnt[1]-cnt[2])/3 + ((cnt[1]-cnt[2])%3!=0);
				}
				else
				if(cnt[2]>cnt[1]){
					ans += (cnt[2]-cnt[1])/3 + ((cnt[2]-cnt[1])%3!=0);
				}
				break;
			}
			case 4: {
				if(cnt[2]%2==0)//only 1 or 3
				{
					int tmp = cnt[1]-cnt[3];
					if(tmp<0) tmp =  -tmp;
					ans += tmp/4 + (tmp%4!=0);
				}
				else {
					int tmp = cnt[1]-cnt[3];
					if(tmp<0) tmp = -tmp;
					if(tmp>2){
						int t1 = (tmp-2)/4+ ((tmp-2)%4!=0) + 1;
						int t2 = tmp/4 + (tmp%4!=0);
						if(tmp%4==0) t2++;
						if(t1>t2) ans+=t1;
						else ans+=t2;
					}
					else if(tmp==1){
						ans+=1;
					}
				}
				break;
			}
			}
		printf("Case #%d: %d\n", casen, ans);
		
	}
	return 0;
//	fclose(stdin);fclose(stdout);
}

