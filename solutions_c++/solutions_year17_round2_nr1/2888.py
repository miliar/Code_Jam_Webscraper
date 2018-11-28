#include <bits/stdc++.h>
#define fore(i,a,n) for(int i = a,qwer = n;i<qwer;i++)
#define fst first
#define snd second
#define pb push_back
#define mp make_pair

using namespace std;
typedef long long ll;
typedef pair<int,int> ii;

int d,n;
int k[1002],s[1002];

pair<double,double> fun(int j) {
	double t = (d-k[j])*1./s[j];
	double ss = t*s[j]+k[j];
	return mp(t,ss);
}

pair<double,double> ans[1002];

int main(){
	int t;
	scanf("%d",&t);
	int q=1;
	while(t--) {
		scanf("%d %d",&d,&n);
		for(int i=0;i<n;i++) {
			scanf("%d %d",&k[i],&s[i]);
			ans[i]=fun(i);
		}
		/*if(q==84) {
			printf("d=%d n=%d\n",d,n);
			for(int i=0;i<n;i++) {
				printf("k[%d]=%d s[%d]=%d\n",i,k[i],i,s[i]);
			}
		}*/
		sort(ans,ans+n);
		reverse(ans,ans+n);
		double r = ans[0].snd/ans[0].fst;
		printf("Case #%d: %.10lf\n",q,r);
		q++;
	}
	return 0;
}