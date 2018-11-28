#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int times=0;times<t;times++){
		long long n,count;
		cin>>n;
		count=n;
		long long res=0,ans=0,ten=1;
		int nsize=0,firstnum=0,check=0;
		while(count!=0){
			nsize++;
			firstnum=count%10;
			count/=10;
		}
		
		for(int i=0;i<nsize;i++){
			res+=1*ten;
			ans+=firstnum*ten;
			ten*=10;
			//cout<<"res:"<<res<<endl;
		}
		check=firstnum;
		
		while(res>0){
			if(ans==n){
				break;
			}
			
			if(ans>n){
				if(ans-res>0){
					//cout<<ans<<endl;
					ans-=res;
					res/=10;
					check-=1;
				}
				else{
					ans=0;
					ten=1;
					for(int i=0;i<nsize-1;i++){
						ans+=9*ten;
						ten*=10;
					}
					break;
				}
			}
			else{
				if(ans+res<=n && check+1<=9){
					ans+=res;
					check+=1;
				}
				else{
					res/=10;
				}
			}
		}
		cout<<"Case #"<<times+1<<": "<<ans<<endl;
	}
	return 0;
}

