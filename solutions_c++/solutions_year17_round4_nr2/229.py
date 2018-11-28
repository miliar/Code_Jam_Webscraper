//In the name of Allah
#include <bits/stdc++.h>
using namespace std; 

typedef long double ld; 

const int maxN = 1000 + 10; 
struct Problem { 
    int count[maxN];
    int tot[maxN];
    int n, c, m; 

    int canDo( int d ) { 
        int rem = 0;
        int ans = 0;
        for( int i = 0 ; i < n ; i++ ) { 
            if( count[i] - rem > d ) 
                return -1; 

            if( count[i] <= d ) 
                rem += d - count[i]; 
            else { 
                ans += count[i]-d; 
                rem -= count[i]-d; 
            }
        }
        return ans; 
    }

    void solve() { 
        fill(count,count+maxN,0);
        fill(tot,tot+maxN,0);

        cin >> n >> c >> m; 
        int s = 0 , e = m; 
        for( int i = 0 ; i < m ; i++ ) { 
            int pl , id; 
            cin >> pl >> id; 
            pl--; id--;
            count[pl]++; 
            tot[id]++; 
            s = max( s , tot[id]-1 ); 
        }

        while( e - s > 1 ) {
            int mid = ( s + e ) / 2; 
            if( canDo( mid ) != -1 ) 
                e = mid; 
            else
                s = mid;
        }
        cout << e << " " << canDo(e) << endl;
    }
};

int main() { 
    cout << fixed << setprecision(15); 

    int t; cin >> t; 
    for( int i = 1 ; i <= t ; i++ ) { 
        cout << "Case #" << i << ": "; 
        Problem x; 
        x.solve(); 
    }
}
