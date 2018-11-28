#include<bits/stdc++.h>
using namespace std;

# define PI           3.14159265358979323846  /* pi */

typedef long long ll;

bool cmp(const pair<ll,ll> &a, const pair<ll,ll> &b){
    return a.first*a.second<b.first*b.second;
}


void _main()
{
    int N,K;
    cin>>N>>K;
    vector<pair<ll,ll>> vec;
    for(int i=0;i<N;i++){
        ll R,H;
        cin>>R>>H;
        vec.push_back({R,H});
    }
    sort(vec.begin(),vec.end());
    ll ans=-1;
    for(int i=N-1;i>=K-1;i--){
        ll temp=vec[i].first*vec[i].first+2*vec[i].first*vec[i].second;
        //cout<<vec[i].first<<","<<vec[i].second<<" ";
        vector<pair<ll,ll>> tempVec;
        for(int k=i-1;k>=0;k--)
            tempVec.push_back({vec[k].second,vec[k].first});
        sort(tempVec.begin(),tempVec.end(),cmp);
        reverse(tempVec.begin(),tempVec.end());
        for(int j=0;j<K-1;j++){
            temp+=2*tempVec[j].first*tempVec[j].second;
            //cout<<tempVec[j].first<<","<<tempVec[j].second<<" ";
        }
        //cout<<endl;
        tempVec.clear();
        ans=max(temp,ans);
    }
    double ans2=double(ans)*PI;
    printf("%.9f",ans2);
}

int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        _main();
        cout<<endl;
    }
}
