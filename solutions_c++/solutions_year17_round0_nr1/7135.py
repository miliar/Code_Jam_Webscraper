/*
ID: barish21
LANG: C++14
TASK: test
*/

/****Author: Barish Namazov****/
#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <stack>
#include <cstring>
#include <cmath>

using namespace std;

/***TEMPLATE***/
#define intt long long

#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define sz(s) (intt)s.size()

#define ms0(arr) memset(arr,0,sizeof arr)
#define ms63(arr) memset(arr,63,sizeof arr)

#define forn(i,a,b) for(intt i=a;i<=b;i++)
#define rofn(i,a,b) for(intt i=a;i>=b;i--)
#define setf(it,myset) for(set<intt>::iterator it=myset.begin();it!=myset.end();it++)

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define VI vector<intt>
#define PII pair<intt,intt>
#define VPII vector< PII >

#define posl(ch) (int)(ch-'a'+1)
#define posL(ch) (int)(ch-'A'+1)

#define IO ios_base::sync_with_stdio(false);cin.tie();
/***************/

/***Additional Functions***/
intt powmod(intt a,intt b,intt mod){intt res=1;a%=mod;assert(b>=0);for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
intt gcd(intt a,intt b){return __gcd(a, b);}
intt lcm(intt a,intt b){return a*b/gcd(a,b);}
intt is_prime(intt n){if(n==1)return 0;if(n==2)return 1;if(n%2==0)return 0;for(intt i=3;i<=sqrt(n);i+=2)if(n%i==0)return 0;return 1;}
intt is_integer(double n){if(floor(n)==ceil(n))return 1;return 0;}

intt sto_int(string s){stringstream ss(s);intt n;ss>>n;return n;}
string to_string(intt n){stringstream ss;ss<<n;string s=ss.str();return s;}

/**************************/

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    //ofstream fout ("test.out");
    //ifstream fin ("test.in");
    IO;
    intt T, c = 1;
    cin >> T;
    while (T --) {
        string s;
        intt k, ans = 0;
        cin >> s >> k;
        reverse (all (s));
        for (intt i = 0; i < s.size() - k + 1; i++)
            if (s[i] == '-') {
                for (intt j = i, cnt = 1; cnt <= k && j < s.size(); j ++, cnt ++)
                    if (s[j] == '-') s[j] = '+'; else
                    if (s[j] == '+') s[j] = '-';
                ans ++;
            }
        intt flag = 1;
        //cout << s << endl;
        for (intt i = 0; i < s.size(); i++)
            if (s[i] != '+') {
                flag = 0;
                break;
            }
        cout << "Case #" << c ++ << ": ";
        if (flag)
            cout << ans << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
