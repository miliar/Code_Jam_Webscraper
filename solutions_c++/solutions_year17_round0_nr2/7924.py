#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

bool valid(unsigned long long n) {
    int g = 10;
    while (n != 0) {
        int d = n%10;
        n /= 10;
        if (d > g) return false;
        g = d;
    }
    
    return true;
}

unsigned long long addNine(unsigned long long r, unsigned long long n) {
    while (r*10 + 9 <= n) {
        r = r*10 + 9;
    }
    
    return r;
}

unsigned long long solved(unsigned long long n) {
    int a[100];
    int l = 0;
    unsigned long long r = 0;
    unsigned long long tmp = n;
    
    while (n != 0) {
        a[l++] = n% 10;
        n /= 10;
    }
    
    n = tmp;
    r = a[l-1];
    int d = a[l-1];
    for (int i = l - 2; i >= 0; --i) {
        if (d > a[i]) {
            --r;
            break;
        } else {
            r = r*10 + a[i];
            d = a[i];
        }
    }
    
    r = addNine(r, n);
    return r;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("/Users/ZALORA/Documents/facebook/facebook/input.txt","r", stdin);
    freopen("/Users/ZALORA/Documents/facebook/facebook/output.txt","w", stdout);
#endif
    
    int t;
    unsigned long long n;
    
    cin>>t;
    for (int test = 1; test <= t; ++test) {
        cin>>n;
        
        cout<<"Case #"<<test<<": ";
        
        unsigned long long tmp = n;
        while (valid(tmp) == false) {
            tmp = solved(tmp);
        }
        
        unsigned long long r = addNine(0ll, n);
        if (tmp > r) cout<<tmp;
        else cout<<r;
        
        cout<<endl;
    }
    
    return 0;
}
