#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<n;++i)

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    //string s;
    long long n,k;
    long long val;
    long long cur;
    pair<long long,long long> q;
    forn(i,t){
        map<long long,long long> a;
        cin>>n>>k;
        val = n;

        a[val] = 1;
        cur = 1;
        while(k>0){
            q = *a.rbegin();
            val = q.first;
            cur = q.second;
            a.erase(val);
            k-=cur;
            a[val/2]+=cur;
            a[(val-1)/2]+=cur;
/*
            cout<<a.size()<<'\n';
            for(auto it:a){
                cout<<it.first<<' '<<it.second<<'\n';
            }
*/
        }
        printf("Case #%d: ",i+1);
        cout<<val/2<<' '<<(val-1)/2<<'\n';
    }
}
