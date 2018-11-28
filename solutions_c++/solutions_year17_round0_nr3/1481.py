#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#define ll long long
using namespace std;
int T;
ll n,k;
ll x,y,a,b,t,s,t1;
ll ans;
ll ta,tb;
ll ts;
int main(){
//	freopen("C.in","r",stdin);	freopen("C.out","w",stdout); 
	scanf("%d", &T);
	for(int casen = 1; casen<=T; casen++)
	{
		scanf("%lld%lld", &n,&k);
		printf("Case #%d: ", casen);
		t = 0;
		ta = tb =n;
		ts = 1;
		while(ts<=k) {
			t++;
			ts = ts*2;
			if(t>1)
			if(ta==tb){
				if(ta%2) ta=tb=ta/2;
				else {ta=(ta-2)/2;tb=ta+1;}
			} 
			else{
				if(ta%2){
					ta = (ta-1)/2;
					tb = tb-1-ta;
					if(tb<ta){
						ta ^= tb;
						tb ^= ta;
						ta ^= tb;
					}
				}
				else{
					tb = (tb-1)/2;
					ta = ta-1-tb;
					if(tb<ta){
						ta^=tb;
						tb^=ta;
						ta^=tb;
					}
					} 
				}
		} 
		// n-(1<<(T-1))000+1

		x = t;
		y = k+1-(ts/2);
		s = n-ts/2+1;//¸Ã²ã×ÜºÍ 8
		if(ta==tb) {
			if(ta%2==1)
				printf("%lld %lld\n", ta/2, ta/2);
			else printf("%lld %lld\n", 1+((ta-2)/2), (ta-2)/2);
		}
		else{
			a =s%(ts/2);
			if(a>=y) 
				if(tb%2)
					printf("%lld %lld\n", (tb-1)/2,(tb-1)/2);
				else printf("%lld %lld\n", tb/2, tb/2-1);
			else
				if(ta%2)
					printf("%lld %lld\n", (ta-1)/2,(ta-1)/2);
				else printf("%lld %lld\n", ta/2, ta/2-1);
		}
		continue;
		t1 = s%(ts);//
		if(t1){
			if((n%4)<2)
			{
//			tmp = (n/(n-(n&(n-1))))-2;
				a = (ts)-t1;
				b = (s+a)/(ts);
				if((ts/2)-a<y) printf("%lld %lld\n", b-1, b-1); 
				else printf("%lld %lld\n", b, b-1);
			}
			else{
				t1 = s%(ts/2);
				if(!t1)
					a = 0;
				else a = ((ts/2)-t1);
				b = (s+a-(ts/2))>>t;
				if((ts/2)-a<y) printf("%lld %lld\n", b, b-1);
				else printf("%lld %lld\n", b, b);
			}
		}
		else {
			ans = 2*s/ts;
			if(ans%2==1)
				printf("%lld %lld\n", ans/2, ans/2);
			else printf("%lld %lld\n", 1+((ans-2)/2), (ans-2)/2);
	}	
	}
//	fclose(stdin);	fclose(stdout);
	return 0;
}
