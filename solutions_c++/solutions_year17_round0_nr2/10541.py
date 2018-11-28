#include<bits/stdc++.h>
using namespace std;
#define MAX 1000
int checkinc(unsigned int x){
	int arr[MAX];
	unsigned int count=0;
	unsigned int i=0;
	while(x!=0){
		arr[i]=x%10;
		x=x/10;
		i++;
	}
	count=i;
	for(i=0;i<count-1;i++){
		if(arr[i]<arr[i+1]){
			return 0;
		}
	}
return 1;	
}
int main(){
	freopen("B-small-attempt3.in","r",stdin);
	freopen("B-small-attempt3.out","w",stdout);
	unsigned int n,ln;
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>n;
		if(n/10==0){
			ln = n;
		}
		else {
			if(checkinc(n)){
				ln = n;
			}
			else{
				for(int k=11;k<n;k++){
				if(checkinc(k)){
					ln=k;
				}
			}
			}
		}
		cout<<"Case #"<<i+1<<": "<<ln<<"\n";
	}
return 0;	
}
