#include <bits/stdc++.h>
#include <math.h>
using namespace std;

int main(){
    int test;
    long long n,k,pol,r,h,big_r,res,bigest_r;
    vector<pair<long long,long long> > pan;
    long double pi=3.1415926535897932384626433832795028841971693993751;
    cin>>test;
	for(int tt=1;tt<=test;tt++){
		pan.clear();
		big_r=0;
		bigest_r=0;
		cin>>n>>k;
		for(int i=0;i<n;i++){
			cin>>r>>h;
			pan.emplace_back(2*r*h,r);
			if(r>big_r)big_r=r;
		}
		sort(pan.begin(),pan.end(),greater<pair<long long,long long>>());
		res=0;
		for(int i=0;i<k;i++){
			res+=pan[i].first;
			if(pan[i].second>bigest_r)
				bigest_r=pan[i].second;
		}
		long long ma=0;
		for(int i=k;i<n;i++){
			if(pan[i].second>bigest_r){
				long long po=pan[i].second*pan[i].second+pan[i].first;
				if(po>ma)
					ma=po;
			}
		}
		if(ma>bigest_r*bigest_r+pan[k-1].first)
			res=res+ma-pan[k-1].first;
		else
			res+=bigest_r*bigest_r;
		
		cout<<"Case #"<<tt<<": ";
		cout << std::fixed;
  		cout << std::setprecision(9);
		cout<<res*pi<<endl;
	}
	
    
    
    return 0;
}

