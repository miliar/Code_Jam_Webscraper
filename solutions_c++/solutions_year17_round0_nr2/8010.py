#include <bits/stdc++.h>
#define ll long long
using namespace std;

int T;
ll N;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for(int t=1;t<=T;++t){
        vector<int> v;
        ll n=0;
        cin>>N;
        while(N>0){
            v.push_back(N%10);
            N/=10;
        }
        v.push_back(0);
        for(int i=v.size()-2;i>0;--i)
            if(v[i]>v[i-1]){
                --v[i];
                for(int j=i+1;v[j]>v[j-1];++j){
                    --v[j];
                    v[j-1]=9;
                }
                while(--i>=0)
                    v[i]=9;
            }
        for(int i=v.size()-1;i>=0;--i){
            n*=10;
            n+=v[i];
        }
        printf("Case #%d: %lld\n",t,n);
    }
}
