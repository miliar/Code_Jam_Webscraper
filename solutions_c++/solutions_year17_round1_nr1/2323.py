#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

typedef long long ll;
#define S(a) scanf("%d",&a)
#define LS(a) scanf("%lld",&a)
#define FOR(i,a,b) for(int i = a, i <= b;++i)
#define DOW(i,b,a) for(int i = b; i >= a;--i)
const ll INF = 1e17;
const ll MOD = 1e9 + 7;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
     cin >>(t);
    for(int tc = 1; tc <= t; ++tc)
    {
        int n,m;
        cin >> n >> m;
        char mat[n][m];
        vector<int> row(n,0);
        getchar();
        for(int i  = 0 ; i < n; ++i)
        {
             for(int j = 0 ; j < m;j++)
                cin >> mat[i][j];


        }

        for(int i  = 0 ; i < n; ++i)
        {

            for(int j = 0 ; j < m; j++)
            {
                if(mat[i][j] != '?')
                {
                    row[i] = 1;
                    break;

                }
            }


        }


        for(int i = 0 ; i < n; ++i)
        {
            if(row[i])
            {
                char last = '0';
                for(int j = 0 ; j < m; ++j)
                {

                    if(mat[i][j] == '?')
                    {
                        if(last != '0')
                        {

                            mat[i][j] = last;

                        }
                        else
                        {

                            int k = j + 1;

                            while(k < m )
                            {
                                if(mat[i][k] != '?')
                                {
                                    last = mat[i][k];
                                    break;
                                }
                                k++;

                            }
                            mat[i][j] = last;


                        }


                    }else last = mat[i][j];
                }
            }

        }

        for(int i = 0 ; i < n;++i){
            if(!row[i]){

               for(int j = 0 ; j < m;++j){

                  int k = i;
                  while(!row[k] && k >=0) k--;
                  if(k>=0){
                  mat[i][j] = mat[k][j];
                  continue;
                  }

                  while(!row[k] && k < n) k++;
                  if(k < n){
                  mat[i][j] = mat[k][j];
                  }
               }

            }


        }
        cout << "Case #" << tc << ":\n";
        for(int i = 0 ; i < n;++i){ for(int j = 0 ; j < m;j++)cout << mat[i][j];
        cout << '\n';}
    }

    return 0;
}

