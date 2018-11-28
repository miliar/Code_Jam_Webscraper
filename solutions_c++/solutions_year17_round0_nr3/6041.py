//
//Worm4047
//Rocks
//

#include <bits/stdc++.h>
using namespace std;
#define ll long long

#define pr pair<long long,long long>

class comp {
public:
	bool operator()(pr n1,pr n2){
		ll s1 = n1.second - n1.first;
		ll s2 = n2.second - n2.first;
		if(s1 < s2)
			return true;
		else if(s1 > s2)
			return false;
		else{
			return n1.first > n2.first;
		}
	}
} ;

int main(){

	ll t;
	cin>>t;
	ll n,k;
	for(ll m=1;m<=t;m++){
			cin>>n>>k;
			priority_queue<pr,vector<pr>,comp> q;	
			q.push(make_pair(0,n-1));
			while(k>1){
				pr val = q.top();
				q.pop();
				ll size = val.second - val.first ;
				ll i = val.first + size/2;

				if(i!=val.first)q.push(make_pair(val.first,i-1));
				if(i!=val.second)q.push(make_pair(i+1,val.second));
				k--;
			}
			pr val = q.top();		
			ll size = val.second - val.first ;
			ll i = val.first + size/2;

			ll d1 = min(i-val.first,val.second-i);

			ll d2 = max(i-val.first,val.second-i);
			cout<<"Case #"<<m<<": "<<d2<<" "<<d1<<endl;
		}
		

	return 0;
}
