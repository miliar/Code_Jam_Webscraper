#include<set>
#include<map>
#include<unordered_set>
#include<vector>
#include<array>
#include<string>
#include<iostream>
#include<queue>
#include<algorithm>
#include<string.h>
#include<math.h>
using namespace std;
typedef long long ll;
typedef long double ld;

#define FOR(i,n) for(int i=0;i<n;i++)

int main(){
    freopen("/Users/shitian/Desktop/gcj/gcj/A-large.in","r",stdin);
    freopen("/Users/shitian/Desktop/gcj/gcj/A-large.txt","w",stdout);
    
    int tcase;
    cin>>tcase;
    for(int tc=1;tc<=tcase;tc++){
        cout<<"Case #"<<tc<<": ";
        ll N,K;
        cin>>N>>K;
        vector<pair<ld,ld> >pan(N);
        for(int i=0;i<N;i++){
            cin>>pan[i].first>>pan[i].second;
            
        }
        sort(pan.begin(),pan.end(),greater<pair<ld,ld> >());
        ld ans=0;
        for(int i=0;i<N;i++){
            vector<ld>pirh2;
            for(int j=i+1;j<N;j++){
                pirh2.push_back(2*M_PI*pan[j].first*pan[j].second);
            }
            if(pirh2.size()<K-1)continue;
            sort(pirh2.begin(),pirh2.end(),greater<ld>());
            ld pir=0;
            for(int j=0;j<K-1;j++){
                pir+=pirh2[j];
            }
            pir+=M_PI*pan[i].first*pan[i].first+2*M_PI*pan[i].first*pan[i].second;
            ans=max(ans,pir);
        }
        printf("%.10Lf\n",ans);
    }
}
