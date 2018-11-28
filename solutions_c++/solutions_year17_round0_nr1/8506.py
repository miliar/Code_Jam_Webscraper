#define ll long long
#define mod 1000000007LL
#define F(a,b,c) for(a=b;a<c;a++)
#define Fr(a,b,c) for(a=b;a>=c;a--)
#define pf printf
#define sfd(a) scanf("%d",&a)
#define sfdd(a,b) scanf("%d%d",&a,&b)
#define sfl(a) scanf("%lld",&a)
#define sfll(a,b) scanf("%lld%lld",&a,&b)
#define pfd(a) printf("%d",a)
#define pfl(a) printf("%lld",a)
#define sf scanf
#define line printf("\n")
#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp(a,b) make_pair(a,b)
#define let(x,a) __typeof(a) x(a)
#define forall(it,v) for(it=v.begin();it!=v.end();it++)
char s[1024];
int main(){
int t,kk=1;
scanf("%d",&t);
while(kk<=t){
	sf("%s",s);
	int k,l=strlen(s),i,j,cnt=0,fl=0;
	sfd(k);
	F(i,0,l){
		if(s[i]=='-'){
			cnt++;
			if(i+k<=l)
				F(j,i,i+k){
					if(s[j]=='+')
						s[j]='-';
					else s[j]='+';
				}
			else fl=1;
		}
	}
	pf("Case #%d: ",kk);
	if(fl)
		pf("IMPOSSIBLE");
	else pfd(cnt);
	line;
	kk++;
}
return 0;
}
