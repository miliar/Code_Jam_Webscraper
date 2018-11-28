#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    int cases= 0;
    while(T--){
        cases++;
        long long n,k;
        cin>>n>>k;
        map<long long,long long> tocal;
        tocal[-n]++;
        auto it=tocal.begin();
        while(it!=tocal.end()){
            long long cur=-it->first;
            long long add1=cur/2;
            long long add2=(cur-1)/2;
            tocal[-add1]+=it->second;
            tocal[-add2]+=it->second;
            it++;
        }
        long long last=0;
        it=tocal.begin();
        while(k>0){
            k-=it->second;
            last=-it->first;
            it++;
        }
        cout<<"Case #"<<cases<<": "<<last/2<<" "<<(last-1)/2<<"\n";
    }
    return 0;
}

