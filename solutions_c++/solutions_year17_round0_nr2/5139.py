#include <bits/stdc++.h>
using namespace std;

long long n;
int k,t,a[20],b[20],pare;

int main(){
	int m=1;
	cin >> t;
	while(t--){
		int i=0;
		cin >> n;
		while(n!=0){
			b[i] = n%10;
			n/=10;
			i++;
		}
		i--;
		for(int j=0;j<=i;j++) a[j] = b[i-j];
		while(true){
			for(int j=0;j<=i-1;j++){
				if(a[j]<=a[j+1]) pare=1;
				else if(a[j]>a[j+1]){
					a[j]--;
					for(int l=j+1;l<=i;l++) a[l]=9;
					pare=0;
					break;
				}
			}
			if(pare){break;}		
		}
		a[0]==0 ? k=1 : k=0;
		printf("Case #%d: ",m);
		for(int j=k;j<=i;j++) printf("%d",a[j]);
		printf("\n");
		m++;
	}
}