#include <bits/stdc++.h>

using namespace std;

int t;
long long n,k;
map<long long,long long> m;
queue<long long> q;
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    for (int test = 1; test <= t; test++){
        cin >> n >> k;
        m.clear();
        while(q.size()) q.pop();
        m[n]=1;
        q.push(n);
        long long p;
        k--;
        while(1){
            p = q.front();
            q.pop();
            if (!m[p]) continue;
            if (m[p]>k) break;
            else{
                k -= m[p];
                q.push(p/2);
                q.push((p-1)/2);
                m[p/2]+=m[p];
                m[(p-1)/2]+=m[p];
                m[p]=0;
            }
        }
        cout << "Case #" << test << ": " << p/2 << " " << (p-1)/2 << " \n";
    }
    return 0;
}
