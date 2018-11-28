#include <bits/stdc++.h>
#define ull unsigned long long
using namespace std;
int main(){
	int t,k;
	cin>>t;
	k=0;
	while(t--){
		k++;
		ull n,value,ans;
		cin>>n;
		ans=n;
		bool sub=true;
		while(sub){
			value=ans;
			vector<int> vc;
			while (value > 0) {
			 int digit = value % 10;
			 vc.push_back(digit);
			 value /= 10;
			}
			ull i=1;
			for(i=1;i<vc.size();i++){
				if(vc[i]>vc[i-1]){
					ans=ans-(ans % (ull) pow(10,i));
					ans--;
					break;
				}
			}
			if(i==vc.size()){
				sub=false;
			}
		}
		cout<<"case #"<<k<<": "<<ans<<endl;
	}
}