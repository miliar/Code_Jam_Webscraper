#include<bits/stdc++.h>
#define ll long long
#define vll vector<long long>
#define pll pair<long long, long long>
#define mp make_pair
#define pb push_back
#define pt complex<long double>
#define ld long double
using namespace std;

int cases;
ll res[105][105][105][4], cres[105][105][105][4];

ll din3(ll m1, ll m2, ll r){
    if(cres[m1][m2][0][r]==cases)return res[m1][m2][0][r];
    ll aux, rres = 0;
    if(m1>0){
        aux = din3(m1-1, m2, (r+1)%3);
        if(r==0)aux++;
        rres = max(rres, aux);
    }
    if(m2>0){
        aux = din3(m1, m2-1, (r+2)%3);
        if(r==0)aux++;
        rres = max(rres, aux);
    }
    cres[m1][m2][0][r]=cases;
    return res[m1][m2][0][r] = rres;
}

ll din4(ll m1, ll m2, ll m3, ll r){
    if(cres[m1][m2][m3][r]==cases)return res[m1][m2][m3][r];
    ll aux, rres=0;
    if(m1>0){
        aux = din4(m1-1, m2, m3, (r+1)%4);
        if(r==0)aux++;
        rres = max(rres, aux);
        }
    if(m2>0){
        aux = din4(m1, m2-1, m3, (r+2)%4);
        if(r==0)aux++;
        rres = max(rres, aux);
        }
    if(m3>0){
        aux = din4(m1, m2, m3-1, (r+3)%4);
        if(r==0)aux++;
        rres = max(rres, aux);
        }
    cres[m1][m2][m3][r]=cases;
    return res[m1][m2][m3][r] = rres;
}

int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    ios_base::sync_with_stdio(false);
    ll i,n,t,k,p,aux,res;
    cin>>t;
    cases=0;
    while(t--){
        cases++;
        cout<<"Case #"<<cases<<": ";
        cin>>n>>p;
        ll can[5] = {0, 0, 0, 0, 0};
        for(i=0;i<n;i++){
            cin>>aux;
            can[aux%p]++;
        }
        res = can[0];
        if(p==2)res += (can[1]+1)/2;
        if(p==3)res += din3(can[1], can[2], 0);
        if(p==4)res += din4(can[1], can[2], can[3], 0);
        cout<<res<<endl;
    }
}
