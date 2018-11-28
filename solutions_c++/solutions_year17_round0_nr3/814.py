#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
	int caso;
	cin>>caso;
	
	for(int testcases=1;testcases<=caso;testcases++){
		cout<<"Case #"<<testcases<<": ";
		long long n,k;
		cin>>n>>k;
		
		long long it=1;
		long long a=1;
		long long b=0;
		long long ans=-1;
		
		while(true){
			if(it+a-1>=k){ans=n;break;}
			if(it+a+b-1>=k){ans=n-1;break;}
			if(n%2==0){
				it=it+a+b;
				b=a+2*b;
			}else{
				it=it+a+b;
				a=2*a+b;
			}
			
			n=n/2;
		}
		
		ans--;
		cout<<ans-ans/2<<" "<<ans/2<<endl;
	}
	
	
	
	return 0;
}
