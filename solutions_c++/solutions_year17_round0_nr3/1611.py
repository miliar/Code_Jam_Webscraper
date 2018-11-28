#include <bits/stdc++.h>

#define ll long long

using namespace std;

// @return size of the task where last man goes.
ll rec(ll n, ll k)
{
    if (k == 1)
        return n;

    if (n%2 == 1) {
        if (k%2 == 1)
            return rec((n-1)/2, (k-1)/2);
        else
            return rec((n-1)/2, (k-1)/2+1);     // go to left
    }
    else {
        if (k%2 == 1)
            return rec(n/2-1, (k-1)/2);
        else
            return rec(n/2, (k-1)/2+1);
    }
}

int main()
{
    #ifdef FILEIO
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);

    int T;
    //scanf("%d\n", &T);
    cin >> T;
    for (int test = 1; test <= T; test++) {
        ll n, k;
        cin >> n >> k;

        ll last_size = rec(n, k);
        ll y, z;
        if (last_size%2 == 1) {
            z = y = (last_size-1)/2;
        }
        else {
            y = last_size/2;
            z = last_size/2-1;
        }

        cout << "Case #" << test << ": " << y << " " << z << endl;
    }
    
}
