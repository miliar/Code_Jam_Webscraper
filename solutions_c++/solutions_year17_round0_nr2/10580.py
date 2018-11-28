#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int i=0;i<t;i++){
		bool b;
		bool bb;
		b=true;
		bb=true;
		char c[20];
		ll m,n;
		cin >> c;
		if(strlen(c)==1) printf("Case #%d: %s\n",i+1,c);
		else{
			for(int j=0;j<strlen(c)-1;j++){
				if(c[j]>c[j+1]){
					m=j+1;
					b=false;
					if(c[j]==c[j-1]){
						m=j;
						bb=false;
					}
					break;
				}
			}
			if(!b){
				for(int j=m;j<strlen(c);j++){
					c[j]='0';
				}
			}
			n=atoi(c);
			if(!b) printf("Case #%d: %d\n",i+1,n-1);
			else printf("Case #%d: %d\n",i+1,n);
		}
	}
	return 0;
}
