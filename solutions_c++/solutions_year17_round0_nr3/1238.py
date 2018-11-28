#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/rope>

typedef long long ll;
using namespace std;
using namespace __gnu_cxx;
using namespace __gnu_pbds;

template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag,tree_order_statistics_node_update>;

#define all(x) x.begin(), x.end()
#define f(i,a,b) for(int i = (a); i <= (b); i++)
#define fd(i,a,b) for(int i = (a); i >= (b); i--)
#define mp make_pair
#define faster_io() ios_base::sync_with_stdio(false)
#define pb push_back
#define pii pair<int,int>
#define SZ(x) ((int)x.size())
#define vii vector<pair<int,int>>

const int INF = 1000000005;
const ll INFLL = 1000000000000000002ll;
const ll MOD = 1000000007;

inline ll min(ll a, ll b, ll c){return min(min(a,b),c);}
inline ll min(ll a, ll b, ll c, ll d){return min(min(min(a,b),c),d);}
inline ll max(ll a, ll b, ll c){return max(max(a,b),c);}
inline ll max(ll a, ll b, ll c, ll d){return max(max(max(a,b),c),d);}

// --------------------------------------------------------------------------------------------

ifstream fin("C.in");
ofstream fout("C_out.out");

int T;
ll K, N, N1, N2, T1, T2;

int main()
{
    fin >> T;

    f(tt,1,T)
    {
        fin >> N >> K;
        if(K == 1)
        {
            cout << "Case #" << tt << ": " << N/2 << " " << (N-1) / 2 << "\n";
            fout << "Case #" << tt << ": " << N/2 << " " << (N-1) / 2 << "\n";
            continue;
        }
        K--;
        N1 = N/2;
        N2 = (N-1) / 2;
        T1 = T2 = 1;
        ll ans1 = -1, ans2 = -1;
        while(true)
        {
            if(T1 >= K)
            {
                ans1 = N1/2;
                ans2 = (N1-1) / 2;
                break;
            }
            K -= T1;
            if(T2 >= K)
            {
                ans1 = N2/2;
                ans2 = (N2-1) / 2;
                break;
            }
            K -= T2;
            if(N1 == N2)
            {
                ll next_n1 = N1 / 2;
                ll next_n2 = (N1-1) / 2;
                T1 *= 2;
                T2 *= 2;
                N1 = next_n1;
                N2 = next_n2;
            }
            else if(N1&1)
            {
                ll next_n1 = N2 / 2;
                ll next_n2 = (N2-1) / 2;
                ll next_t1 = (T1+T2) * 2 - T2;
                ll next_t2 = T2;
                N1 = next_n1;
                N2 = next_n2;
                T1 = next_t1;
                T2 = next_t2;
            }
            else
            {
                ll next_n1 = N1/2;
                ll next_n2 = N2/2;
                ll next_t1 = T1;
                ll next_t2 = (T1+T2) * 2 - T1;
                N1 = next_n1;
                N2 = next_n2;
                T1 = next_t1;
                T2 = next_t2;
            }
        }
        cout << "Case #" << tt << ": " << ans1 << " " << ans2 << "\n";
        fout << "Case #" << tt << ": " << ans1 << " " << ans2 << "\n";
    }
}
