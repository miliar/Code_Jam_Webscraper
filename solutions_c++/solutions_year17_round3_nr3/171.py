#include<bits/stdc++.h>
#define LL int64_t
#define LD long double
using namespace std;

bool canDo(vector<LD>& p, LD u, LD goal) {
    for(LD a : p) {
        if(a < goal) u -= (goal - a);
    }
    return u >= 0;
}

void f() {
    int n,k;
    cin>>n>>k;  
    LD u;
    vector<LD> p(n);
    cin>>u;
    for(int i=0;i<n;i++) cin>>p[i];

    LD low=0, high = 1;
    for(int i=0;i<1000;i++) {
        LD mid = (low+high)/2;
        if(canDo(p,u,mid)) low = mid;
        else high = mid;
    }
    
    LD succProb = 1;
    for(LD a : p) succProb *= max(a,(low+high)/2);
    cout<<setprecision(30)<<succProb<<endl;

}

int main() {
    ios::sync_with_stdio(false); cin.tie(0);

    int T;
    cin>>T;
    for(int i=1;i<=T;i++) {
        cout<<"Case #"<<i<<": ";
        f();
    }
}
