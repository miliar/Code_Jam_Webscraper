/// In the name of God
#include <bits/stdc++.h>
//#define int long long
using namespace std;
typedef pair<int,int> pii;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;

#define y1 def1
#define X first
#define Y second
#define endl '\n'
#define all(o) o.begin(), o.end()
#define IOS ios::sync_with_stdio(0), cin.tie(0)
const int maxn = 100 + 10;
const ld inf = 1e15;
ld en[maxn], spe[maxn];
ld d[maxn][maxn], D[maxn][maxn];
int main(){
    IOS;
    freopen("CL.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int it=0; it<T; it++){
        cout << "Case #" << it + 1 << ": ";
        int n, q;
        cin >> n >> q;
        for(int i=0; i<n; i++)
            cin >> en[i] >> spe[i];
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++){
                int x;
                cin >> x;
                d[i][j] = x;
                if(d[i][j] == -1) d[i][j] = inf;
                if(i == j) d[i][j] = 0;
            }
        for(int k=0; k<n; k++)
            for(int i=0; i<n; i++)
                for(int j=0; j<n; j++)
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
        /*for(int i=0; i<n; i++, cout<<endl)
            for(int j=0; j<n; j++)
                cout << d[i][j] << " ";*/
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++){
                if(d[i][j] <= en[i])
                    D[i][j] = d[i][j]/spe[i];
                else
                    D[i][j] = inf;
            }
        for(int k=0; k<n; k++)
            for(int i=0; i<n; i++)
                for(int j=0; j<n; j++)
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
        for(int i=0; i<q; i++){
            int u, v;
            cin >> u >> v;
            u--, v--;
            cout << setprecision(12) << D[u][v] << " ";
        }
        cout << endl;
    }
}
