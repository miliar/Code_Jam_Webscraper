#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int qq=1;qq<=t;qq++){
		ll n;
		cin>>n;
		cout<<"Case #"<<qq<<": ";
		ll tmp=n;
		int nd=0;
		ll qo=1;
		while(tmp>0){
			tmp/=10;
			nd++;
		}	
		if(nd==1){
			cout<<n<<endl;
			continue;
		}
		int flag=nd;
		while(flag--){
			qo*=10;
		}
		qo/=10;
		//cout<<qo<<nd<<endl;
		ll ans;
		int p=n/qo; //previous digit.
		ans=p;
		n=n%qo;
		qo/=10;
		bool cont=0;
		int pd=0;
		int cd=1;
		while(cd<nd){
			int d=n/qo;
			n%=qo;
			//cout<<"! "<<ans<<" "<<p<<" "<<d<<endl;
			if(d>=p){
				ans=ans*10+d;
				p=d;
			} else{
				ans--;
				p=ans%10;
				while(cd>1){
					d=(ans/10)%10;
					if(d<=p) break;
					else{
						ans=ans/10;
						ans--;
						//cout<<"!! "<<ans<<endl;
						d--;
						p=d;
					}
					cd--;
				}
				break;
			}
			cd++;
			qo/=10;
		}
		while(cd<nd){
			ans=ans*10+9;
			cd++;
		}
		cout<<ans<<endl;
			
	}
	return 0;
}
