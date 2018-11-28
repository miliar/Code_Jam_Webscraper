#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define fori(n) for(int i = 0; i < n; i++)
#define forj(m) for(int j = 0; j < m; j++)
#define fork(m) for(int k = 0; k < m; k++)
#define for1(n) for(int i = 1; i < n; i++)

#define mp make_pair
#define pb push_back
#define fi first
#define se second


int main()
{
//    cin.tie(0);
//    ios_base::sync_with_stdio(0);
    ifstream cin("a.in");
    ofstream cout ("output.txt");
    int t;
    cin >> t;

    fork(t){

        ll d,n;
        cin >> d >> n;
        ld minn = 0;
        fori(n){
            ld a,b;
            cin >> a >> b;
            ld dd = (d-a)/b;
            if (dd > minn) minn = dd;
        }
        ld ans = d/minn;
        cout << "Case #" << k+1 << ": " << fixed << setprecision(7) << ans << "\n" ;

    }
}

