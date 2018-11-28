#include <bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,i,n,k,u=1;
	cin>>t;
	while(t--){
	cin>>n;
	for(i=n;i>=1;i--){
        k=i;
        while((k%10>=(k%100)/10)&&k>0){
            k/=10;
        }
        if(k==0){break;}
	}
	cout<<"Case #"<<u<<": "<<i<<endl;
	u++;
	}

return 0;
}
