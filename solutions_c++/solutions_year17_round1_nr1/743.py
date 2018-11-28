#include <bits/stdc++.h>
#define maxx 100005
#define inf 2000000000
#define mod 1000000007
#define pii pair<int,int>
#define piii pair<pii,pii>
#define pli pair<long long,int>
#define pll pair<long long,long long>
#define f first
#define s second
#define in(x) scanf("%d",&x)
#define IN(x) scanf("%lld",&x)
#define inch(x) scanf("%s",x)
#define indo(x) scanf("%lf",&x)
#define pb push_back

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int t, r, c;
char s[123][123];
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    in(t);
    for(int cases = 1; cases <= t; cases ++){
        in(r); in(c);
        for(int i = 0; i < r; i++){
            inch(s[i]);
        }
        int x = -1, y = -1;
        for(int i = 0; x == -1 && i < r; i++){
            for(int j = 0; j < c; j++){
                if(s[i][j] != '?'){
                    x = i; y = j;
                    break;
                }
            }
        }
        ///cout << x << " " << y << endl;
        for(int j = 0; j < y; j++){
            s[x][j] = s[x][y];
        }

        for(int j = y + 1; j < c; j++){
            if(s[x][j] == '?'){
                s[x][j] = s[x][y];
            }else{
                y = j;
            }
        }
        for(int i = x - 1; i >= 0; i--){
            for(int j = 0; j < c; j++){
                s[i][j] = s[i + 1][j];
            }
        }
        for(int i = x + 1; i < r; i++){
            int last = -1;
            char let;
            for(int j = 0; j < c; j++){
                if(s[i][j] != '?'){
                    for(int l = last + 1; l < j; l++){
                        s[i][l] = s[i][j];
                    }
                    last = j;
                    let = s[i][j];
                }
            }
            if(last == -1){
                for(int j = 0; j < c; j++){
                    s[i][j] = s[i - 1][j];
                }
            }else{
                for(int j = c - 1; j >= 0; j--){
                    if(s[i][j] == '?'){
                        s[i][j] = let;
                    }
                }
            }
        }
        printf("Case #%d:\n",cases);
        for(int i = 0; i < r; i++){
            printf("%s\n",s[i]);
        }
    }
    return 0;
}
