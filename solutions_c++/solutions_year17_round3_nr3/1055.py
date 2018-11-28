#include <bits/stdc++.h>
#define ll long long int

using namespace std;

double pi=2*acos(0.0);

int n,k;

double U;

double p[55];

double prob=0.0;
int counter;


bool possible(double val){
    double x=U;
    for(int i=0;i<n;i++){
        if (p[i]<val){
            x-=(val-p[i]);
        }
    }

    if (x>=0.0)
        return true;
    else return false;
}

void bs(double l, double h){
    if (counter==100)
        return;
    counter++;
    double mid=(l+h)/2.0;

    if (possible(mid)){
        prob=mid;
        bs(mid,h);
    }
    else {
        bs(l,mid);
    }


}


int main(){
    freopen("C-small-1-attempt0.in","r",stdin); freopen("C-small-1.txt","w",stdout);
    int t;
    cin>>t;

    for(int tc=1;tc<=t;tc++){
        cin>>n>>k;

        cin>>U;

        for(int i=0;i<n;i++){
            cin>>p[i];
        }

        prob=0.0;
        counter=0;

        bs(0.0,1.0);

        for(int i=0;i<n;i++){
            if (p[i]<prob){
                p[i]=prob;
            }
        }

        double ans=1.0;

        for(int i=0;i<n;i++){
            ans*=p[i];
        }

        printf("Case #%d: %.7f\n",tc,ans);


    }


}
