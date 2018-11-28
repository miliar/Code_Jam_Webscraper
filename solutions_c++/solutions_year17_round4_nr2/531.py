#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
typedef long long ll;
typedef pair<int, int> pi;
const int MAXN = 1005;
int TC, N, C, M;
multiset<int> P[MAXN], B[MAXN];
int cmp(int x, int y) {
    return B[x].size() > B[y].size();
}

bool check(int x) {
    int surplus = 0;
    for (int i = 1; i <= N; ++i) {
        if (P[i].size() > x) {
            if (surplus < P[i].size()-x) return 0;
            surplus -= P[i].size() - x;
        }
        else {
            surplus += x - P[i].size();
        }
    }
    return 1;
}
bitset<MAXN> done, taken_seats;
priority_queue<pi, vector<pi>, greater<pi> > pq;
int main() {
    scanf("%d", &TC);
    for (int Txn = 1; Txn <= TC; ++Txn) {
        scanf("%d%d%d", &N, &C, &M);
        for (int i = 0, p, b; i < M; ++i) {
            scanf("%d%d", &p, &b);
            P[p].insert(b);
            B[b].insert(p);
        }
        int rides = (M+N-1)/N;
        for (int i = 1; i <= C; ++i) {
            rides = max(rides, (int) B[i].size());
        }
        while (check(rides) == false) ++rides;
        
        //puts("checkpoint 1");
        
        for (int k = 0; k < rides; ++k) {
            //must give seats!
            //printf("Ride %d: ", k);
            done.reset();
            taken_seats.reset();
            for (int i = 1; i <= N; ++i) {
                //printf("%d %d + %d\n", i, P[i].size(), k);
                if (P[i].size()+k >= rides) {
                    pi cur = mp(i, *P[i].begin());
                    P[cur.first].erase(P[cur.first].find(cur.second));
                    B[cur.second].erase(B[cur.second].find(cur.first));
                    taken_seats[i] = 1;
                    //printf("*%d ", i);
                    done[cur.second] = 1;
                }
            }
            for (int i = 1; i <= C; ++i) {
                if (B[i].size() <= 0) continue;
                if (done[i]) continue;
                pq.push(mp((int) *B[i].begin(), i));
            }
            
            
            int taken = 0;
            while (!pq.empty()) {
                pi cur = pq.top();
                if (cur.first <= taken) {
                    pq.pop();
                    auto it = B[cur.second].upper_bound(taken);
                    if (it != B[cur.second].end()) {
                        pq.push(mp(*it, cur.second));
                    }
                    continue;
                }
                else {
                    if (taken_seats[cur.first]) {
                        taken = cur.first + 1;
                        continue;
                    }
                }
                pq.pop();
                //printf("%d ", cur.first);
                P[cur.first].erase(P[cur.first].find(cur.second));
                B[cur.second].erase(B[cur.second].find(cur.first));
                taken = cur.first;
            }
            //printf("checpoint k = %d\n", k);
        }
        
        printf("Case #%d: ", Txn);
        int ans = 0;
        for (int i = 1; i <= C; ++i) ans += B[i].size();
        printf("%d %d\n", rides, ans);
        
        
        for (int i = 0; i <= N; ++i) P[i].clear();
        for (int i = 0; i <= C; ++i) B[i].clear();
    }
}