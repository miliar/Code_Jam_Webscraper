#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <algorithm>
#include <fstream>
#include <utility>
#define MAX 9999999999
#define NUM 10
using namespace std;
typedef long long ll;
const double pi = 3.1415926535897;

bool cmp1(pair<ll,ll>a,pair<ll,ll>b){
    if(a.first*a.second > b.first*b.second) return true;
    return false;
}

ll calc(ll a,ll b){
    return a*a + 2*a*b;
}

bool cmp2(pair<ll,ll>a,pair<ll,ll>b){
    if(calc(a.first,a.second) > calc(b.first,b.second)) return true;
    return false;
}


int main () {
    ifstream input("/Users/ahnzeus/Desktop/input.in");
    ofstream output("/Users/ahnzeus/Desktop/output.txt");
    
    int T;
    //cin >> T;
    input >> T;
    for(int t=1;t<=T;t++){
        ll n,k;
        //cin >> n >> k;
        input >> n >> k;
        
        pair<ll,ll> a[NUM];
        
        for(int i=0;i<n;i++){
            ll r,h;
            //cin >> r >> h;
            input >> r >> h;
            a[i] = make_pair(r,h);
        }
        
        sort(a,a+NUM,cmp1);
        
        pair<ll,ll> std_p = make_pair(0, 0);
        ll temp = 0;
        for(int i=0;i<k;i++){
            temp += 2*a[i].first*a[i].second;
            if(calc(std_p.first,std_p.second) < calc(a[i].first,a[i].second))
                std_p = make_pair(a[i].first, a[i].second);
        }
        
        double res = 0;
        res += temp;
        
        
        sort(a+k,a+NUM,cmp2);
        if(k<n && calc(std_p.first,std_p.second) < calc(a[k].first,a[k].second)){
            res += (2*a[k].first*a[k].second - 2*a[k-1].first*a[k-1].second);
            a[k-1] = a[k];
        }
        
        ll max_r = -1;
        for(int i=0;i<k;i++)
            max_r = max(max_r,a[i].first);
        res += max_r*max_r;
        res *= pi;
        
        //cout.precision(6);
        //cout << "Case #" << t << ": " << fixed << res << endl;
        output.precision(6);
        output << "Case #" << t << ": " << fixed << res << endl;
    }
}
