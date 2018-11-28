#include<bits/stdc++.h>

#define INF 9223372036854775807
#define mod 1000000007
#define ep 0.000000001
#define ll  long long int
#define ld double
#define endl '\n'
#define sz 2005
#define pi 3.141592653589
#define fast() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

using namespace std;

ll g,b;
typedef pair<ll,ll> pii;
vector <pii> v;

int main(){
    ll i,j,t,x,y;
    fast();
    cin>>t;
    for(j = 1; j <= t; j++){
        cin>>g>>b;
        v.clear();
        for(i = 0; i < g+b; i++){
            cin>>x>>y;
            v.push_back(make_pair(x,y));
        }
        cout<<"Case #"<<j<<": ";
        if(g == 1 && b ==0){
            cout<<2<<endl;
        }
        else if(g == 0 && b == 1){
            cout<<2<<endl;
        }
        else if(g == 1 && b== 1){
            cout<<2<<endl;
        }
        else if(g == 2 && b == 0){
            sort(v.begin(),v.end());
            if(v[1].second - v[0].first <= 720)
                cout<<2<<endl;
            else if(v[1].first - v[0].second >= 720)
                cout<<2<<endl;
            else
                cout<<4<<endl;
        }
        else if(g == 0 && b == 2){
            sort(v.begin(),v.end());
            if(v[1].second - v[0].first <= 720)
                cout<<2<<endl;
            else if(v[1].first - v[0].second >= 720)
                cout<<2<<endl;
            else
                cout<<4<<endl;
        }
    }
    return 0;
}
