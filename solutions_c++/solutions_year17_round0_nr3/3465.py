#include<bits/stdc++.h>
#include<stdio.h>
#include<string.h>

using namespace std;
typedef long long ll;
typedef double db;
const int N = 1005;

int get_mid(int l,int r) {
    return (l + r) >> 1;
}

struct Node{
    int m,l,r;
    Node(int _l = 0,int _r = 0) {
        l = _l, r = _r;
        m = get_mid(l, r);
    }
    int Min() const{
        return min(m - l, r - m);
    }
    int Max() const {
        return max(m - l, r - m);
    }
    bool operator < (const Node & t) const{
        return Min() < t.Min() || Min()==t.Min()&&Max() < t.Max();
    }
    void print(){
        printf("l: %d   m: %d   r:  %d\n", l, m, r);
    }
};

int main() {
#ifdef PKWV
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
#endif // PKWV
    int T;
    scanf("%d", &T);
    for(int ca=1; ca<= T; ca++) {
        int n,k;
        scanf("%d%d",&n,&k);
        priority_queue<Node> q;
        q.push(Node(0, n+1));
        for(int i = 1;i<k;i++) {
            Node now = q.top();
//            now.print();
            q.pop();
            if(now.l < now.m) q.push(Node(now.l, now.m));
            if(now.m < now.r) q.push(Node(now.m, now.r));
        }
        Node now = q.top();
        printf("Case #%d: %d %d\n",ca, now.Max() - 1, now.Min() - 1);
    }
    return 0;
}
