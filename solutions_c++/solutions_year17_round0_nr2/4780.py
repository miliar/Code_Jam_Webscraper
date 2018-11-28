#include<iostream>

#include <inttypes.h>
#include<cmath>
using namespace std;
typedef uint64_t lng;
lng v;
lng* ref= &v;  
uint64_t istidy(uint64_t n){
	uint64_t last = n%10,curr,l;
	bool ret = true;
	uint64_t m=n , sub=0;
	while(n>0){
		
		curr = n%10;
		if(last < curr){
			ret = false;
			*ref = n;
			break;
		}
		n/=10;
		last = curr;
	}
	if(ret == true){
		return 0;
	}else{
		l= 0;
		n=m;
		while(n>0){
			n/=10;
			l++;
		}
		sub = *ref;
		while(sub>0){
			sub/=10;
			l--;
		}
		sub = *ref;
		return (1+m-sub*((uint64_t)pow(10,l)));
	}
}
int main(){
	int t;
	cin>>t;
	for(int x=1;x<=t;x++){
		cout<<"Case #"<<x<<": ";
		uint64_t n,p;
		cin>>n;
		bool y=true;
		bool* y_ref = &y;
		for(uint64_t i=n;(*y_ref);){
			p=istidy(i);			
			if(p==0){
				cout<<i;
				(*y_ref) = false;
				break;
			}
			i-=p;
		}
		
		cout<<endl;
	}
	return 0;
}

