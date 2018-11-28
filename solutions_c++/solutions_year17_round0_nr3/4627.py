#include <vector>
#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <map>
#include <math.h>
#include <queue>
#include <climits>
#include <iomanip>

typedef long long ll;

using namespace std;

void solution(ll n,ll k)
{
    priority_queue<ll, vector<ll>, less<ll>> pq;
    pq.push(n);

    ll smallest, greatest;

    for (ll i = 1; i <= k; ++i) {
        ll top = pq.top();
        pq.pop();
        ll left = top / 2;
        ll right = top / 2;
        if (top % 2 == 0) right -=1;

        smallest = min(left,right);
        greatest = max(left, right);

        if (left > 0) pq.push(left);
        if (right > 0) pq.push(right);
    }

    cout << greatest << " " << smallest << endl;
}

int main()
{
    int T;
    cin >> T;

    for (size_t i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        ll n, k;
        cin >> n >> k;
        solution(n,k);
    }
    return 0;
}
