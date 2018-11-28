#include <bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;
#define rep(i,n) for(ll i=0;i<(n);i++)

using namespace std;


struct Node{
    ll index;
    ll min;
    ll max;
    bool operator< (const Node &r) const{
        if(min != r.min)    return min > r.min;
        if(max != r.max)    return max > r.max;
        return index < r.index;
    }
};

ll leafNum(ll leafN){
    ll res = 1;
    while(res < leafN)  res *= 2;
    return res;
}

vector<Node> segmentTree(ll leafN){
    return vector<Node>(2 * leafN);
}

ll parent(ll x){
    return (x-1)/2;
}
vector<ll> child(ll x){
    vector<ll> res(2, 0);
    res[0] = 2*x + 1;
    res[1] = 2*x + 2;
    return res;
}

Node comp(Node x, Node y){
    return (x < y)? x:y;
}

void update(vector<Node> &segTree, ll leafN, ll index, Node value){
    index += leafN - 1;
    segTree[index] = value;
    while(0 < index){
        index = parent(index);
        vector<ll> childs = child(index);
        Node up = comp(segTree[childs[0]], segTree[childs[1]]);
        if(segTree[index].index == up.index &&
            segTree[index].min == up.min &&
            segTree[index].max == up.max){
            index = 0;
        }
        else    segTree[index] = up;
    }
}
ll INF = pow(10, 18)+5;
Node EMP = {INF, -1, -1};
set<ll> trueSet;
set<ll, greater<ll>> revTSet;

//  [l, r)
Node query(vector<Node> &segTree, ll l, ll r, ll nodeId, ll nodeL, ll nodeR){
    if(nodeR <= l || r <= nodeL)    return EMP;
    if(l <= nodeL && nodeR <= r){
        return segTree[nodeId];
    }
    vector<ll> childs = child(nodeId);
    ll mid = (nodeL+nodeR)/2;
    Node vl = query(segTree, l, r, childs[0], nodeL, mid);
    Node vr = query(segTree, l, r, childs[1], mid, nodeR);
    return comp(vl, vr);
}

Node createNode(vector<bool> &list, ll i, ll n){
    if(list[i])   return EMP;

    ll lenL = 0;
    ll lenR = 0;
    if((ll)revTSet.size() < n/100){
        for(auto lx : revTSet){
            if(i-1 < lx)    continue;
            if(list[lx]){
                lenL = i-lx-1;
                break;
            }
        }
    }
    else{
        for(ll lx = i-1; 0 <= lx; lx--){
            if(list[lx]){
                lenL = i-lx-1;
                break;
            }
        }
    }
    if((ll)trueSet.size() < n/100){
        for(auto rx : trueSet){
            if(rx < i+1)    continue;
            if(list[rx]){
                lenR = rx-i-1;
                break;
            }
        }
    }
    else{
        for(ll rx = i+1; rx < n+2; rx++){
            if(list[rx]){
                lenR = rx-i-1;
                break;
            }
        }
    }

    ll minlen = min(lenL, lenR);
    ll maxlen = max(lenL, lenR);
    Node node = {i, minlen, maxlen};
    return node;
}

Node solve1(ll n, ll k){
    Node head1;
    vector<bool> list(n+2, false);
    list[0] = list[n+1] = true;
    trueSet.insert(0);
    revTSet.insert(0);
    trueSet.insert(n+1);
    revTSet.insert(n+1);

    vector<Node> memo(n+2);
    rep(i, n+2) memo[i] = {i, min(i-1, n-i), max(i-1, n-i)};
    memo[0] = EMP;
    memo[n+1] = EMP;
    
    ll len = n+2;
    ll leafN = leafNum(len);
    vector<Node> segT = segmentTree(leafN);
    rep(i, len){
        update(segT, leafN, i, memo[i]);
    }
    
    rep(ik, k){
        head1 = query(segT, 0, leafN, 0, 0, leafN);
        ll idx = head1.index;
        update(segT, leafN, idx, EMP);
        list[idx] = true;
        trueSet.insert(idx);
        revTSet.insert(idx);

        for(ll lx = idx-1; 0 <= lx; lx--){
            if(list[lx])    break;
            Node node = createNode(list, lx, n);
            update(segT, leafN, lx, node);
        }
        for(ll rx = idx+1; rx < n+2; rx++){
            if(list[rx])    break;
            Node node = createNode(list, rx, n);
            update(segT, leafN, rx, node);
        }
    }

    return head1;
}

int main(){
    int t;
    cin >> t;

    rep(times, t){
        ll n, k;
        cin >> n >> k;

        Node head1 = solve1(n, k);
        trueSet.clear();
        revTSet.clear();

        cout << "Case #" << times+1 << ": " << head1.max << " " << head1.min << endl;
    }



    return 0;
}
