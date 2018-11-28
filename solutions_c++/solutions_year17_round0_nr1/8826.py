#include <bits/stdc++.h>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 2000000000000000000LL
#define INF 2000000000
#define EPS 1e-8
#define ll long long
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define setzero(a) memset(a,0,sizeof(a))
#define setdp(a) memset(a,-1,sizeof(a))
#define IOS ios_base::sync_with_stdio(0)
#define fillArray(a,n) fill_n(a,sizeof(a),n)

using namespace std;


int tests;
int counter , k, steps;
string str;


int main()
{
                freopen("A-large.in","r",stdin);
              freopen("out.txt","w",stdout);
    IOS;
    cin >> tests;
    while(tests--) {
        counter++;
        cin >> str >> k;
        steps = 0;
        for (int i=0; i < str.length() ; i++) {
            if (str[i] == '-' && str.length() - (i) >= k) {
                    steps++;
            for (int j=i ; j< i+k && j < str.length(); j++) {
                if (str[j] == '+')
                    str[j] = '-';
                else
                    str[j] = '+';
             }
          }
        }
        bool mnsFound = false;
        for (int i=0 ; i < str.length() ; i++)
        {
            if (str[i] == '-')
            {
                mnsFound = true;
            }
        }
//        cout << str << endl;
        if (mnsFound)
            cout << "Case #" << counter << ": IMPOSSIBLE" ;
        else
            cout << "Case #" << counter << ": " << steps;
        if (tests!=0)
            cout << endl;
    }
    return 0;
}
