#include<bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define rep(i,a,b) for(i=a;i<=b;i++)
#define rep2(i,a,b,c) for(i=a;i<=b;i+=c)
#define ll long long
#define db double
#define pii pair<int,int>

pii ar[200];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tes,n,m,i,has,cas=0;
	cin>>tes;
	while(tes--){
		cas++;
		cin>>n>>m;
		rep(i,0,n-1){
			cin>>ar[i].f>>ar[i].s;
		}
		rep(i,0,m-1){
			cin>>ar[i].f>>ar[i].s;
		}
		if(max(n,m)==1){
			has=2;
		}
		if(max(n,m)==2){
			sort(ar,ar+n+m);
			if(min(ar[1].s-ar[0].f,ar[0].s+1440-ar[1].f) > 720){
				has=4;
			}
			else{
				has=2;
			}
		}
		cout<<"Case #"<<cas<<": "<<has<<"\n";
	}
}

