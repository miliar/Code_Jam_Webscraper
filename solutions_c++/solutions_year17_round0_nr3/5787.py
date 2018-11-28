#include<iostream>
#include <cstdio>      
#include <cstdlib>     
#include <ctime>       
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <queue>

using namespace std;

typedef long long ll;

const int maxn = 1000000 + 10;

ll total[maxn];

void solve1000(ll n, ll k) {

    bool a[1111];
    for(int i=1; i<=n; i++) {
        a[i] = false;
    }

    a[0] = true;
    a[n+1] = true;
    
    int l[1111];
    int r[1111];

    int last = -1;
    for(int i=1; i<=k; i++) {
        for(int j=1; j<=n; j++) if (a[j] == false) {
            int tl = j;
            int tr = j;
            
            while (a[tr+1] == false) {
                tr++;
            }

            while (a[tl-1] == false) {
                tl--;
            }

            l[j] = j - tl;
            r[j] = tr - j;
        }
        
        last = -1;
        for(int j=0; j<=n; j++) if (a[j] == false) {
            if (last == -1) {
                last = j;
            } else {
                if ((min(l[j],r[j]) > min(l[last],r[last])) || (min(l[j],r[j]) == min(l[last],r[last]) && (max(l[j],r[j]) > max(l[last],r[last]))) ) {
                    last = j;
                }
            }
        }

        a[last] = true;
    }
    
    // cout << max(l[last],r[last]) << " " << min(l[last],r[last]) << " : c" << endl;
}

void solve1000000(ll n, ll k) {

    int first = 1;
    int last = 1;
    total[1] = n;

    while (last < k) {
        
        int nlast = last;

        for(int i=first; i<=nlast && last < k; i++) {
            total[last + 1] = (total[i])/2;
            last++;
        }

        for(int i=first; i<=nlast && last < k; i++) {
            total[last + 1] = (total[i]-1)/2;
            last++;
        }

        first = nlast+1;
    }

    cout << total[k]/2 << " " << (total[k]-1)/2 << endl;
}

int main() {

    std::ios::sync_with_stdio(false);
	freopen("c-small-2-attempt0-in.txt", "r", stdin);
	freopen("c-small-out-2.txt", "w", stdout);

    int test = 0;
    cin >> test;

    for(int t=1; t<=test; t++) {
        ll n,k;

    	cin >> n >> k;

        cout << "Case #" << t << ": ";
        // solve1000(n,k);
        solve1000000(n,k);
    }

    return 0;
}