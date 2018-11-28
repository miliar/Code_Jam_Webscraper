#include<bits/stdc++.h>
#define LL int64_t
#define LD long double
using namespace std;
int n,p;
vector<int> counts;
vector<vector<vector<vector<vector<int> > > > >  dyn;

int rec(vector<int> counts, int remainder) {
    bool allZero = true;
    for(int i : counts) if(i!=0) allZero = false;
    int& mem = dyn[counts[0]][counts[1]][counts[2]][counts[3]][remainder];
    if(mem >= -1) return mem;
    if(allZero) return mem=0;

    int best = INT_MIN;
    for(int i=0;i<4;i++) {
        if(counts[i]==0) continue;
        counts[i]--;
        int newRemainder = (remainder + p - i) % p;
        int res = rec(counts, newRemainder);
        if(res >= 0 && res > best) best = res;
        counts[i]++;

    }
    if(best == INT_MIN) return mem = -1;
    return mem = best + (remainder == 0);
}

int f() {
    cin>>n>>p;
    counts = vector<int>(4,0);
    for(int i=0;i<n;i++) {
        int g;
        cin>>g;
        counts[g%p]++;
    }
    dyn = vector<vector<vector<vector<vector<int> > > > >(counts[0]+1,
            vector<vector<vector<vector<int> > > >(counts[1]+1,
                vector<vector<vector<int> > >(counts[2]+1,
                    vector<vector<int> >(counts[3]+1,
                        vector<int>(p,-2)))));

    return rec(counts,0);
    
}

int main() {
    int T;
    cin>>T;
    for(int i=1;i<=T;i++) {
        cout<<"Case #"<<i<<": ";
        cout<<f();
        cout<<endl;

    }
}
