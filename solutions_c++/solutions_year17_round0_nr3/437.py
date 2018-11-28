#include<bits/stdc++.h>
using namespace std;

void f() {
    int64_t n, k;
    cin>>n>>k;
    map<int64_t,int64_t> m;
    m[n] = 1;

    while(k) {
        auto p = *m.rbegin();
        int64_t gap = p.first;
        int64_t count = p.second;

        m.erase(gap);
        gap--;
        int64_t l = gap/2;
        int64_t r = gap - l;

        if(k<=count) {
            cout<<max(l,r)<<" "<<min(l,r)<<endl;
            return;
        }
        k -= count;
        
        if(l) m[l] += count;
        if(r) m[r] += count;


    }
}

int main() {
    int t;
    cin>>t;
    for(int i=1;i<=t;i++) {
        cout<<"Case #"<<i<<": ";
        f();

    }
}
