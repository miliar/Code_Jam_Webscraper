#include<bits/stdc++.h>
using namespace std;

inline bool check(unsigned long long int n){
    int cur = n%10;
    n/=10;
    while(n){
        int dig = n%10;
        if (cur < dig)
            return false;
        n=n/10;
        cur = dig;
    }
    return true;
}

int main(){
    int test;
    cin>>test;
    int y =test;
    while(test--){
        unsigned long long n;
        cin>>n;
        n++;
        while(n--){
            if (check(n) ==true){
                break;
            }
        }
        cout<<"Case #"<<y-test<<": "<<n<<endl;
    }

}
