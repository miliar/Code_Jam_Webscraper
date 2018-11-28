#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

typedef long long ll;
#define S(a) scanf("%d",&a)
#define LS(a) scanf("%lld",&a)
#define FOR(i,a,b) for(int i = a, i <= b; ++i)
#define DOW(i,b,a) for(int i = b; i >= a; --i)
const ll INF = 1e17;
const ll MOD = 1e9 + 7;

int N,n;
string s,s2;
bool done = 0;
ll ans = 0;

void solve(int i,int last,bool l)
{
 //cout << i << " " << last << " " << l << "\n";
    if(i == n)
    {

        done = 1;

       // cout << s2 << "\n";
        ans = stoll(s2);

        return;

    }

    if(l)
    {
        for(int j = 9 ; j >= last; --j)
        {

            s2[i] =(j + '0');
            solve(i + 1,j,l);
            if(done) return;

        }
    }
    else
    {

    for(int j = s[i] - '0' ; j >= last; --j)
        {

            s2[i] =(j + '0');
            solve(i + 1,j,j < s[i] - '0');
            if(done) return;

        }



    }


}
ll solve2()
{


    string st(n - 1,'9');
    s[0] -= 1;
    st = s.substr(0,1) + st;
    s[0] += 1;
    s2 = s;
   // cout << s2 <<"\n";
    done = 0;
    ans = 0;
    solve(1,s[0] -'0',0);
//cout << s2 << " " << ans << " " <<  st << "\n";
    s2.clear();
    return max(ans,stoll(st));

}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    S(t);
    for(int tc = 1; tc <= t; ++tc)
    {
        //int n;

        cin >> s;
        n = s.length();


     //  cout << s<< "\n";
        cout << "Case #" << tc << ": " << (n <= 1 ? stoll(s) :solve2()) << "\n";
          s.clear();

    }

    return 0;
}
