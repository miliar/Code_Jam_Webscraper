#include <bits/stdc++.h>
using namespace std;

int T,N,K;
int main(){
    cin>>T;
    for(int t=1;t<=T;t++){
        cin>>N>>K;
        map<int, int> seg;
        seg[N] = 1;
        int l, c;
        while(K > 0){
            l = seg.rbegin()->first;
            c = seg.rbegin()->second;
            seg.erase(l);
            K -= c;
            seg[(l-1)/2] += c;
            seg[l/2] += c;
        }
        cout<<"Case #"<<t<<": "<<l/2<<" "<<(l-1)/2<<"\n";
    }
    return 0;
}
