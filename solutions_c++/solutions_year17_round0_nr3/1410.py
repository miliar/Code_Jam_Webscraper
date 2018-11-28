#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
typedef long long ll;
#define fst first
#define scn second
int main(){
	int T;	cin>>T;
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		ll k,n;	cin>>n>>k;
		map<ll,ll> mp;
		mp[n]=1;
		ll sum=1;
		while(k){
			map<ll,ll> mp2;
			if(k>sum){
				k-=sum;
				for(auto it:mp){
					if(it.fst%2==1){
						mp2[(it.fst-1)/2]+=it.scn*2;
					}
					else{
						mp2[it.fst/2]+=it.scn;
						mp2[it.fst/2-1]+=it.scn;
					}
				}
				mp=mp2;
				sum=0;
				for(auto it:mp)	sum+=it.scn;
			}
			else{
				for(map<ll,ll>::reverse_iterator it=mp.rbegin();it!=mp.rend();it++){
					auto tmp=*it;
					if(k>tmp.scn)	k-=tmp.scn;
					else{
						k=0;
						if(tmp.fst%2==1){
							ll out=(tmp.fst-1)/2;
							cout<<out<<" "<<out<<endl;
						}
						else{
							ll out=(tmp.fst-2)/2;
							cout<<out+1<<" "<<out<<endl;
						}
						break;
					}
				}
			}
		}
	}
	return 0;
}