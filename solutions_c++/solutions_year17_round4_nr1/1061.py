#include <iostream>
#include <fstream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <cmath>

using namespace std;

typedef map<pair<int,vector<int> >, int> MA;

MA memo;
int PP;
int dp(int left, int z, const vector<int> &cts) {
    if(left == 0){return 0;}
    const pair<int,vector<int> > key = make_pair(z, cts);
    MA::const_iterator iter = memo.find(key);
    if(iter != memo.end()){return iter->second;}
    vector<int> next = cts;
    int qq = (z == 0);
    int out = qq;
    for(int i=0;i<next.size();++i) {
        const int curr_val = cts[i];
        if(!curr_val){continue;}
        --next[i];
        int znext = ((z-i)+PP)%PP;
        out = max(out, qq + dp(left-1, znext, next));
        ++next[i];
    }
    memo[key] = out;
    return out;
}

void do_case(const int cn) {
    memo.clear();
    int N;
    int P;
    cin >> N >> P;
    vector<int> counts(P, 0);
    ::PP = P;
    for(int i=0;i<N;++i) {
        int t;
        cin >> t;
        counts[t%P]++;
    }
    int out = dp(N, 0, counts);
    printf("Case #%d: %d\n", cn, out);
}

int main(int argc, char **argv)
{
    int CASES;
    cin >> CASES;
    for(int cn=1;cn<=CASES;++cn) {
        do_case(cn);
    }

    return 0;
}
