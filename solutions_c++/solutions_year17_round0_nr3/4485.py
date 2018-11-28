#include <bits/stdc++.h>
#define fore(i,a,n) for(int i=a,qwer=n;i<qwer;i++)
#define fst first
#define snd second
#define pb push_back
#define mp make_pair
using namespace std;
 
typedef long long ll;
typedef pair<int,int> ii;
 
int main() {
	int tn;
	scanf("%d",&tn);
	fore(tc,0,tn) {
		int n,k;
		scanf("%d%d",&n,&k);
		priority_queue<ii> q;
		q.push(ii(n,0));
		fore(i,0,k-1) {
			ii p=q.top();
			q.pop();
			ii l,r;
			if(p.fst&1) {
				l=ii(p.fst/2,p.snd);
				r=ii(p.fst/2,p.snd+p.fst/2+1);
			}
			else {
				l=ii(p.fst/2-1,p.snd);
				r=ii(p.fst/2,p.snd+p.fst/2);
			}
			q.push(l);
			q.push(r);
		}
		n=q.top().fst;
		int mn=0,mx=0;
		if(n) {
			if(n%2==0)
				mn=n/2-1,mx=n/2;
			else
				mn=mx=n/2;
		}
		printf("Case #%d: %d %d\n",tc+1,mx,mn);
	}
 
}
