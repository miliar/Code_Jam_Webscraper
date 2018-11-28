#include <bits/stdc++.h>
using namespace std;
long long need[55];
vector<long long>req[55];
long long lb[55], ub[55];
long long n, m;
long long solve(long long serv){
    long long ans=0;
    for(long long i=0;i<n;++i){
        lb[i] = ceil(need[i]*serv*.9);
        ub[i] = floor(need[i]*serv*1.1);
        while(!req[i].empty() && req[i].back() < lb[i]) { 
            req[i].pop_back(); 
        }
    }
    while (1) {
        long long ct = 0;
        for(long long i=0;i<n;++i)
            if (!req[i].empty() && req[i].back() <= ub[i]) { ct++; }
        if (ct == n) {
            ans++;
            for(long long i=0;i<n;++i) req[i].pop_back();
        }
        else 
            return ans;
    }
} 
int main() {
    long long t,tc=0;
    cin >> t;
    while(t--){
        for(long long i=0;i<50;++i)
            req[i].clear();
        cin >> n >> m;
        for(long long i=0;i<n;++i)
            cin >> need[i];
        for(long long i=0;i<n;++i){
            for(long long j=0;j<m;++j) { 
                long long a; 
                cin >> a; 
                req[i].push_back(a); 
            }
            sort(req[i].rbegin(), req[i].rend());
        }
        long long cnt=0;
        for(long long i=1;i<=1000000;++i) cnt += solve(i);
        cout << "Case #" << ++tc << ": " << cnt << endl;
    }
}