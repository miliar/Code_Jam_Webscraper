#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	ll t,n;
	cin>>t;
	for(int z=1;z<=t;z++){
		cin>>n;
		int ans=0;
		if (n<10) {
			ans=n;
		}
		else{
			for(int i=n;i>0;i--){
				int temp=i;
				int temp2=i%10;
				int flag=1;
				temp/=10;
				while(temp!=0){
				//	printf("temp %d i %d temp2 %d\n",temp,i,temp2);
					if (temp2<temp%10) {
						flag=0;
						break;
					}
					temp2=temp%10;
					temp/=10;
				}
				if (flag==1) ans=i;
				if (ans) break;
			}
		}
		printf("Case #%d: %d\n",z,ans);
	}
		
	
	return 0;
}

