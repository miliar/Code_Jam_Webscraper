#include <iostream>
using namespace std;

bool checknd(long long int n) {
    int p = 0,c=0;
    p = n%10;
    while(n=n/10) {
        c = n%10;
        if (c>p) return true;
        p=c;
    }
    return false;
}
int main() {
    long long int val;
    int t;
    cin>>t;
    int i=0;
    while(i++ < t) {
        cin>>val;
        while(checknd(val)) {
            val--;
        }
        cout<<"Case #"<<i<<": "<<val<<endl;
    }
    return 0;
}
