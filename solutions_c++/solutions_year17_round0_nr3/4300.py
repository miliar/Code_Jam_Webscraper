
#include <iostream>
#include <queue>
#include <cmath>

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pll;

struct compare {
    bool operator()(const pll l1, const pll l2) {
        if (l1.second != l2.second) return l1.second < l2.second;
        else return l1.first > l2.first;
    }
};

void process(ll n, ll k){
    priority_queue<pll, vector<pll>, compare> pq;
    if (n == k){
        cout << 0 << " " << 0 ;
        return;
    }
    if ( k ==1){
        cout << floor(ld(n)/2) << " " << floor(ld(n-1)/2)  ;
        return;
    }

    pq.push(make_pair(0,n+1));
    // cout << pq.size();
    pll temp;
     for (int t = 0; t < k; t++)
    {
        temp = pq.top();
        pq.pop();
        ll d1 = floor(ld(temp.second)/2);
        pq.push(make_pair(temp.first,d1));
        pq.push(make_pair(temp.first+d1,temp.second-d1));
    }

    cout  << floor(ld(temp.second-1)/2) << " " << floor(ld(temp.second-2)/2);
    return;
}


int main()
{
    int T, i;
    ll n, k;
    cin >> T;
    i = T;
    while (i-- > 0)
    {
        cin >> n >> k;
        cout << "Case #" << T - i << ": ";
        process(n,k);
        cout << endl;
    }
}