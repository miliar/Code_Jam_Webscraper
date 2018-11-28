#include <iostream>
#include <algorithm>
#include <string>
#include <iostream>     // std::cout, std::fixed
#include <iomanip> 


using namespace std ;
#define PB push_back
#define MP make_pair
typedef unsigned long long int llu;
typedef long long int ll;

int main() {
     std::cout << std::fixed;
    llu t;
    cin >> t;
    
    for (llu num = 1; num <= t; num++) {
        cout << "Case #"<<num<<": ";
        int d, n, k[1005], s[1005];
        double mspeed = 1e99;

        cin >> d >> n;
        for (int i = 0; i < n; i++) {
            cin >> k[i]>>s[i];
            mspeed = min(mspeed, (1.0*d)/((d-k[i]*1.0)/(1.0*s[i]))) ;   
        }
        
        std::cout << std::setprecision(9)<< mspeed << endl;
           
    }
}
