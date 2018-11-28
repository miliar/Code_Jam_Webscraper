#include <bits/stdc++.h>

using namespace std;
struct abc{
    double k,s;

};
double d;
vector<abc> vv;
bool comp(abc a, abc b){

    return a.k<b.k;
}

bool fnc(double mid){

    double mx=d/mid;
    for(int i=0; i<vv.size(); i++){

        double p=(d-vv[i].k)/vv[i].s;
                if(p>mx)return false;
        }
        return true;


}

int main(){
    //double p=10000000000.0;
//    printf("%f",p);
    freopen("in", "r", stdin);
    freopen("output","w",stdout);
    int t;
    scanf("%d", &t);
    for(int cs=1; cs<=t; cs++){
    int n;
    scanf("%lf %d", &d, &n);
    for(int i=0; i<n; i++){
        double p,q;
        scanf("%lf %lf", &p, &q);
        abc x;
        x.k=p;
        x.s=q;
        vv.push_back(x);
    }
    sort(vv.begin(), vv.end(), comp);
    double l=1.0, h=100000000000000.0;
    for(int i=1; i<=1000; i++){
        double mid=(l+h)/2;
        bool x=fnc(mid);
        if(x)l=mid;
        else h=mid;

    }

    printf("Case #%d: %0.6f\n", cs, l);
    vv.clear();

    }



}
