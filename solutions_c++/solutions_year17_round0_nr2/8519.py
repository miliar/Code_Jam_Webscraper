#include <bits/stdc++.h>
using namespace std;
int main() {
    int t,T,i;
    long long int ans,n;
	cin>>T;
	for(t=1;t<=T;t++)
	{
	    cin>>n;
	    int l=(int)(log10(n));
	    if(l==0){
	        printf("Case #%d: %lld\n",t,n);
	        continue;
	    }
	    int dig[l+2];
	    i=0;
	    ans=n;
	    while(n>0){
	        dig[i++]=n%10;
	        n/=10;
	    }
	    i--;
	    l=i;
	    int flip=l;
	    int flag=0;
	    while(i>0){
	        if(dig[i]>dig[i-1]){flag++;break;}
	        if(dig[i]<dig[i-1])flip=i-1;
	        i--;
	    }
	    if(((flip!=i)||(flip==0)) && flag==0){
	        printf("Case #%d: %lld\n",t,ans);
	        continue;
	    }
	    dig[flip]--;
	    flip--;
	    while(flip>=0){
	        dig[flip]=9;
	        flip--;
	    }
	    ans=0;
	    i=0;
	    while(i<=l){
	        ans+=dig[i]*pow(10,i);
	        i++;
	    }
	    printf("Case #%d: %lld\n",t,ans);
	}
	return 0;
}

