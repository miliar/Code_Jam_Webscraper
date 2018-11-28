#include<bits/stdc++.h>

using namespace std;
 
typedef long long ll;


ll A[1000000];
int main(){
 freopen("input.txt", "r", stdin);
             freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	int i=0;
	while(t--){
            
		for(int m=0;m<1000000;m++){
			A[m]=0;
		}
		i++;
		ll n,k,s=1,p=0;
		cin>>n>>k;
		ll k1 = k;
		A[0]=n;
		while(k--){
            sort(A+p,A+s,std::greater<ll>());
			
			ll a = A[p] / 2 ;

				A[s++]=a;
	
			if(A[p]%2==0){
     			A[s++]=a-1;
			}	
			else
		          {A[s++]=a;}

p++;
		}

cout<<"Case #"<<i<<": "<<A[s-2]<<" "<<A[s-1]<<endl;
	
	}

}
