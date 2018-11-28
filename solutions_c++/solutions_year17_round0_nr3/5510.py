#include <iostream>
#include <queue>
#include <climits>
using namespace std;

struct r{
    int x, y;
};

struct i{
    int s, e;
};

class Compare{
public:
    bool operator ()(i a, i b){
        return (a.e-a.s < b.e-b.s);
    }
};

r solve(int n, int k){
    priority_queue<i, vector<i>, Compare> pq;

    pq.push({0, n+1});

    int minlr=-1, maxlr=-1;

    while(k--){
        i crt = pq.top();
        pq.pop();

        int mid = (crt.s+crt.e)/2;
        minlr = min(mid-crt.s-1, crt.e-mid-1);
        maxlr = max(mid-crt.s-1, crt.e-mid-1);

        pq.push({crt.s, mid});
        pq.push({mid, crt.e});
    }

    r res = {maxlr, minlr};
    return res;
}

int main()
{
    int t;
    cin>>t;

    for(int i=1;i<=t;i++){
        int n, k;
        cin>>n>>k;

        r res = solve(n, k);
        cout<<"Case #"<<i<<": "<<res.x<<" "<<res.y<<"\n";
    }
    return 0;
}
