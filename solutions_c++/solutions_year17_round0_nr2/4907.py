#include <bits/stdc++.h>
using namespace std;

#define int long long

int power(int base, int power)
{
    int ret =1;
    for(int i=1; i<=power; i++) {
        ret*=base;
    }
    return ret;
}

vector<int> get(int n)
{
    vector<int> s;
    while(n!=0) {
        s.push_back(n%10);
        n/=10;
    }
    return s;
}

int func_2(int n)
{
    if(n<10) return n;
    vector<int> v=get(n);
    for(int i=0; i<v.size()-2; i++) {
        if(v[i]<v[i+1]) {
            v[i+1]--;
            for(int j=0; j<=i; j++) v[j]=9;
        }
    }
    if(v[v.size()-1]>v[v.size()-2]) {
        for(int i=0; i<v.size()-1; i++) {
            v[i]=9;
        }
        v[v.size()-1]--;
    }
    int ret=0;
    for(int i=0; i<v.size(); i++) {
        ret+=(v[i]*power(10, i));
    }
    return ret;
}

int32_t main ()
{
    freopen("sub-4.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cs; cin>>cs;
    for(int t=1; t<=cs; t++) {
        int n;
        cin>>n;
        int ans=func_2(n);
        printf("Case #%lld: %lld\n", t, ans);
    }
    return 0;
}
