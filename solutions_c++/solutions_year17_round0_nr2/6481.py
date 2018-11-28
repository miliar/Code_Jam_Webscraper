#include <iostream>
#include <string>
#include <math.h>
using namespace std;

typedef long long int ll;

bool ok(ll num){
	string buf = to_string(num);
	int l = buf.length();
	for(int i = 1; i<l; i++){
		if (buf[i]<buf[i-1]) return false;
	}
	return true;
}

int main(){
	int t;
	ll n,ans;
	string buf;
	scanf("%d\n", &t);
	for (int _=1; _<=t; _++){
		
		getline(cin,buf);
		int l = buf.length();
		ans = 0ll;
		bool borrow = false;
		bool decreased = false;
		for(int i = 1; i<l; i++){
			if (buf[i]<buf[i-1]){
				buf[i] = '9';
				if (!decreased){
					decreased = true;
					if(buf[i-1]=='0'){
						buf[i-1] = '9';
						borrow = true;
					}else{
						buf[i-1] = (char)((int)buf[i-1]-1);
					}
					for (int j=i-2; j>=0; j--){
						if (borrow){
							if (buf[j]=='0'){
								buf[j] = '9';
							}else{
								buf[j] = (char)((int)buf[j]-1);
								borrow = false;
							}
						}
						if (buf[j]>buf[j+1]){
							buf[j+1] = '9';
							if (buf[j]=='0'){
								buf[j] = '9';
								borrow = true;
							}else{
								buf[j] = (char)((int)buf[j]-1);
							}
						}
					}
				}

			}
			
			
		}
		for (int k=0; k<l; k++) 			ans += ((int)buf[k]-48) * (ll)pow(10,l-k-1);
		printf("Case #%d: %lld\n", _, ans); 
	}
}