#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int t,n,q;
vector<pair<ll,ll> > mesta;
vector<vector<ll> > hrany;
vector<pair<ll,ll> > otazky;
int main() {
  ios::sync_with_stdio(false);
  cin>>t;
  for(int cislo=1;cislo<=t;cislo++){
    cout <<"Case #"<<cislo<<": ";
    cout <<setprecision(10)<<fixed;
    cin>>n>>q;
    mesta.resize(n);
    hrany.resize(n);
    otazky.resize(q);
    for(int i=0;i<n;i++)cin>>mesta[i].first>>mesta[i].second;
    for(int i=0;i<n;i++){
      hrany[i].resize(n);
      for(int j=0;j<n;j++)cin>>hrany[i][j];
    }
    vector<vector<ll> > cesta=hrany;
    for(int i=0;i<n;i++){
      cesta[i][i]=0LL;
      for(int j=i+1;j<n;j++)cesta[i][j]=cesta[i][j-1]+cesta[j-1][j];
    }
    /*for(int i=0;i<n;i++){
      for(int j=0;j<n;j++)cout <<" "<<cesta[i][j];cout <<endl;
    }
    return 0;*/
    for(int i=0;i<q;i++)cin>>otazky[i].first>>otazky[i].second;
    vector<vector<double> > dynamika(n, vector<double>(n,-1.0));
    vector<double> vsledok(n,-1.0);
    dynamika[0][0]=0.0;
    dynamika[1][0]=(hrany[0][1]*1.0)/(mesta[0].second);
    vsledok[0]=0.0;
    vsledok[1]=dynamika[1][0];
    for(int i=2;i<n;i++){
      //i-te mesto
      for(int j=0;j<i;j++){
        if(cesta[j][i]>mesta[j].first)continue;//vycerpany
        dynamika[i][j]=vsledok[j]+((cesta[j][i]*1.0)/(mesta[j].second));
        if(vsledok[i]<0.0)vsledok[i]=dynamika[i][j];
        else vsledok[i]=min(vsledok[i],dynamika[i][j]);
      }
    }
    cout <<vsledok[n-1]<<endl;
  }
  return 0;
}