#include <bits/stdc++.h>
#define ll long long
#define var ll
#define vi vector<var>
#define pii pair<var,var>
#define pb push_back
#define fi first
#define se second
const int inf = 0x3f3f3f3f;

using namespace std;

int main(){
	
	int t,cont=0; cin>>t;
	ll n, k, contt, tam, ind;
	pii res,psh;
	while(t--){
		priority_queue< pii > pq;
		contt=0;
		cin>>n>>k;
		pq.push( pii(n,0) );
		while(contt<k){
			contt++;
			if(contt==k){res = pq.top(); break;}
			tam = pq.top().fi; ind = pq.top().se;
			pq.pop();
			if(tam>2){
				pq.push( pii(tam-(tam/2)-1, ind) );
				pq.push( pii(tam/2, ind+tam-(tam/2)-1) );
			} else if(tam==2){
				pq.push( pii(1,ind+1) );
			}
		}
		tam = res.fi - 1;
		cout<< "Case #" << ++cont << ": " <<tam-tam/2<<' '<<tam/2<<endl;
	}
	
	return 0;
}










