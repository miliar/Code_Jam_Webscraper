#include<bits/stdc++.h>

using namespace std;

int main(){
	int t,z; cin>>t;
	for(z=1;z<=t;z++){
		long long int n,p,q; cin>>n;
		//string s= to_string(n);
		//int k= s.length();
		p=n,q=n;
		int a[20],i,k=19;
		for(i=0;i<20;i++) a[i]=0;
		while(n){
			a[k--]=n%(long long int)10;
			n=n/(long long int)10;
		}
		k=19;
		//for(i=0;i<20;i++) cout<<a[i]<<" ";

		while(true){
            int flag=-1,k=19;
            for(i=0;i<19;i++){
                if(a[i]>a[i+1]){
                    flag=1;
                    //cout<<"i="<<i<<endl;
                    break;
                }
            }
            //cout<<"q="<<q<<endl;
            if(flag==-1){
                cout<<"Case #"<<z<<": "<<q<<endl;
                break;
            }
            else{
                p=q-1;
                q--;
                while(p){
                    a[k--]=p%(long long int)10;
                    p=p/(long long int)10;
                }
            }
            //for(i=0;i<20;i++) cout<<a[i]<<" ";

		}
	}
	return 0;
}
