#include "bits/stdc++.h"
#define ll long long
using namespace std;
// 1 |2| 3| 4 |5| 6| 7 |8| 9 10
int main()
{
	int t;
	cin>>t;
	for(int tt = 1; tt <= t; tt++){
		cout<<"Case #"<<tt<<": ";
		ll n, k,mx=0,mn=0,l,h;
		cin>>n>>k;
		priority_queue<ll > hep;
		hep.push(n);
		while(k--){
			l = hep.top();
			hep.pop();
			if(l&1){
				mx=mn = l>>1;
				hep.push( l>>1);
				hep.push(l>>1);
			}else{
				mx = l>>1;

				mn = max(mx - 1, 0LL);
				hep.push(mx);
				hep.push(mn);
			}
			if(mx==0 && mn == 0)
				break;
		
		}
		cout<<mx<<" "<<mn<<endl;			
	
	}
	return 0;

}
