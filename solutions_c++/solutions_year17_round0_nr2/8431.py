#include <iostream>
using namespace std;

int main() {
    int test;
    cin>>test;
    int all = test, sum1 = 0 , sum= 0;
    while(test--) {
        long long int num , m , i;
        cin>>num;
        m = num;
        for( i = num ; i >= 0 ; i--) {
            m = i;
            sum = 0;
            sum1 = 0;
            while(m) {
                int rem1 , rem2;
                rem1 = m%10;
                m/=10;
                rem2 = m%10;
                if(rem1 >= rem2) {
                    sum++;
                }
                sum1++;
            }
            if(sum == sum1) {
                cout<<"Case #"<<all-test<<": "<<i<<endl;
                break;
            }
        }
    }
    
    return 0;
}

