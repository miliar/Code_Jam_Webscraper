#include <iostream>
#include<stdio.h>
using namespace std;
typedef long long unsigned int ll;
ll t,n,k,max1,min1,max2,min2,temp,tempn_d,newn,tempk;
int n_d;
ll gen(int d){
    ll num=0;
    while(d--){
        num=num<<1;
        num = num|1LL;
    }
    return num;
}
int main() {
	// your code goes here
	scanf("%llu",&t);
	int cs=0;
	while(t--){
	    cs++;
	    scanf("%llu %llu",&n,&k);
	    n_d=0;
	    tempk=k;
	    while(k>0){
	        n_d++;
	        k=k>>1;
	    }
	    temp=n;
	    tempn_d=n_d;
	    while(n_d--){
	        if(temp&1LL){
	            max1=temp>>1;
	            max2=max1;
	            min1=max1;
	            min2=min1-1;
	        }
	        else{
	            max1=temp>>1;
	            max2=max1-1;
	            min1=max2;
	            min2=min1;
	        }
	        temp=temp>>1;
	    }
	    n_d=tempn_d;
	    n_d--;
	    newn = n^gen(n_d);
	    newn = newn & gen(n_d);
	   // cout<<k<<endl;
	    if(n_d==0)
	    std::cout << "Case #"<< cs << ": " << max1 << " " << min1 << std::endl;
	    else if(tempk<=(gen(tempn_d)-newn))
	    std::cout << "Case #"<< cs << ": " << max1 << " " << min1 << std::endl;
	    else
	    std::cout << "Case #"<< cs << ": " << max2 << " " << min2 << std::endl;
	}
	return 0;
}

