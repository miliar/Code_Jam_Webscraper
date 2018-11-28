#include <bits/stdc++.h>
using namespace std;
#define ll long long
char a[25],b[25];
int main(){
	int t,tt,n,i,j,k;
	ll v,w;
	cin >> t;
	for(tt=1;tt<=t;tt++){
		scanf(" %s",a);
		n=strlen(a);
		for(k=0;k<25;k++){
			for(i=1;i<n;i++){
				if(a[i]<a[i-1]){
					if(a[i-1]>'1'){
						a[i-1]--;
						for(j=i;j<n;j++)
							a[j]='9';
					}
					else{
						a[0]='0';
						for(j=1;j<n;j++)
							a[j]='9';
					}
					break;
				}
			}
		}
		sscanf(a,"%lld",&v);
		printf("Case #%d: %lld\n",tt,v);
	}
}