#include <bits/stdc++.h>
using namespace std;
#define _USE_MATH_DEFINES
typedef pair<double,double> ii;

double sol[1001][1001];

bool sorte(ii a,ii b){
    if (a.first!=b.first)return a.first>b.first;
    return a.second>b.second;
}

int main(){
    int n,k,t;
    ii val[1000];
    cin>>t;
    for (int c=1;c<=t;c++){
        cin>>n>>k;
        for (int i=0;i<n;i++){
            cin>>val[i].first>>val[i].second;
        }
        sort(val,val+n,sorte);
        double wmax;
        for (int j=0;j<n;j++){
                sol[0][j]=2*val[j].first*val[j].second+
            val[j].first*val[j].first;
            //cout<<val[j].first<<" "<<val[j].second<<endl;
        }
        for (int i=1;i<k;i++){
            wmax=sol[i-1][i-1];
            for (int j=i;j<n;j++){
                sol[i][j] = wmax - val[j].first*val[j].first+sol[0][j];
                wmax = max(sol[i-1][j],wmax);
            }
        }
        /*for (int i=0;i<k;i++){
            for(int j=i;j<n;j++)cout<<sol[i][j]<<" ";
            cout<<endl;
        }*/
        wmax = -1;
        for (int j=k-1;j<n;j++)wmax = max(wmax,sol[k-1][j]);
        printf("Case #%d: %.9lf\n",c,wmax*M_PI);
    }
}
