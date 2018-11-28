// 
#include "bits/stdc++.h"
#define ll long long
using namespace std;
const int N=1e5+1;
int main(){
     int t;
     cin>>t;
     int r=1;
     while(t--){
		long long n;
		cin>>n;
		long long res=0;
		long long cur=9;
		long long base=1;
		while(n>0){
			if(cur>=(n%10)){
			   cur=n%10;
			   res=res+((n%10)*base);
			}
			else{
			   cur=(n%10)-1;
			   res=(base-1)+(cur)*base;
			}
			n/=10;
			base=base*10;
		}
		cout<<"Case #"<<r++<<": "<<res<<endl;
	 }
return 0;
}

