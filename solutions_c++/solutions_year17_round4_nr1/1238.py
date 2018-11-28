#include <bits/stdc++.h>
#define fr(x) scanf("%d", &x)
using namespace std;

int a[100010], m[100010];

int main(){
	int t, n, p, ans=0, temp, toadd=0;
	fr(t);

	for(int t1=1; t1<=t ;++t1){
		fr(n);
		fr(p);
		for(int i=0;i<111;++i){
			m[i]=0;
		}		
		ans=0;
		temp=0;
		toadd=0;
		for(int i=1; i<=n; ++i){
			fr(a[i]);
			a[i]%=p;
			++m[a[i]];
		}

		if(p==2){
			toadd=(m[1]%2);
			printf("Case #%d: %d\n", t1, toadd+m[0]+(m[1]/2));
		}
		else if(p==3){
			temp = min(m[1], m[2]);
			m[1]-=temp;
			m[2]-=temp;
			if((m[1]+m[2])%3) toadd=1;
			printf("Case #%d: %d\n", t1, toadd+m[0]+temp+((m[1]+m[2])/3));
		}
		else if(p==4){
			ans+=(m[2]/2);
			m[2]%=2;
			
			temp=min(m[1], m[3]);
			ans+=temp;
			m[1]-=temp;
			m[3]-=temp;
			
			if(m[1]>=2 && m[2]>=1){
				m[1]-=2;
				m[2]-=1;
				ans+=1;
			}
			if(m[3]>=2 && m[2]>=1){
				m[3]-=2;
				m[2]-=1;
				ans+=1;
			}
			if(m[2]) toadd=1;
			else if(((m[1]+m[3])%4)) toadd=1;
			printf("Case #%d: %d\n", t1, toadd+m[0]+ans+((m[1]+m[3])/4));
		}
	}
	return 0;
}