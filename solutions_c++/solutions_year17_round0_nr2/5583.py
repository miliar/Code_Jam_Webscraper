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

    freopen ("B-large.in", "r", stdin);
    freopen ("sol.txt","w",stdout);

    ios::sync_with_stdio(false);cin.tie(0);

    long long n , m  , k , d , t , tem1 , tem2 , tem3 , tem4 , y = 1, sum = 0 , ans = 0;
    string s , c;


    cin >>      t          ;

    while(t--){

        cs(y++);

        cin >> n;
        s = to_string(n);

        int st = 0;
        int nines = s.size();

        for(int i = s.size() - 1; i >= 1; i--){

            if(s[i] < s[i - 1]){

                for(int j = i; j >= 1; j--){

                    if(s[j] < s[j - 1]){

                        if(j == 1 && s[0] == '1'){

                            nines = 1;
                            st = 1;
                            s[j] = '9';
                            break;
                        }

                        s[j - 1]--;
                        nines = j;
                        s[j] = '9';

                    } else break;
                }
            }
        }

        for(int i = st; i < s.size(); i++){

            if(i >= nines) cout << "9";
            else cout << s[i];
        }

        cout << "\n";
    }

    return 0;
}
