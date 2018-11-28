#include <iostream>
#define ull unsigned long long
using namespace std;


int main(){
	int t;
	ull n,k;
	cin>>t;
	for(int x=1;x<=t;x++){
		cin>>n>>k;
		bool busy[100000]={false};
		busy[0]=true;
		busy[n+1]=true;
		if(k==n){
			cout<<"Case #"<<x<<": "<<0<<" "<<0<<endl;
			continue;
		}
		if(k==1){
			if(n%2==0)
				cout<<"Case #"<<x<<": "<<n/2<<" "<<(n/2)-1<<endl;
			else
				cout<<"Case #"<<x<<": "<<n/2<<" "<<n/2<<endl;
			continue;
		}
		ull maxl=0,maxr=0,ind=1000000000;
		while(k--){
			maxl=0,maxr=0,ind=1000000000;
			for(ull i=1;i<=n;i++){
				if(!busy[i]){
					ull j=i-1,l=0,r=0;
					while(!busy[j--])
						l++;
					j=i+1;
					while(!busy[j++])
						r++;
					if(min(l,r)>min(maxl,maxr)){
						maxl=l;
						maxr=r;
						ind=i;
					}
					else if(min(l,r)==min(maxl,maxr)){
						if(max(l,r)>max(maxl,maxr)){
							maxl=l;
							maxr=r;
							ind=i;
						}
						else if(max(l,r)==max(maxl,maxr)){
							if(ind>i)
								ind=i;
						}
					}
				}
			}
			busy[ind]=true;
		}
		cout<<"Case #"<<x<<": "<<max(maxl,maxr)<<" "<<min(maxl,maxr)<<endl;
	}
	return 0;
}