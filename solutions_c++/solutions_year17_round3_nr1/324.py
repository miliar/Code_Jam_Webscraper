#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;

const double PI=atan(1.)*4;

int n,k;

vector<pair<int,int> > cs;


double area(int r) {
    return PI*r*r;
}

double side(int r, int h) {
    return 2*PI*r*h;
}

bool help(pair<int,int> a, pair<int,int> b) {
    double s1=side(a.first,a.second);
    double s2=side(b.first,b.second);
    return s1>s2;
}

double doit(int first,int k) {
    double ret=area(cs[first].first)+side(cs[first].first,cs[first].second);
    k--;
    for(int i=0;i<n&&k>0;i++) if(i!=first&&cs[i].first<=cs[first].first) { k--; ret+=side(cs[i].first,cs[i].second); }
    if(k!=0) return -1;
    return ret;
}

void solve(int tc) {
    cs.clear();
    cin>>n>>k;
    int lr=0;
    int r, h;
    double ret=0;
    for(int i=0;i<n;i++) {
        cin>>r>>h;
        cs.push_back(make_pair(r,h));
    }
    sort(cs.begin(),cs.end(),help);
    for(int i=0;i<n;i++) ret=max(ret,doit(i,k));
    cout<<std::fixed<<std::setprecision(16)<<"Case #"<<tc<<": "<<ret<<endl;
}

int main() {
    int cases;
    cin>>cases;
    for(int i=1;i<=cases;i++) solve(i);
}
