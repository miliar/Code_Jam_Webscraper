#include<bits/stdc++.h>
#define mp make_pair
using namespace std;

int t,n,k;
priority_queue<pair<int,int>,vector<pair<int,int> > > pq;

int main(){
	FILE *fout = fopen("output_c.txt","w");
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		scanf("%d %d",&n,&k);
		pq.push(mp(n,-1));
		int maxi,mini;
		for(int i=1;i<=k;i++){
			pair<int,int> p=pq.top();
			pq.pop();
			int l=-p.second;int len=p.first;int r=l+len-1;
			int mid=(l+r)/2;
			int kiri=(mid-l);int kanan=(r-mid);
			maxi=max(kiri,kanan); mini=min(kiri,kanan);
			pq.push(mp(mid-l,-l));
			pq.push(mp(r-mid,-mid-1));
		}
		while(!pq.empty()) pq.pop();
		printf("Case #%d: %d %d\n",tc,maxi,mini);
		fprintf(fout,"Case #%d: %d %d\n",tc,maxi,mini);
	}
	return 0;
}
