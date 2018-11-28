#include<iostream>
#define int long long


using namespace std;

bool ok(int n) {
    while(n>=10) {
        if(n%10 < (n/10)%10) return false;
        n/=10;
    }
    
    return true;
}

#undef int
int main(void) {
    #define int long long
    
    int T; cin >> T;
    int ca = 0;
    while(T--) {
        int n; cin >> n;
        while(!ok(n)) n--;
        cout << "Case #" << ++ca << ": " << n << endl;;
    }
    return 0;
}