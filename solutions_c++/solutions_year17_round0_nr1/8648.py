#include <bits/stdc++.h>
using namespace std;

int vis[1<<10];


int main() {
	//freopen("in.in","rt",stdin);
	//freopen("newfile.txt","wt",stdout);
	int z;
	cin>>z;
	for(int t=1;t<=z;t++){
		string x;
		int k,msk=0;
		cin>>x>>k;
		int l=x.size();
		for(int i=0;i<l;i++){
			if(x[i]=='-') msk|=(1<<i);
		}
		deque<pair<int,int> > q;
		q.push_back(make_pair(0,msk));
		memset(vis,0,sizeof vis);
		int ans=-1;
		while(q.size()){
			int dis=q[0].first,m=q[0].second;
			q.pop_front();
			if(m==0){
				ans=dis;
				break;
			}
			vis[m]=1;

			for(int i=0;i+k<=l;i++){
				int v=m;
				for(int j=i;j<i+k;j++){
					v^=(1<<j);
				}
				if(!vis[v]) q.push_back(make_pair(dis+1,v));
			}

		}
		cout<<"Case #"<<t<<": ";
		if(ans!=-1) cout<<ans<<"\n";
		else cout<<"IMPOSSIBLE\n";
	}

	return 0;
}
