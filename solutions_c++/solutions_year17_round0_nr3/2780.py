#include <iostream>
#include <vector>
#include <utility>
#include <stdio.h>
#include <cstring>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <fstream>
#include <algorithm>

using namespace std;

#define mp make_pair
#define pb push_back

int main() {

    std::ios::sync_with_stdio(false);

    int tc;
    cin>>tc;

    for (int t=0; t<tc; t++){

        priority_queue <long long> q;
        map <long long, long long> m;
        m.clear();
        while (!q.empty())
            q.pop();
        long long n, k, cnt;
        cin>>n>>k;
        m[n] = 1;
        q.push(n);
        cnt = 0;

        while (!q.empty()){
            long long temp = q.top();
            long long l, r;
            if (temp % 2 == 0){
                l = temp / 2 - 1;
                if (l < 0)
                    l = 0;
                r = temp / 2;
                if (r < 0)
                    r = 0;
            }
            else{
                l = temp / 2;
                r = temp / 2;
            }
            q.pop();

            if (cnt + m[temp] >= k){
                cout<<"Case #"<<t+1<<": ";
                cout<<r<<" "<<l<<"\n";
                break;
            }
            else{
                cnt += m[temp];
                if (m.find(l) == m.end()){
                    m[l] = m[temp];
                    q.push(l);
                }
                else{
                    m[l] += m[temp];
                }
                if (m.find(r) == m.end()){
                    m[r] = m[temp];
                    q.push(r);
                }
                else{
                    m[r] += m[temp];
                }
            }
        }
    }

    return 0;
}
