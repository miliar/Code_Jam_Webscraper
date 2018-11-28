#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <unordered_map>
#include <functional>
#include <bitset>
using namespace std;

bool ok(vector<bool> &v) {
    for (int i=0; i<v.size(); ++i)
        if (!v[i])
            return false;
    return true;
}
int main() {
    int ntc;
    cin>>ntc;
    for (int tc=1; tc<=ntc; ++tc) {
        string s;
        int k, n;
        cin>>s>>k;
        n=s.length();
        vector<bool> v(n, 0);
        for (int i=0; i<n; ++i)
            if (s[i]=='+')
                v[i]=1;
        int ans=0;
        list<pair<vector<bool>, int>> q;
        set<vector<bool>> intree;
        q.push_back(make_pair(v, 0));
        intree.insert(v);
        bool found=0;
        while (!q.empty()) {
            pair<vector<bool>, int> p=q.front();
            q.pop_front();
            vector<bool> vv=p.first;
            /*
            cout<<"Popped:\n";
            for (int ii=0; ii<vv.size(); ++ii)
                cout<<vv[ii]<<' ';
            cout<<endl;
            */
            if (ok(vv)) {
                cout<<"Case #"<<tc<<": "<<p.second<<'\n';
                found=1;
                break;
            }
            if (p.second>n) {
                cout<<"Case #"<<tc<<": IMPOSSIBLE\n";
                found=1;
                break;
            }
            for (int i=0; i<vv.size()-k+1; ++i) {
                if (!vv[i]) {
                    vector<bool> vvv(vv);
                    for (int j=0; j<k; ++j)
                        vvv[i+j]=!vv[i+j];
                    if (intree.find(vvv)==intree.end()) {
                        q.push_back(make_pair(vvv, p.second+1));
                        intree.insert(vvv);
                    }
                }
            }
        }
        if (!found)
            cout<<"Case #"<<tc<<": IMPOSSIBLE\n";
    }
    return 0;
}