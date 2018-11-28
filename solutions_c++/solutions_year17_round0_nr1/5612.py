#include <bits/stdc++.h>

using namespace std;

#define mem0(arr) memset(arr , 0 , sizeof arr)
#define memf(arr) memset(arr , false , sizeof arr)
#define memdp(arr) memset(arr , -1 , sizeof arr)
#define rep(i , n) for(int i = 1; i <= n; i++)
#define loop(i , n) for(int i = 0; i < n; i++)
#define pb push_back
#define fi first
#define se second
#define cs(y) cout << "Case #" << y << ": "
#define cs2(y) cout << "Case " << y << ":" << "\n"

typedef long long ll;


int main()
{

    freopen ("A-large.in", "r", stdin);
    freopen ("sol.txt","w",stdout);

    //ios::sync_with_stdio(false);cin.tie(0);

    int n , m  , k , d , t , tem1 , tem2 , tem3 , tem4 , y = 1, sum = 0 , ans = 0;
    string s , c;


    cin >>      t          ;

    while(t--){

        cs(y++);

        ans = 0;
        bool imp = false;
        cin >> s >> k;

        for(int i = 0; i < s.size(); i++){

            if(s[i] == '-' && i + k <= s.size()){

                for(int j = i; j < i + k; j++){

                    if(s[j] == '+') s[j] = '-';
                    else s[j] = '+';
                }

                ans++;

            } else if (s[i] == '-'){

                cout << "IMPOSSIBLE\n";
                imp = true;
                break;
            }
        }

        if(!imp) cout << ans << "\n";
    }

    return 0;
}
