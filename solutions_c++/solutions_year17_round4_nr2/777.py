#include <bits/stdc++.h>

using namespace std;

vector<pair<int,int> > vec;//(seat,buyer)
int n, c, m;

bool possible(int rides) {
    for(int i=0;i<vec.size();i++) {
        if(vec[i].first*rides <= i) {
            return false;
        }
    }
    return true;
}

int calc(int rides) {
    int prom = 0, aux = 1;
    for(int i=1;i<vec.size();i++) {
        if(vec[i].first == vec[i-1].first) {
            aux++;
        } else {
            aux=1;
        }
        if(aux > rides) {
            prom = max(prom,aux-rides);
        }
    }
    return prom;
}

void solve(int caseNumber) {
    cin >> n >> c >> m;
    vec.clear();
    vec.resize(m);
    vector<int> cant(c+1,0);
    int mx = m, mn = 0;
    for(int i=0;i<m;i++) {
        cin >> vec[i].first >> vec[i].second;
        cant[vec[i].second]++;
        mn = max(mn,cant[vec[i].second]-1);
    }
    sort(vec.begin(),vec.end());
    while(mx-mn > 1) {
        int med = (mx+mn)/2;
        if(possible(med)) {
            mx = med;
        } else {
            mn = med;
        }
    }
    printf("Case #%d: %d %d\n",caseNumber,mx,calc(mx));
}

int main() {
    int casos;
    cin >> casos;
    for(int i=1;i<=casos;i++) {
        solve(i);
    }
}