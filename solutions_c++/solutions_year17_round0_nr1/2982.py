#include <bits/stdc++.h>
using namespace std;

const int N = 1005;
char str[N];
int v[N];


int main(){

    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int t , k , n , ans , s , i;
    bool flag;
    scanf("%d",&t);
    for(int T = 1 ; T <= t ; ++T){
        ans = 0;
        s = 0;
        flag = true;
        scanf("%s%d",str,&k);
        n = strlen(str);
        fill(v , v+n , 0);
        for(i = 0 ; i < n-k+1 ; i++){
            s += v[i];
            int cur = ((str[i] == '+') + s)&1;
            if(cur == 1)continue;
            ans++;
            s++;
            v[i + k] = -1;
        }


        for(;i < n ; i++){
            s += v[i];
            int cur = ((str[i] == '+') + s)&1;
            if(cur != 1){
                flag = false;
                break;
            }
        }

        if(flag)
            printf("Case #%d: %d\n",T,ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",T);
    }

	return 0;
}
