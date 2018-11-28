#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<string>
#include<queue>
using namespace std;


struct interv {
    long long len;
};

map<long long, long long> counts;
set<long long> seen;
bool operator< (interv const & lhs, interv const & rhs) {
    return lhs.len < rhs.len;
}

void solve(long long k, long long n){

    seen.clear();
    counts.clear();
    priority_queue<interv> pq;
    counts[n] = 1;
    pq.push({n});
    while(k - counts[pq.top().len] > 0){
        interv cur = pq.top();
        k -= counts[pq.top().len];
        pq.pop();
        if(cur.len %2 == 1){
            counts[(cur.len - 1) / 2] += 2 * counts[cur.len];
            cur.len = (cur.len - 1) / 2;
            if(seen.find(cur.len) == seen.end()){
                seen.insert(cur.len);
                pq.push(cur);
            }
        } else {
            long long oldlen = cur.len;
            counts[(cur.len - 1)/ 2] += counts[oldlen];
            cur.len = (cur.len - 1) / 2;
            if(seen.find(cur.len) == seen.end()){
                seen.insert(cur.len);
                pq.push(cur);
            }
            counts[(cur.len + 1)] += counts[oldlen];
            cur.len = cur.len + 1;
            if(seen.find(cur.len) == seen.end()){
                seen.insert(cur.len);
                pq.push(cur);
            }
        }
    }
    cout << pq.top().len / 2 << " " << (pq.top().len - 1) / 2;
}

int main(){

    int ncases;

    cin >> ncases;


    for(int i = 0; i < ncases;i++){
        long long k, n;
        cin >> n;
        cin >> k;
        cout << "Case #" << i + 1 << ": ";
        solve(k, n);
        cout << endl;
    }
}
