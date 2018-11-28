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

ifstream fin("B.in");
ofstream fout("B_out.out");

int A[25], N, T;
ll DP[25][25][2];
set<ll,greater<ll>> Set;
string S;

string tostring(int n)
{
    string ret;
    while(n)
    {
        ret += (char) (n%10 + '0');
        n /= 10;
    }
    reverse(all(ret));
    return ret;
}

int main()
{
    fin >> T;
    //T = 100000;

    f(tt,1,T)
    {
        cout << tt << "\n";
        f(i,0,24) f(j,0,24) f(k,0,1) DP[i][j][k] = -1;
        fin >> S;
        //S = tostring(tt);
        //cin >> S;
        N = SZ(S);
        f(i,0,SZ(S)-1) A[i+1] = S[i] - '0';
        DP[0][1][0] = 0;
        f(i,0,N-1) f(d,1,9) f(small,0,1)
        {
            if(DP[i][d][small] < 0) continue;
            if(small) f(nd,d,9)
            {
                ll next_num = DP[i][d][small]*10 + nd;
                if(next_num > DP[i+1][nd][small]) DP[i+1][nd][small] = next_num;
            }
            else f(nd,d,A[i+1])
            {
                int next_small = small | (nd < A[i+1]);
                ll next_num = DP[i][d][small]*10 + nd;
                if(next_num > DP[i+1][nd][next_small]) DP[i+1][nd][next_small] = next_num;
            }
        }
        Set.clear();
        f(d,1,9) Set.insert(DP[N][d][0]);
        f(d,1,9) Set.insert(DP[N][d][1]);
        if(*Set.begin() >= 0) fout << "Case #" << tt << ": " << *Set.begin() << "\n";
        else
        {
            fout << "Case #" << tt << ": ";
            f(cnt,1,N-1) fout << "9";
            fout << "\n";
        }
    }
}
