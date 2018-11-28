#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define fore(i,a,b) for(int i=a,ThxDem=b;i<ThxDem;++i)
using namespace std;
typedef long long ll;

ll n;

bool istydy(ll n){
	int l=10;
	while(n){
		if(n%10>l)return false;
		l=n%10;
		n/=10;
	}
	return true;
}

int main(){
	int tn;
	scanf("%d",&tn);
	fore(tc,1,tn+1){
		printf("Case #%d: ",tc);
		scanf("%lld",&n);
		int q=0;
		while(!istydy(n)){
			while(n%10!=9)n--;
			n/=10;
			q++;
		}
		assert(n>=0);
		if(n)printf("%lld",n);
		fore(i,0,q)putchar('9');
		puts("");
	}
	return 0;
}















