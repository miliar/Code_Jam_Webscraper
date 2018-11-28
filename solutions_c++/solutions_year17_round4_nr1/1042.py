#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

typedef long long ll;
typedef long double ld;
typedef priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pqG; // smaller first
typedef pair<int,int> pii;
typedef vector<int> vi;
#define S(a) scanf("%d",&a)
#define LS(a) scanf("%lld",&a)
#define D(a) scanf("%lf",&a)
#define LD(a) scanf("%lf",&a)
#define FOR(i,a,b) for(int i = a;i <= b;++i)
#define DOW(i,b,a) for(int i = b; i >= a;--i)
#define Sort(a) sort(a.begin(),a.end())
#define eb emplace_back
#define fi first
#define se second


const ld DINF = 1e45;
const ll INF = 1e17;
const ll MOD = 1e9 + 7;
const int MAXF = 500010;
ll fact[MAXF],inv[MAXF];
ll power(ll base,ll expo,ll MOD)
{
    ll res = 1;
    while(expo > 0)
    {
        if(expo & 1) res = (res * base) % MOD;
        base = (base * base ) % MOD;
        expo>>= 1;

    }

    return res;




}
void pre()
{
    fact[0] = fact[1] = inv[0] = inv[1] = 1;
    for(int i = 2; i < MAXF; ++i)
    {
        fact[i] = (fact[i - 1] * i) % MOD;
        inv[i] = power(fact[i],MOD -2,MOD);
    }

}
ll nck(int n,int k)
{
    if(n < k) return 0;
    ll ans = fact[n];
    ans = (ans * inv[k]) % MOD;
    ans = (ans * inv[n - k]) % MOD;
    return ans;

}





int main()
{
    freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
    int t;
    cin >>(t);

    for (int i = 0; i < t; i++)
    {
        int n, p;
        cin >> n >> p;
        int ar[105];
        int mod[4] = { 0 ,0,0,0};
        for (int y = 0; y < n; y++)
        {
            cin >> ar[y];
            mod[ar[y] % p]++;
        }
        int count = 0;
        if (p == 2)
        {
            count = mod[0] + ((mod[1]  +  1) / 2);
        }
        else if(p==3)
        {
            count = mod[0];

            if (mod[1] < mod[2])
            {
                count += mod[1];
                mod[2] -= mod[1];
                count += (mod[2]) % 3 != 0 ? mod[2] / 3 + 1: mod[2] / 3;
            }
            else
            {
                count += mod[2];
                mod[1] -= mod[2];
                count += (mod[1]) % 3 != 0 ? mod[1] / 3 + 1: mod[1] / 3;
            }
        }
        else if(p==4)
        {
           int extra = mod[2] % 2;
			if (extra == 1) {
				extra = 2;
			}
			count = mod[0] + mod[2] / 2;

			if (mod[1] <= mod[3]) {
				count += mod[1];
				mod[3] = mod[3] - mod[1];
                if(extra == 2 && mod[3] * 3 >= 6) count+=1,mod[3] = max(0,mod[3] - 2);
                else if(extra == 2 && mod[3] * 3 < 6) count++,mod[3] = 0;
                count += mod[3] % 4 != 0 ? mod[3] / 4 + 1 : mod[3] / 4;

			}
			else
			{
				count += mod[3];
				mod[1] = mod[1] - mod[3];
			    if(extra == 2 && mod[1]  >= 2) count+=1,mod[1] = max(0,mod[1] - 2);
                else if(extra == 2 && mod[1] * 1 < 2) count++,mod[1] = 0;
                count += mod[1] % 4 != 0 ? mod[1] / 4 + 1 : mod[1] / 4;
			}
        }

        cout << "Case #" << i+1 << ": " << count << "\n";


    }

    return 0;
}

