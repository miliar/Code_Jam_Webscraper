#include <iostream>  
#include <cstdio>
#include <sstream>

using namespace std; 

bool check(long long int n)
{
    int prev = n%10;
    n = n/10;
    while (n)
    {
        int curr = n%10;
        if (curr > prev)
            return false;
        prev = curr;
        n = n/10;
    }
 
    return true;
}
 

int main(void){
	int t; 
	cin >> t; 
	for(int c =1;c<=t;c++){
		long long int k; 
		cin  >> k; 
		if(k < 10){
			cout << "Case #" << c << ": " << k << endl;
		}else{
			long long int i=0;
			for( i= k; i>0 ; i--){
				bool l = check(i); 
				if(l == true ){
					cout << "Case #" << c << ": " << i << endl;
					break;
				}
			}
		}
	}
	return 0;
	
}