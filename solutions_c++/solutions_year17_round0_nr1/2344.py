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

#define end '\n'

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

    #ifndef ONLINE_JUDGE
    // For getting input from input.txt file
    freopen("A-large.in", "r", stdin);
    // Printing the Output to output.txt file
    freopen("A-large-attempt.out", "w", stdout);
    #endif
    testcase(t){
        string inpString;
        cin >> inpString;
        int k;
        cin >> k;
        int n = (int)inpString.length();

        bool inp[n];

        for(int tem = 0; tem<n; tem++){
            inp[tem] = (inpString[tem] == '+')?true:false;
        }

        int result = 0;

        while(true){
            int tr;
            for(tr=0; tr<n; tr++){
                if(inp[tr] == false){
                    break;
                }
            }

            if(tr == n){
                out(result);
                break;
            }
            else if(tr>n-k){
                out("IMPOSSIBLE");
                break;
            }

            for(int i = tr; i<tr+k; i++){
                inp[i] = !(inp[i]);
            }
            result++;

        }

    }

    return 0;
}

