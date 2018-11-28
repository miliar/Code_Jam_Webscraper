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
#define pll pair<ll,ll>

db pi=acos(-1);
pll ar[1005];

bool hakal(pll aw,pll ak){
	return aw.f*aw.s > ak.f*ak.s;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tes,cas,n,k,i,rem,j;
	ll lu,has;
	cin>>tes;
	while(tes--){
		cas++;
		has=0;
		cin>>n>>k;
		rep(i,0,n-1){
			cin>>ar[i].f>>ar[i].s;
		}
		sort(ar,ar+n,hakal);
		rep(i,0,n-1){
			rem =k-1;
			lu=ar[i].f*ar[i].f+(ll)2*ar[i].f*ar[i].s;
			rep(j,0,n-1){
				if(rem==0){
					break;
				}
				if(i==j || ar[j].f > ar[i].f){
					continue;
				}
				rem--;
				lu+=((ll)2*ar[j].f*ar[j].s);
			}
			has=max(has,lu);
		}
		cout<<"Case #"<<cas<<": ";
		cout<<fixed<<setprecision(9)<<pi*(db)has<<"\n";
	}
}

