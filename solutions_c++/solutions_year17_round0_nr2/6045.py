#include <iostream>
#include <string.h>
using namespace std;

int main() {
	unsigned long long n, num, rem1, rem2;
	int step, t, i ,j, k, temp;
	cin >> t;
	for ( i=1; i<=t; i++) {
	    cin >> num;
	    n=num;
	    step=1;
	    while(n>9){
	        rem1=n%10;
	        n=n/10;
	        rem2=n%10;
	        if( rem2>rem1){
	            for(j=0;j<step;j++) {
	                n=n*10;
	            }
	            if(rem2!=0) {
	            n=n-1;
	            num=n;
	            }
	            else { temp=1;
	                for(k=0;k<step;k++){
	                   temp=(temp*10);
	                   
	                }
	                temp++;
	               n=n-temp;
	               num=n;
	            }
	            for(j=0;j<step;j++) {
	                n=n/10;
	            }
	            
	            }
	         
	            step++;
	            }
	            cout << "Case #" << i << ": " << num << endl;
	        }
	    }
	
