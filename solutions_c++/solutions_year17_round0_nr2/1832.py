#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (decltype(a) i=(a); i<(b); ++i)
#define iter(it,c) for (decltype((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned long long ull;
const int INF = ~(1<<31);



int main()
{
    int t;
    cin >> t;
    rep(k,0,t)
    {
        string s;
        cin >> s;
        char last = '1';
        bool nondec = true;
        int ind = -1;
        rep(i,0,size(s))
        {
            if(s[i] < last)
            {
                nondec = false;
                ind = i;
                break;
            }
            last = s[i];
        }

        cout << "Case #" << k+1 << ": ";
        if(!nondec)
        {
            while(ind > 0 && s[ind] <= s[ind-1]) ind--;
            rep(i,ind+1,size(s)) s[i] = '9';
            s[ind]--;
            if(s[ind] == '0') s = s.substr(1);
        }
        cout << s << endl;
    }
    return 0;
}
