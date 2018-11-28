#include <iostream>

using namespace std;

bool checkTidy(uint64_t n){
    uint64_t ld = n % 10;
    n = n / 10;
    while(n > 0){
        uint64_t sld = n % 10;
        n = n / 10;
        if(ld >= sld){
            ld = sld;
            continue;
        }
        else
            return false;
    }
    return true;
}

int main() {
    int t,i = 1;
    cin>>t;
    uint64_t n;
    while(t--){
        cin>>n;
        while (!checkTidy(n)){
            n = n - 1;
        }
        cout<<"Case #" << i << ":" << " " << n <<endl;
        i++;
    }
    return 0;
}