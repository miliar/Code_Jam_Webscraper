#include<iostream>

using namespace std;

long long is_ok(long long a) {
    long long rem, last, ret=0, ten=1;
    rem = a%10l;
    last=10l;
    while (rem <= last && a>0) {
        a/=10l;
        last=rem;
        rem=a%10l;
        if(last != 10)
            ret+=ten*last;
        ten=ten*10l;
    }
    if(a>0) {
        return ret+1;
    }
    return 0;
}

int main() {
    int T; cin >> T;
    for(int t=1; t<=T; t++) {
        long long i; cin>>i;
        long long ok=is_ok(i);
        while(ok) {
            i = i-ok;
            ok = is_ok(i);
        }
        cout << "Case #" << t << ": " << i << "\n";
    }
}
