#include<bits/stdc++.h>
#define ll long long
#define mp make_pair
#define vll vector<long long>
#define pll pair<long long, long long>
#define pb push_back
#define cd complex<double>
#define x first
#define y second
#define ld long double
#define epsilon 0.0000000000001
using namespace std;
int main(){
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    ios_base::sync_with_stdio(false);
    int t,cases,n,p,i,j;
    ll aux, k, in, su;
    cases=0;
    cin>>t;
    while(t--){
        cases++;
        cin>>n>>p;
        vll v;
        vector<pll> c[n];
        for(i=0;i<n;i++){
            cin>>aux;
            v.pb(aux);
        }
        bool coso = false;
        for(i=0;i<n;i++){
            for(j=0;j<p;j++){
                cin>>aux;
                //cout<<(0.9 * (ld)(v[i]))<<endl;
                su = floor((ld)(aux)/(0.9 * (ld)(v[i])) + epsilon);
                in = ceil((ld)(aux)/(1.1 * (ld)(v[i])) - epsilon);
                //cout<<in<<" - "<<su<<endl;
                if(in<=su){
                    c[i].pb(mp(in, su));
                }
            }
            if(c[i].size()==0){
                coso = true;
            }
            else{
                sort(c[i].begin(), c[i].end());
            }
        }
        cout<<"Case #"<<cases<<": ";
        ll res=0;
        vll poin;
        if(coso){
            cout<<"0\n";
        }
        else{
            for(i=0;i<n;i++){
                poin.pb(0);
            }
            while(true){
                in = c[0][poin[0]].x;
                su = c[0][poin[0]].y;
                for(i=1;i<n;i++){
                    in = max(in, c[i][poin[i]].x);
                    su = min(su, c[i][poin[i]].y);
                    if(su<in){
                        break;
                    }
                }
                if(i<n){
                    for(i=0;i<n;i++){
                        if(c[i][poin[i]].y < in){
                            poin[i]++;
                            if(poin[i]>=c[i].size()){
                                break;
                            }
                        }
                    }
                    if(i<n)break;
                }
                else{
                    res++;
                    for(i=0;i<n;i++){
                        poin[i]++;
                        if(poin[i]>=c[i].size()){
                            break;
                        }
                    }
                    if(i<n)break;
                }
            }
            cout<<res<<"\n";
        }
    }
}
