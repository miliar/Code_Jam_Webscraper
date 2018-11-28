#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <iostream>

using namespace std;


const int maxn = 1e5 + 10;
const int MOD = 1e9 + 7;
const double eps = 1e-7;
const int INF = 2e9;

char s[maxn];
int k;

void main_part(){
    scanf("%s",s);
    scanf("%d",&k);
    int len = strlen(s);
    int cnt = 0;
    for (int i = 0; i + k - 1 < len; ++i){
        if (s[i] == '-'){
            for (int j = 0; j < k; ++j){
                int cur = i + j;
                if (s[cur] == '+'){
                    s[cur] = '-';
                }else{
                    s[cur] = '+';
                }
            }
            cnt++;
        }
    }
    for (int i = 0; i < len; ++i){
        if (s[i] == '-'){
            printf("IMPOSSIBLE\n");
            return;
        }
    }
    printf("%d\n",cnt);
    return;

}
int main(){
    freopen("A-large.in.txt","r",stdin);freopen("a.txt","w",stdout);
    int T;
    scanf("%d",&T);
    //cout<<T<<endl;
    for (int cas = 1; cas <= T; ++cas){
        printf("Case #%d: ",cas);
        main_part();
    }
    return 0;
}
