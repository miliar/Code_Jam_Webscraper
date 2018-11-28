#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<utility>
#include<iomanip>
using namespace std;
const long double PI = 3.141592653589793238L;
long long T,N,K;
pair<long long,long long> x[1000];
long long h[1000],r[1000];
vector< pair<long long,long long> > t;
long long solve(){
    t.clear();
    sort(x,x+N);
    long long ret=0;
    for(long long i=0;i<K;i++){
        pair<long long,long long> tt(x[i].second , x[i].first);
        t.push_back(tt);
        //cout<<i<<":"<<tt.first<<' '<<tt.second<<endl;
    }
    for(long long i=K;i<N;i++){
        long long delta=x[i].second + x[i].first - t[K-1].second;
        long long mint = 0;
        for(long long j=1;j<t.size();++j)
            if(t[j].first < t[mint].first)
                mint = j;
        delta -= t[mint].first;
        if(delta>0){
            t.erase(t.begin()+mint);
            pair<long long,long long> tt(x[i].second,x[i].first);
            t.push_back(tt);
        }
    }
    for(long long i=0;i<K;i++){
        ret+= t[i].first;
        //cout<<t[i].first<<' ';
    }
    //cout<<endl<<t[K-1].second<<endl;
    ret+=t[K-1].second;
    return ret;
}
int main(){
    cin>>T;
    for(long long _c=1;_c<=T ; _c++){
        //Input
        cin >> N>>K;
        for(long long i=0;i<N;i++){
           long long r;
           cin>>r;
           long long h;
           cin>>h;
           x[i].first=r*r;
           x[i].second=2*r*h;
           //cout<<x[i].first<<' '<<x[i].second<<endl;
        }
        long long s=solve();
        cout<<setprecision(9)<<fixed<<setprecision(9);
        cout<<"Case #"<<_c<<": "<<(long double)s*PI<<endl;

    }
}
