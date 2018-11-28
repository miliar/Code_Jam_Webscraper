#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define fore(i,a,b) for(int i=a,ThxDem=b;i<ThxDem;++i)
using namespace std;
typedef long long ll;

bitset<2048> w;
bitset<2048> z;
char s[2048];
int n,k;

int main(){
	int tn;
	scanf("%d",&tn);
	fore(tc,1,tn+1){
		printf("Case #%d: ",tc);
		w.reset();
		scanf("%s%d",s,&k);n=strlen(s);
		fore(i,0,n)if(s[i]=='-')w[i]=1;
		z.reset();
		fore(i,0,k)z[i]=1;
		int r=0;
		fore(i,0,n-k+1)if(w[i])w^=z<<i,r++;
		if(w.any())puts("IMPOSSIBLE");
		else printf("%d\n",r);
	}
	return 0;
}
