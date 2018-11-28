#include <bits/stdc++.h>
#define maxx 100005
#define inf 2000000000
#define mod 1000000007
#define pii pair<int,int>
#define piii pair<pii,pii>
#define pli pair<long long,int>
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

int t, n;
char s[1234];
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    in(t);
    for(int cases = 1; cases <= t; cases ++){
        inch(s);
        n = strlen(s);
        printf("Case #%d: ",cases);
        for(int i = 0; i < n - 1; i++){
            if(s[i] > s[i + 1]){
                s[i]--;
                for(int j = i + 1; j < n; j++){
                    s[j] = '9';
                }
                for(int j = i; j > 0; j--){
                    if(s[j - 1] > s[j]){
                        s[j - 1]--;
                        s[j] = '9';
                    }
                }
            }
        }
        int i = 0;
        while(s[i] == '0'){
            i++;
        }
        for(; i < n; i++){
            printf("%c",s[i]);
        }
        printf("\n");
    }
    return 0;
}
