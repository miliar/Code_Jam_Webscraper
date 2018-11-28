#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define all(v) v.begin(),v.end()
#define mp make_pair
#define ff first
#define ss second
#define MAX  1e6+5;
using namespace std;
ll n;
string func(const vector<vector<ll> >&vv,map<ll,char>m,vector<ll>v){

    bool flag=1;
    string s;
    ll p=0;
    ll ma=0;
    for(ll j=0;j<6;j+=2){
        if(v[j]>ma){
            ma=v[j];
            p=j;
        }
    }
    if(ma==0){
        flag=0;
    }
    v[p]--;
    ll ss=p;
    s+=m[p];
    ll pp;
    //cout<<"p="<<p<<" "<<ma<<endl;
    for(ll j=1;j<n&&flag;j++){
        ma=0;
        ll l=vv[p].size();
        for(ll k=0;k<l;k++){
            //cout<<vv[p][k]<<" "<<v[vv[p][k]]<<endl;
            if(v[vv[p][k]]>0&&vv[p][k]%2){
                ma=v[vv[p][k]];
                pp=vv[p][k];
                break;
            }
            if(v[vv[p][k]]>ma){
                ma=v[vv[p][k]];
                pp=vv[p][k];
                //cout<<pp<<" "<<ma<<endl;
            }
        }
        if(ma==0){
            flag=0;
            break;
        }
        p=pp;
        v[p]--;
        s+=m[p];
       //cout<<"p="<<p<<" "<<ma<<endl;
    }
    ll ee=p;
    if(find(all(vv[ee]),ss)==vv[ee].end()||find(all(vv[ss]),ee)==vv[ss].end())
        flag=0;
    if(flag==0){
        s="IMPOSSIBLE";
    }
    //cout<<s<<endl;
    return s;
}



int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll t;
    cin>>t;
    map<ll,char>m;
    vector<vector<ll> >vv(6);
    vv[0].pb(2);vv[0].pb(3);vv[0].pb(4);
    vv[2].pb(0);vv[2].pb(4);vv[2].pb(5);
    vv[4].pb(0);vv[4].pb(1);vv[4].pb(2);
    vv[1].pb(4);
    vv[3].pb(0);
    vv[5].pb(2);
    m[0]='R';m[1]='O';m[2]='Y';m[3]='G';m[4]='B';m[5]='V';
    for(ll i=0;i<t;i++){
        cout<<"Case #"<<i+1<<": ";
        //cout<<"test"<<i<<endl;
        cin>>n;
        vector<ll>v(6,0);
        for(ll j=0;j<6;j++){
            cin>>v[j];
        }
        string s=func(vv,m,v);
        if(s=="IMPOSSIBLE"){
            reverse(all(vv[0]));
            s=func(vv,m,v);
            reverse(all(vv[0]));
        }
        if(s=="IMPOSSIBLE"){
            reverse(all(vv[2]));
            s=func(vv,m,v);
            reverse(all(vv[2]));
        }
        if(s=="IMPOSSIBLE"){
            reverse(all(vv[4]));
            s=func(vv,m,v);
            reverse(all(vv[4]));
        }
        if(s=="IMPOSSIBLE"){
            reverse(all(vv[0]));
            reverse(all(vv[2]));
            s=func(vv,m,v);
            reverse(all(vv[0]));
            reverse(all(vv[2]));
        }
        if(s=="IMPOSSIBLE"){
            reverse(all(vv[0]));
            reverse(all(vv[4]));
            s=func(vv,m,v);
            reverse(all(vv[0]));
            reverse(all(vv[4]));
        }
        if(s=="IMPOSSIBLE"){
            reverse(all(vv[2]));
            reverse(all(vv[4]));
            s=func(vv,m,v);
            reverse(all(vv[2]));
            reverse(all(vv[4]));
        }
        if(s=="IMPOSSIBLE"){
            reverse(all(vv[0]));
            reverse(all(vv[2]));
            reverse(all(vv[4]));
            s=func(vv,m,v);
            reverse(all(vv[0]));
            reverse(all(vv[2]));
            reverse(all(vv[4]));
        }
        cout<<s<<endl;


    }


    return 0;
}

