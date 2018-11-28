#include<bits/stdc++.h>
using namespace std;

#define ll long long

map<ll,ll>mymap;
map<ll,ll>::iterator im;

void solve(ll n,ll k){
	ll runner=0;
	mymap.insert(make_pair(n,1));
	ll t_len;
	while(runner<k){
		//cout<<runner<<endl;
		im=mymap.end(); --im;
		ll segment_len=im->first;
		ll segment_cnt=im->second;
		mymap.erase(im);
		runner=runner+segment_cnt;
		if(runner>=k){
			t_len=segment_len;
			break;
		}
		else{
			if(segment_len%2!=0){
				// Odd so one half type only
				im=mymap.find((segment_len/2));
				if(im!=mymap.end()){
					im->second+=(segment_cnt*2);
				}
				else{
					mymap.insert(make_pair((segment_len/2),(segment_cnt*2)));
				}
			}
			else{
				// Even so two halves
				im=mymap.find((segment_len/2));
				if(im!=mymap.end()){
					im->second+=(segment_cnt);
				}
				else{
					mymap.insert(make_pair((segment_len/2),(segment_cnt)));
				}
				im=mymap.find((segment_len/2-1));
				if(im!=mymap.end()){
					im->second+=(segment_cnt);
				}
				else{
					mymap.insert(make_pair((segment_len/2-1),(segment_cnt)));
				}
			}
		}
	}
	if(t_len%2==0){
		cout<<(t_len/2)<<" "<<(t_len/2-1)<<endl;
	}
	else{
		cout<<(t_len/2)<<" "<<(t_len/2)<<endl;
	}
	mymap.clear();
}

int main(){
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,ti;
	ll n,k;
	cin>>t;
	for(ti=1;ti<=t;++ti){
		cin>>n>>k;
		printf("Case #%d: ",ti);
		solve(n,k);
	}
	return 0;
}
