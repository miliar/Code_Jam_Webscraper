#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;
bool tid(long long int n){
	int prev=n%10;
	n/=10;
	while(n){
		if(n%10>prev) return 0;
		prev=n%10;
		n/=10;
		}
	return 1;
}
 main(){
 	long long int t,n,cas=0;
 	freopen("B-small-attempt3.in","r",stdin);
 	freopen("txt.out","w",stdout);
 	cin>>t;
 	while(t--){
 		cin>>n;
 		cout<<"Case #"<<++cas<<": ";
 		for(long long int i=n;i>=1;i--){
 			if(tid(i)){
 				cout<<i<<endl;
 				break;
 			}
 		}
 	}

}
