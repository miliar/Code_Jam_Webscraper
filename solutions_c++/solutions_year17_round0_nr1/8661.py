//In the name of God
//-----gmmj

#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <ctime>
#include<iomanip>
#include<ctime>

#define Time printf("\nTime : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC);
#define For(J,R,K) for(int J=R;J<K;++J)
#define Rep(I,N) For(I,0,N)
#define MP make_pair
#define ALL(X) (X).begin(),(X).end()
#define SF scanf
#define PF printf
#define pii pair<long long,long long>
#define pdd pair<double , double>
#define Sort(v) sort(ALL(v))
#define Test freopen("a.in","r",stdin);
#define Testout freopen("a.out","w",stdout);
#define pb push_back
#define Set(a,n) memset(a,n,sizeof(a))
#define MAXN 100000+9
#define EPS 1e-15
#define inf 1ll<<62

typedef long long ll;

using namespace std;

int k;

set <string> vis;

bool isOk(string st)
{
    For(i , 0 , (int)st.size())
    {
        if(st[i] == '-')
            return false;
    }
    return true;
}

ll dig(string st)
{
    vis.clear();
    queue < pair<int , string> > q;

    q.push( MP(0 , st) );
    vis.insert(st);

    while(!q.empty())
    {
        string cur = q.front().second;
        int mv = q.front().first;
        q.pop();
        if(isOk(cur))
        {
            return mv;
        }
        For(i , 0 , ((int)cur.size()) - k + 1)
        {
            string nx = cur;
            Rep(j , k)
            {
                int ind = i+j;
                if(nx[ind] == '-')
                    nx[ind] = '+';
                else
                    nx[ind] = '-';
            }
            if(vis.find(nx) != vis.end())
                continue;
            vis.insert(nx);
            q.push(MP(mv + 1 , nx));
        }
    }

    return -1;
}

int main()
{
   // Test;
   // Testout;
    int tc , cas = 1;
    cin >> tc;
    while(tc --)
    {
        string st;
        cin >> st >> k;

        ll ans = dig(st);

        cout << "Case #" << cas++ <<": ";
        if(ans == -1)
        {
            cout << "IMPOSSIBLE";
        }
        else
        {
            cout << ans;
        }
        cout << endl;
    }
	return 0;
}
