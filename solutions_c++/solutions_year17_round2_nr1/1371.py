#include<bits/stdc++.h>
using namespace std;
 
#define ll long long
#define dbg(x)  cout<<#x<<"="<<x<<endl
#define N 2001025
#define MOD  786433
#define pb push_back
#define iosbase  ios_base::sync_with_stdio(false)
#define dbg(x)  cout<<#x<<"="<<x<<endl

vector< pair <double,double > >node;
int main(){

	ll t,n,tc;
	double d,curpos,tm,curt,maxt,ans,sp,a,b;
	cin>>t;

	for(tc=1;tc<=t;tc++){
		maxt=0;
		printf("Case #%d: ",tc);
		cin>>d>>n;
		for(int i=0;i<n;i++){
			cin>>a>>b;
			node.push_back({a,b});
		}
		sort(node.begin(),node.end());
		reverse(node.begin(),node.end());

		for(int i=0;i<n;i++){
			curpos=node[i].first;
			sp=node[i].second;
			curt=(d-curpos)/sp;
			if(curt > maxt)
				maxt=curt;
		}
		if(maxt!=0)
			ans=d/maxt;
		printf("%.7lf\n",ans);
		node.clear();
	}
}