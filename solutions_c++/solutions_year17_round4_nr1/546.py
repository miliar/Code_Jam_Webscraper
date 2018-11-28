//hi
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
typedef long long int LL;
int s[103];
int n,p;
int hh;
void sol2(){
	int i;
	int cnt=0;
	for(i=0;i<n;i++){
		if(s[i]%2==0) cnt++;
	}
	int x=n-cnt;
	printf("Case #%d: %d\n",hh,cnt+(x+1)/2);
}
void sol3(){
	int a0=0, a1=0, a2=0;
	int i;
	for(i=0;i<n;i++){
		if(s[i]%3==0) a0++;
		else if(s[i]%3==1) a1++;
		else a2++;
	}
	int x=min(a1,a2);
	a1-=x; a2-=x;
	int c=a1/3 + a2/3;
	if(a1%3) c++;
	if(a2%3) c++;
	int ans=a0+x+c;
	printf("Case #%d: %d\n",hh,ans);
}
void sol4(){
	int a[5];
	int i;
	for(i=0;i<4;i++) a[i]=0;
	for(i=0;i<n;i++)
		a[s[i]%4]++;
	int ans=0;
	ans+=a[0];
	int x=min(a[1], a[3]);
	a[1]-=x; a[3]-=x;
	ans+=x;
	x=a[2]/2;
	a[2]-=x*2;
	ans+=x;
	int l=max(a[1], a[3]);
	if(a[2]==0){
		int c=l/4;
		if(l%4) c++;
		printf("Case #%d: %d\n",hh,ans+c);
	}else{
		l-=2;
		int c=1;
		if(l>0){
			c+=l/4;
			if(l%4) c++;
		}
		printf("Case #%d: %d\n",hh,ans+c);
	}
}
int main(void){
    int t;
    scanf("%d",&t);
    for(hh=1;hh<=t;hh++){
		scanf("%d%d",&n,&p);
		int i;
		for(i=0;i<n;i++)
			scanf("%d",&s[i]);
		if(p==2) sol2();
		if(p==3) sol3();
		if(p==4) sol4();
	}
    return 0;
}
