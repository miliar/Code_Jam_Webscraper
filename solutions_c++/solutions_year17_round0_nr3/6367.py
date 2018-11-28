#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() {
    long long n,k,t;
    cin >> t;
    
    for (int i = 1; i <= t; i++) {
        cout << "Case #"<<i<< ": ";  
        cin >> n>> k;
        vector<long long> n1c(1000), n2c(1000);
        long long l = 1, n1 = n, n2 = n, j = 0;

        n1c[0] = 0;
        n2c[0] = 1;
        //cout << l << " " << k << endl;
        for (; 2*l-1 < k; j++,l*=2) {

            if ((n2%2)==0) {
                n1c[j+1] = 2*n1c[j]+n2c[j];
                n2c[j+1] = n2c[j];
            }
            if ((n2%2)!=0) {
                n1c[j+1] = n1c[j];
                n2c[j+1] = n1c[j]+2*n2c[j];
            }
            n1 = n2/2-1;
            n2 = n2/2;
//            cout << n1 << " "<< n2 << " "<<n1c[j+1] <<" "<<n2c[j+1]<<endl; 

        }
        k -= l-1;
  //      cout << k << " " << j << endl;
        if (k > n2c[j]) 
            cout << n1/2 <<" "<<(n1-1)/2 << endl;
        else
            cout << n2/2 <<" "<<(n2-1)/2 << endl;
    }
        
    return 0;


}
