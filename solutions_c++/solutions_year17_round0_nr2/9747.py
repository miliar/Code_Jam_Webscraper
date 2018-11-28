#include <iostream>
#include<string.h>
using namespace std;

int main() {
	int test=0;
	cin>>test;
	for(int n =1;n<=test;n++){
	    long int a=0,rq=0;
	    int lb=0;
	    long int c=0;
	    int mb=0;
	    cin>>a;
	    while(a>0){
	        lb=a%10;
	        mb=(a/10)%10;
	        a=a/10;
	        c++;
	        if(mb>lb){
	            int j=c;
	            rq=0;
	            while(j>0){
	                rq=(rq*10)+9;
	                j--;
	            }
	            --a;
	        }
	        else
	        if(lb>=mb){
	            rq=rq*10+lb;
	        }
	    }
	    c=0;
	    while(rq>0){
	        c=(c*10)+(rq%10);
	        rq/=10;
	    }
	    
	cout<<"Case #"<<n<<": "<<c<<endl;
	}
	return 0;
}
