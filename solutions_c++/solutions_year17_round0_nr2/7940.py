#include<bits/stdc++.h>

using namespace std;

#define ll 							long long
#define boost 						ios_base::sync_with_stdio(false); //to synchronize the input of cin and scanf
#define fileio 						freopen("in.in","r",stdin); freopen("out.txt","w",stdout);

ll t,i,j,r,c,m,k,u,v;
int main(){
	fileio
	cin>>t;
	for(u=1;u<=t;u++){
		string n,ans;
        v=0;
        ans="";
		cin>>n;
		k = n.length();
		j = k-1;
		for(i=k-1;i>=1;i--){
            if(n[i]<n[i-1]){
                for(;j>=i;j--){
                    n[j]='9';
                }
                n[i-1]-=1;
            }
        }
        for(i=0;i<k;i++){
            if(v==0 && n[i]=='0'){
                continue;
            }
            if(n[i]!='0'){
                v=1;
                ans+=n[i];
            }
        }
		cout<<"Case #"<<u<<": "<<ans<<endl;
	}
	return 0;
}
