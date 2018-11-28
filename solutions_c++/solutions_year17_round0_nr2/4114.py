#include <bits/stdc++.h>
using namespace std;
#define int long long
ifstream fin("B-large.in");
ofstream fout("B.out");
int n;
int pw[20];
int32_t main(){
	ios::sync_with_stdio(false);
	pw[0]=1;
	for(int i=1;i<18;i++) pw[i]=pw[i-1]*10;
	int t; fin>>t;
	for(int tc=1;tc<=t;tc++){
		fin>>n;
		int ndigs=0;
		for(int i=n;i>0;i/=10) ndigs++;
		int ans=0,prev=0;
		for(int i=ndigs-1;i>=0;i--){
			int maxd=prev;
			for(int d=prev;d<=9;d++){
				int cur=ans;
				for(int k=i;k>=0;k--) cur+=d*pw[k];
				if (cur<=n) maxd=max(maxd,d);
				else break;
			}
			ans+=maxd*pw[i];
			prev=maxd;
		}
		fout<<"Case #"<<tc<<": "<<ans<<'\n';
	}
}
