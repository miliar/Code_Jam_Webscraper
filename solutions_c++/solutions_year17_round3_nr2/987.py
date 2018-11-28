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
    freopen("/Users/shitian/Desktop/gcj/gcj/B-small-attempt0.in","r",stdin);
    freopen("/Users/shitian/Desktop/gcj/gcj/B-small-attempt0.txt","w",stdout);
    
    int tcase;
    cin>>tcase;
    for(int tc=1;tc<=tcase;tc++){
        cout<<"Case #"<<tc<<": ";
        
        int ac,aj;
        cin>>ac>>aj;
        vector<pair<pair<int,int>,int> >tim(ac+aj);
        for(int i=0;i<ac;i++){
            cin>>tim[i].first.first>>tim[i].first.second;
            tim[i].second=0;
        }
        for(int i=0;i<aj;i++){
            cin>>tim[i].first.first>>tim[i].first.second;
            tim[i].second=1;
        }
        sort(tim.begin(),tim.end());
        if((ac==1&&aj==0)||(ac==0&&aj==1)||(ac==1&&aj==1)){
            cout<<2<<endl;
            continue;
        }
        if((tim[1].first.second-tim[0].first.first)<=720||(1440-tim[1].first.first+tim[0].first.second)<=720){
            cout<<2<<endl;
        } else {
            cout<<4<<endl;
        }
    }
}
