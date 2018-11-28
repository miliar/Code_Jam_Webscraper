#include <iostream>
#include <cstdio>
#include <map>
using namespace std;
map<long long,long long> box;

pair<long long,long long> calc(long long n,long long k) {
    box.clear();
    box[n] = 1;
    map<long long,long long>::reverse_iterator it;
    long long tmp1, tmp2, tmp;
    while(1) {
        it = box.rbegin();
        tmp1 = (it->first-1)/2;
        tmp2 = it->first/2;
        tmp = it->second;
        if(k <= it->second) {
            return make_pair(tmp1, tmp2);
        } else {
            k -= it->second;
            if(box.count(tmp1) == 0) box[tmp1] = tmp; else box[tmp1] += tmp;
            if(box.count(tmp2) == 0) box[tmp2] = tmp; else box[tmp2] += tmp;
            box.erase(it->first);
        }
    }
}

int main(){
    freopen("input.txt","r",stdin);
    int T;
    long long n,k;
    cin>>T;
    pair<long long,long long> ans;
    for(int i=1;i<=T;i++){
        cin>>n>>k;
        ans = calc(n,k);
        cout<<"Case #"<<i<<": "<<ans.second<<" "<<ans.first<<" "<<endl;
    }
}