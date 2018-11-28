#include <iostream>
using namespace std;

long long check (long long n){
	long long p=n%10;
	long long c=(n/10)%10;
	if(c>p)
		return 0;
	else {
		while (c<=p){
			n/=10;
			if(n<10)
				break;
			p=n%10;
			c=(n/10)%10;
		}
		if(c>p)
			return 0;
		else
			return 1;
	}
}
int main() {
    long long i,t,n[1000],r[1000];
    cin>>t;
    for(i=0;i<t;i++)
    	cin>>n[i];
    for(i=0;i<t;i++)
    {
    	if(n[i]<10) { 
    		r[i]=n[i];
    		continue;
    	}
    	else if(n[i]==10){
    		r[i]=9;
    		continue;
    	}
    	else {
    		long long nt=n[i];
    		while(!check(nt)){
    			nt--;
    			if(nt<=10){
    				if(nt<10) r[i]=nt;
    				else r[i]=9;
    				break;
    			}
    		}
    		if(nt>10 && check(nt))
    			r[i]=nt;
    	}
    }
    for(i=0;i<t;i++){
    	cout<<"Case #"<<i+1<<": "<<r[i]<<"\n";
    }
	return 0;
}