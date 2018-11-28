#include <iostream>  
#include <string>
#include<stack>

using namespace std;  


int main() {
    long long int t,n,k;
    cin >> t; 
    for (long long int i = 1; i <= t; ++i) {
        cin>>n;
        cin>>k;
        long long int n1 = k;
        long long int k1 = 2;
        while(n1/k1 != 0){
            k1 = k1*2;
        }
        k1 = k1/2;
    
        long long int m = ( n - k + k1 )/k1;
        long long int min = (m-1)/2;
        long long int max = m/2 ;
        cout << "Case #" << i << ": " << max << " "<<min<<endl;
    }
    return 0;
}
 