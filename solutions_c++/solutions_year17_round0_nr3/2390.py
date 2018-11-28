/*
Author @kbstudios
Kaushal Bhogale GCJ 2017
*/
#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <utility>
#include <string>
#include <cctype>
#include <cmath>

using namespace std;

typedef long long ll;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

const int mod=1000000007;

#define rep(i,n) for(auto i=0; i<(n); i++)
#define mem(x,val) memset((x),(val),sizeof(x));
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))
#define pb push_back
#define inf (1<<30)
#define ins insert
#define xx first
#define yy second
#define eps 1e-9

#define testcase(t) int tc;cin >> tc;for(int t=1; t<=tc; t++)
#define out(result) cout << "Case #" << t << ": " << result << end;cerr << "Case #" << t << ": " << result << end;
#define outT(result) cout << "Case #" << t << ": " << result << end;

int main()
{
    //ios::sync_with_stdio(false);

    //#ifndef ONLINE_JUDGE
    // For getting input from input.txt file
    //freopen("C-large.in", "r", stdin);
    // Printing the Output to output.txt file
    //freopen("C-large-f.out", "w", stdout);
    //#endif
    testcase(t){
        ll n0, k0;

        cin >> n0 >> k0;

        vector<bool> ks;
        ll n = n0;
        ll k = k0;

        while(true){
            if(k == 1){
                break;
            }
            if(k%2 == 0){
                ks.pb(false);
            }
            else{
                ks.pb(true);
            }
            k = k >> 1;
        }
        reverse(ks.begin(), ks.end());

        ll kl = (int)ks.size();

        for(vector<bool>::iterator it = ks.begin(); it != ks.end(); ++it){
            if(n%2 == 0 && *(it)){
                n = n >> 1;
                n--;
            }
            else{
                n = n >> 1;
            }
            //cerr << n << "\n";
        }

        ll nhigh;
        ll pos = pow(2,kl);
        if(k0 - pos != 0){
            if(n%2 == 0){
                nhigh = n+1;
            }
            else{
                nhigh = n;
                n = n-1;
            }
        }
        else{
            nhigh = n;
            n = n-1;
        }

        //cerr << n << '\n';
        /* OUTPUT */
        //cerr << pos << '\n';
        ll calc = n0 - (pos-1) - pos*n;
        cerr << k0 - pos + 1 << " " << calc << '\n';
        if((k0 - pos + 1) <= calc){
            n = nhigh;
        }

        if(n%2 != 0 || n==0){
            cout << "Case #" << t << ": " << (n/2) << " " << n/2 << '\n';
            cerr << "Case #" << t << ": " << (n/2) << " " << n/2 << '\n';
        }
        else{
            cout << "Case #" << t << ": " << (n/2) << " " << n/2-1 << '\n';
            cerr << "Case #" << t << ": " << (n/2) << " " << n/2-1 << '\n';
        }
    }

    return 0;
}

