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
 int ar[202] ;
int main()
{
    freopen("B-large.txt" , "r" , stdin);
    freopen("B-largeOp.txt" , "w" , stdout); 
    int t;
    cin >> t;
   
    for(int T = 1 ; T <= t ; T ++)
    {
            string s;
            cin >> s;
            int le = s.length();
            for(int i = 0 ; i < le; i++)
            {
                ar[i] = (int)(s[i] - '0');
            }
            int pp  = 0 ;
            int cp  = 0 ; 
        for(int i = 0 ;i < le - 1 ;i++)
        {
            cp = i;
              if (ar[i+1] > ar[i]){
                pp = cp + 1;

            }
           
            if(ar[i+1] < ar[i]){
               
               ar[pp] = ar[pp] - 1;

               
                for(int ii = pp + 1 ; ii < le ; ii++)
                {
                    ar[ii] = 9;
                }
                break;
            }
           



        }
        cout << "Case #" << T <<": " ;
        int h = 0;
        if(ar[h] == 0){
            for(int i =  0 ; i < le -1 ; i++){
                cout << 9 ;
            }
        }
        else
        for(int i = h ; i < le ; i++){
            cout << ar[i] ;
        }
        cout << endl;
    }

}