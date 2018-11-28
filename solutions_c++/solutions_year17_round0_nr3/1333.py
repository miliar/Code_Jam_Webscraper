#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
    ios_base::sync_with_stdio(0);
    int T;
    cerr<<"------ start -----"<<endl;
    cin>>T;
    for(int t = 1; t <= T; ++t)
    {
        cerr<<"----- "<< t<<" ------"<<'\n';
        map<LL,LL> ma;
        LL n,k;
        cin>>n>>k;
        ma[n] = 1;

        pair<LL,LL> x;
        while(k>0LL)
        {
            auto it = ma.end();
            --it;
            x = *it;
            ma.erase(it);
            k -= x.second;
            ma[(x.first-1)/2] += x.second;
            ma[(x.first-1)/2+(x.first-1)%2] += x.second;
        }

        LL res = x.first-1;

        cout<<"Case #"<<t<<": "<<res/2+(res%2)<<' '<<res/2<<'\n';
    }
    cerr<<"------ done -----"<<endl;
    return 0;
}
