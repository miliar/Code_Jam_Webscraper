#include <bits/stdc++.h>
using namespace std;

struct Comp {
    bool operator() (const pair<int, int>& l, const pair<int,int>& r) const {
        return l.second - l.first < r.second - r.first;
    }
};

int main(int, char**) {
    ifstream fin("C-small-2.in");
    ofstream fout("C-small-2.out");

    long long T;
    fin >> T;
    for (long long t = 0; t < T; ++t) {
        int n, k;
        fin >> n >> k;

        priority_queue< pair<int, int>, vector< pair<int, int> >, Comp> pq;
        pq.push( make_pair(0, n+1) );
        int l = 0, r = 0;
        while (k > 0 && !pq.empty()) {
            auto cur = pq.top(); pq.pop();
            int m = (cur.second + cur.first)/2;
            l = m - cur.first;
            r = cur.second - m;

            //cout << cur.first << " " << cur.second << "| " << m << "\n";            

            if (l > 1)
                pq.push( make_pair(cur.first, m) );
            if (r > 1)
                pq.push( make_pair(m, cur.second) );
            --k;
        }        
        --l; --r;
    
        fout << "CASE #" << t+1L << ": " << max(l,r) << " " << min(l, r) <<"\n";
    }
    return 0;
}
