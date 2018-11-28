#include<iostream>
#include<algorithm>
#include<set>
#include<string>
#include<cmath>
#include <iomanip> 
#include<map>
#include<vector>
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define REP(i,n) for(int i=0;i<n;++i)
#define REPD(i,n) for(int i=n;i>=0;--i)
#define FOR(i,j,k) for(int i=j;i<k;++i)
#define LL long long int
using namespace std;

double initial(pair<double,double> p)
{
       double ret = 0;
       double pi = 3.14159265359;
       ret = pi * p.first * p.first + 2.0*pi *p.first*p.second;
       return ret;
}

double area(pair<double,double> p)
{
       double ret = 0;
       double pi = 3.14159265359;
       ret = 2.0*pi *p.first*p.second;
       return ret;
}

void solve(int wc)
{
     int n,k; cin>>n>>k;
     double ret = 0;
     
     vector<pair<double,double> > d(n);
     REP(i,n)
     {
             double a,b; cin>>a>>b;
             d[i] = make_pair(a,b);
     }
     
     sort(ALL(d));
     reverse(ALL(d));
     
     vector<vector<double> > w(k+1); REP(i,k+1) w[i].resize(n);
     REP(i,k+1) REP(j,n) w[i][j] = 0;
     REP(j,n) w[1][j] = initial(d[j]);
     FOR(i,2,k+1) 
     {
        FOR(j,i-1,n)
        {
            REP(l,j)
            {
                    double x1 = w[i][j];
                    double x2 = w[i-1][l]+area(d[j]);
                    w[i][j] = max(w[i][j],x2);
            }    
        }
     }
     
     REP(i,n) ret= max(w[k][i],ret);
     
     //REP(i,k+1) {REP(j,n) cout<<w[i][j]<<" ";cout<<endl;}
     
     //<<fixed<<setprecision(6)
     cout<<"Case #"<<(wc+1)<<": "<<fixed<<setprecision(9)<<ret<<endl;
}

int main(){
    int g; cin>>g;
    REP(w,g) solve(w);
    return 0;
}
