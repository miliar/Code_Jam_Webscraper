#pragma comment(linker, ”/STACK:38777216“
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <stack>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <time.h>
#include <map>
#include <set>

using namespace std;

const int N = 1005;
const int inf = 1000 * 1000 * 1000;
const int mod = 1000 * 1000 * 1000 + 7;

int n,t,k;
double d;
set < pair<double,double> > q;
set < pair<double,double> >::iterator it;

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    cout.setf(ios::fixed);
    cout.precision(6);
    cin>>t;
    while(t--){
        k++;
        cin>>d>>n;
        for(int i=1;i<=n;i++){
            double kk,v;
            cin>>kk>>v;
            q.insert(make_pair(kk,v));
        }
        double time = 0.0;
        while(true){
            if((int)q.size() == 1){
                it = q.begin();
                time += (d - (*it).first) / (*it).second;
                break;
            }
            double t = 1e18 , xx , vv;
            for(it=q.begin();;++it){
                double x1 = (*it).first;
                double v1 = (*it).second;
                ++it;
                if(it == q.end())break;
                double x2 = (*it).first;
                double v2 = (*it).second;
                --it;
                if(v1 <= v2)continue;
                double T = (x1 - x2) / (v2 - v1);
                double S = x1 + v1 * T;
                if(S < d){
                    t = min(t , T);
                    xx = x1;
                    vv = v1;
                }
            }
            if(t == 1e18){
                it = q.begin();
                time += (d - (*it).first) / (*it).second;
                break;
            }
            time += t;
            q.erase(make_pair(xx , vv));
            vector < pair<int,int> > G;
            for(it = q.begin();it != q.end(); ++it){
                double x = (*it).first;
                double v = (*it).second;
                G.push_back(make_pair(x + t * v , v));
            }
            q.clear();
            for(int i=0;i<(int)G.size();i++)q.insert(G[i]);
        }
        printf("Case #%d: ",k);
        cout<<d / time<<endl;
        q.clear();
    }
    return 0;
}
