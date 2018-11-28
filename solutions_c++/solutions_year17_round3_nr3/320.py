#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

const double EPS=1e-9;

int n,k;
vector<double> p;
double u;

double doit() {
    int ties=1;
    double second=-1;
    for(int i=1;i<n;i++) {
        if(fabs(p[i]-p[0])<EPS) ties++;
        else {
            second=p[i];
            break;
        }
    }
    double inc=second-p[0];
    double tot=inc*ties;
    if(tot>u) {
        inc=u/ties;
        tot=u;
    }
    //cout<<u<<','<<tot<<','<<inc<<','<<ties<<endl;
    for(int i=0;i<ties;i++) {
        p[i]+=inc;
    }
    //for(int i=0;i<n;i++) cout<<p[i]<<' ';
    //cout<<endl;
    u-=tot;
}

void solve(int tc) {
    cin>>n>>k>>u;
    p=vector<double>(n);
    for(int i=0;i<n;i++) cin>>p[i];
    p.push_back(1);
    n++;
    sort(p.begin(),p.end());
    while(fabs(u)>EPS) doit();
    double ret=1;
    for(int i=0;i<n;i++) ret*=p[i];
    cout<<std::fixed<<std::setprecision(12)<<"Case #"<<tc<<": "<<ret<<endl;
}

int main() {
    int cases;
    cin>>cases;
    for(int i=1;i<=cases;i++) solve(i);
}
