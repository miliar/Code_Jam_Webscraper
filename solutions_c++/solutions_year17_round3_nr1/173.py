#include<bits/stdc++.h>
#define LL int64_t
using namespace std;

LL ar(LL radius, LL height) {
    return 2*radius*height;
}
LL circle(LL radius) {
    return radius*radius;
}
const long double PI = 3.141592653589793238L;

void f() {
    int n,k;
    cin>>n>>k;  
    vector<pair<LL,LL> > pan(n);
    for(int i=0;i<n;i++) cin>>pan[i].first>>pan[i].second;

    auto comp = [](pair<LL,LL>& a, pair<LL,LL>& b) {
        return ar(a.first,a.second) > ar(b.first,b.second);
    };
    LL best = 0;
    for(int i=0;i<n;i++) {
        LL area = circle(pan[i].first) + ar(pan[i].first,pan[i].second);
        vector<pair<LL,LL> > vec;
        for(int j=0;j<n;j++) {
            if(i==j) continue;
            if(pan[j].first <= pan[i].first) vec.push_back(pan[j]);
        }
        sort(vec.begin(),vec.end(),comp);
        if(vec.size()<k-1) continue;
        for(int j=0;j<k-1;j++) area += ar(vec[j].first,vec[j].second);
        best = max(best,area);
    }
    cout<<setprecision(30)<<(PI*best)<<endl;

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
