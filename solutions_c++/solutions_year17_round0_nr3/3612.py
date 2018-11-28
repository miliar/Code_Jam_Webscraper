#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Interval {
    int left;
    int right;

    Interval(int l, int r) {
        left = l;
        right = r;
    }
};

struct DereferenceCompare : public std::binary_function<Interval, Interval, bool> {
    bool operator()(const Interval lhs, const Interval rhs) const {
        int l = lhs.right - lhs.left;
        int r = rhs.right - rhs.left;
        if(l == r)
            return lhs.left > rhs.right;
        else
            return l < r;
    }
};

void simulator(int n, int k, int *y, int *z) {
    priority_queue<Interval, vector<Interval>, DereferenceCompare> pq;
    Interval init(0, n + 1);
    pq.push(init);
    for(int i = 0; i < k; i++) {
        Interval cur = pq.top();
        pq.pop();
        int interv = cur.right - cur.left - 1;
        int middle = interv / 2 + cur.left;
        if(interv % 2 == 1)
            middle++;
        int ls = middle - cur.left - 1;
        int rs = cur.right - middle - 1;
        *y = ls > rs ? ls : rs;
        *z = ls < rs ? ls : rs;
        Interval a(cur.left, middle);
        Interval b(middle, cur.right);
        pq.push(a);
        pq.push(b);
    }
}

int main() {
    int t;
    cin>>t;
    for(int i=1;i<=t;i++) {
        int n, k;
        cin>>n>>k;
        int y, z;
        simulator(n, k, &y, &z);
        cout<<"Case #"<<i<<": "<<y<<" "<<z<<endl;
    }

    return 0;
}
