#include <bits/stdc++.h>
using namespace std;

int t,n,k,r,h;
double xam,res;
vector<pair<double,double> > v;


double pinggir(double a, double b){
    return (2*a*acos(-1)*b);
}

double alas(double a){
    return acos(-1)*a*a;
}
void keluar(){
    for (int i = 0; i < v.size(); i++){
        cout << v[i].first << " " << v[i].second << endl;
    }
}

int main(){
    scanf("%d", &t);
    for (int i = 1; i <= t; i++){
        scanf("%d %d", &n, &k);
        v.clear();
        for (int j = 0; j < n; j++){
            scanf("%d %d", &r, &h);
            v.push_back(make_pair(pinggir(r,h),r));
        }
        sort(v.begin(),v.end(), greater<pair<double,double> >());
        res = 0; xam = 0;
        for (int j = 0; j < k; j++){
            xam = max(xam,v[j].second);
            res += v[j].first;
        }
        xam = alas(xam);
        res += xam;
        xam += v[k-1].first;
        for (int j = k; j < n; j++){
            if (v[j].first + alas(v[j].second) > xam){
                res -= xam;
                xam = v[j].first + alas(v[j].second);
                res += xam;
            }
        }
        printf("Case #%d: %.8f\n", i,res);
    }
}
