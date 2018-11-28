#include<bits/stdc++.h>
using namespace std;

int main(){
    //freopen("a.txt", "r", stdin);
    //freopen("asmallout.txt", "w", stdout);
    int t, tc, k, lmt, l, flag, i, j, st, a[1099], cnt, ans, loop, c;
    char s[1099];
    scanf("%d", &tc);
    for(t = 1; t <= tc; t++){
        cin >> s >> k;
        l = strlen(s);
        for(i = 0; i < l; i++){
            if(s[i] == '+'){
                a[i + 1] = 1;
            }
            else if(s[i] == '-'){
                a[i + 1] = 0;
            }
        }

        for(i = 1, ans = 0, cnt = 0; i <= l; i++){
            if(a[i] == 0){
                if(cnt == 0){
                    st = i;
                }
                cnt++;
            }
            else{
                if(cnt >= k){
                    lmt = cnt/k;
                    lmt = lmt*k;
                    for(j = st; j < st + lmt; j++){
                        a[j] = 1;
                    }
                    ans += (lmt/k);
                    //printf("333\n");
                }
                cnt = 0;
            }
        }
        if(cnt >= k){
            lmt = cnt/k;
            lmt = lmt*k;
            for(j = st; j < st + lmt; j++){
                a[j] = 1;
            }
            //printf("222\n");
            ans += (lmt/k);
        }

        /*for(int f = 1; f <= l; f++){
            printf("%d", a[f]);
        }
        printf("\n");*/

        for(i = 1, cnt = 0, loop = 0, flag = 1; i <= l; i++, loop++){
            if(a[i] == 0 && i <= l - k + 1){
                for(j = i; j < i + k; j++){
                    a[j] = (a[j] == 0)?1:0;
                }
                i = 1;
                ans++;
                cnt = 0;
                //for(int f = 1; f <= l; f++){
                    //printf("%d", a[f]);
                //}
                //printf("\n");
            }
            else{
                cnt++;
            }
            if(cnt == l) break;
            if(loop == 1000){flag = 0;break;}
        }

        for(i = 1, c = 0; i <= l; i++){
            if(a[i] == 0){
                c = 1;
                break;
            }
        }
        if(!flag || c)
            printf("Case #%d: IMPOSSIBLE\n", t, ans);
        else
            printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
