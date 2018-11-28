#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream cin("in.in");
    ofstream cout("out.out");

    int t;
    cin >> t;

    for(int o = 1; o <= t; o ++) {
        long long n, k;
        cin >> n >> k;

        cout << "Case #" << o << ": ";

        priority_queue< pair<long long, long long> > q; //current length & number of times
        while(!q.empty()) q.pop();

        q.push({n, 1});

        while(k > 0) {
            pair<long long, long long> now = q.top(); q.pop();
            if(now.first % 2 == 1) q.push({now.first / 2, now.second * 2});
            else {
                q.push( {now.first / 2, now.second} );
                q.push( {now.first / 2 - 1, now.second} );
            }

            k -= now.second;
            if(k <= 0) {
                cout << now.first / 2 << " " << (now.first - 1) / 2;
            }
        }


        cout << "\n";
    }

    return 0;
}
