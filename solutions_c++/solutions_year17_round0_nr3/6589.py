#include <bits/stdc++.h>
#define ll long long
using namespace std;


int main(){
	ll t;
	cin>>t;
	ll hmm=1;
	while(t--){
		ll n, k;
		cin>>n>>k;
		bool array[n+2];
		memset(array,false,sizeof(array));

		array[0]=array[n+1]=true;
		for(int h=0;h<k;h++){
			ll l=-1, r=-1, index;
			for(int i=1;i<=n;i++){
				ll ls=-1, rs=-1;
				if(array[i]==false){
					for(int j=i-1;j>=0;j--){
						if(array[j]){
							ls=i-j;
							break;
						}
					}
					for(int j=i+1;j<=n+1;j++){
						if(array[j]){
							rs=j-i;
							break;
						}
					}
					if(min(l,r)<min(ls,rs)){
						l=ls, r=rs, index=i;
					}
					else if(min(l,r)==min(ls,rs) && max(l,r)<max(ls,rs)){
						l=ls, r=rs, index=i;
					}
				}
				
			}	
			array[index]=true;
			if(h==k-1){
				cout<<"Case #"<<hmm<<": "<<max(l,r)-1<<" "<<min(l,r)-1<<endl;
				hmm++;
			}
		}
	}
}