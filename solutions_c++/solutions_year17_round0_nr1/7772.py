/********   All Required Header Files ********/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <assert.h>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#define fast cin.sync_with_stdio(0);cin.tie(0)
/***pre processors ***/
#define setbits(x) __builtin_popcount(x)
using namespace std;
#define gcd(a,b) __gcd(a,b)
#define TEST int t;cin>>t;while(t--)
const long long int mod = 1e9+7;
typedef long long int ll;
ll fexpo(ll a,ll b)
{
    if(b==0)
        return 1LL;
    if(b==1)
        return a;
    if(b==2)
        return a*a;
    if(b%2==0)
        return fexpo(fexpo(a,b/2),2);
    else
        return a*fexpo(fexpo(a,(b-1)/2),2);
}
int main()
{
    freopen("BC.txt" , "r" , stdin);
    freopen("chaluBAAP.txt" , "w" , stdout); 
    int t;
    cin >> t;
    for(int T = 1 ; T <= t ; T ++)
    {
        string s;
        cin >> s;
        int k  ; 
        cin >> k;
        int answer = 0;
        int le = s.length();
        for(int i = 0 ; i <= le - k ;i++)
        {
                if(s[i] == '-')
                {
                    answer++;
                    for(int j = i ; j < i + k ; j++)
                    {
                        if(s[j] == '-'){
                            s[j] = '+';
                        }
                        else s[j] = '-';
                    }
                }
              //  cout << "DONE " << s << endl;
        }
       // cout << "New string " << s << endl;
        bool found = false;
        for(int i  =0 ; i < le ; i++)
        {
            if(s[i] == '-')
                {
                    found = true;
                }
        }
         cout << "Case #" << T <<": ";
        if(found){
            cout << "IMPOSSIBLE" << endl;
        }
        else
        {
            cout <<  answer << endl;
        }
    }
}