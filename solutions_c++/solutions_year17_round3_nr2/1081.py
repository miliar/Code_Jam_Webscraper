#include<bits/stdc++.h>
using namespace std;
vector<pair<int,int>>v,w;
int main(){
    ios_base::sync_with_stdio(0);
    int tc,cc,ac,aj,i,x,y;
    cin>>tc;
    for(cc=1;cc<=tc;++cc){
        cin>>ac>>aj;
        for(i=0;i<ac;++i){
            cin>>x>>y;
            v.emplace_back(x,y);
        }
        for(i=0;i<aj;++i){
            cin>>x>>y;
            w.emplace_back(x,y);
        }
        if(v.size())sort(v.begin(),v.end());
        if(w.size())sort(w.begin(),w.end());
        cout<<"Case #"<<cc<<": ";
        if(v.empty()){
            if(w.size()==1)cout<<"2\n";
            else if(w[0].first+720>=w[1].second||w[0].second+1440-w[1].first<=720)cout<<"2\n";
            else cout<<"4\n";
        }
        else if(v.size()==1)cout<<"2\n";
        else if(v[0].first+720>=v[1].second||v[0].second+1440-v[1].first<=720)cout<<"2\n";
        else cout<<"4\n";
        v.clear();
        w.clear();
    }
    return 0;
}
