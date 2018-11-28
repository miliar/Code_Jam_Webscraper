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

int arr_lf [1000000 + 10];
int arr_rt [1000000 + 10];

int main()
{

    freopen ("C-small-1-attempt0.in", "r", stdin);
    freopen ("ans.txt","w",stdout);

    ios::sync_with_stdio(false);cin.tie(0);

    long long n , m  , k , d , t , tem1 , tem2 , tem3 , tem4 , y = 1, sum = 0 , ans = 0;
    string s , c;


    cin >>      t          ;

    while(t--){


        memset(arr_lf, 0 , sizeof arr_lf);
        memset(arr_rt, 0 , sizeof arr_rt);
        cs(y++);

        cin >> n >> k;

        for(int i = 0; i < k; i++){

            int busy_lf = -1, busy_rt = n;
            int index;
            ll maxi = -1, maxi2 = -1;

            for(int j = 0; j < n; j++){

                if(arr_lf[j] == -1){

                    busy_lf = j;
                    continue;
                }

                arr_lf[j] = j - busy_lf - 1;
            }

            for(int j = n - 1; j >= 0; j--){

                if(arr_rt[j] == -1){

                    busy_rt = j;
                    continue;
                }

                arr_rt[j] = busy_rt - j - 1;

                if( ( min(arr_lf[j], arr_rt[j]) > maxi) ||
                    ( min(arr_lf[j], arr_rt[j]) == maxi && max(arr_lf[j], arr_rt[j]) >= maxi2) ){

                    maxi = min(arr_lf[j], arr_rt[j]);
                    maxi2 = max(arr_lf[j], arr_rt[j]);
                    index = j;
                }
            }

            arr_lf[index] = -1;
            arr_rt[index] = -1;

            if(i == k - 1){

                cout << maxi2 << " " << maxi << "\n";
            }
        }

    }

    return 0;
}
