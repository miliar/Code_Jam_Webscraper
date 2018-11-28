#include <cstdio>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <algorithm>
#define MAX_N 1005
#define ll __int64

using namespace std;


struct Node {
    ll s, e;
    ll len;
    Node(ll _s, ll _e, ll _len) : s(_s), e(_e), len(_len) {}
    bool operator > (const Node b) const {
        if (len == b.len) {
            return s < b.s;
        } else {
            return len > b.len;
        }
    }
    bool operator < (const Node b) const {
        if (len == b.len) {
            return s > b.s;
        } else {
            return len < b.len;
        }
    }
};


int main()
{
   // freopen("in.txt", "r", stdin);
   //freopen("C-small-2-attempt1.in", "r", stdin);
  //  freopen("B-small-attempt4.in", "r", stdin);
   // freopen("out.txt", "w+", stdout);
    int T;
    scanf("%d", &T);
    ll N, K;
    for (int i = 1; i<= T; i++) {
        scanf("%I64d%I64d", &N, &K);
        priority_queue<Node> q;
        q.push(Node(1, N, N));
        ll right, left;
        for (ll i = 0; i < K; i++) {
            Node node = q.top(); q.pop();
            //cout << node.s << " " << node.e << endl;
            ll local = (node.s + node.e) / 2;
            left = local - node.s;
            right = node.e - local;
            if (left >= 1)
                q.push(Node(node.s, local-1, left));
            if (right >= 1)
                q.push(Node(local+1, node.e, right));
        }

        printf("Case #%d: %lld %lld\n", i, max(right, left), min(right, left));
    }
    return 0;
}
