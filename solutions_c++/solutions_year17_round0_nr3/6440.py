#include<bits/stdc++.h>
using namespace std;

int m[10000];

int main(){
    freopen("c1.txt", "r", stdin);
    freopen("c1out.txt", "w", stdout);
    int t, tc, n, k, i, j, cnt, diff, st, ed, cur, l, pos;
    //vector <int> v;
    scanf("%d", &tc);
    for(t = 1; t <= tc; t++){
        scanf("%d %d", &n, &k);
        for(i = 2; i <= n + 1; i++){
            m[i] = 0;
        }
        m[1] = 1, m[n + 2] = 1;
        l = n + 2;
        //v.clear();
        for(i = 1; i <= k; i++){
            for(j = 1, st = 1, ed = 1,cnt = 0, diff = 0; j <= l; j++){
                if(m[j] == 1){
                    if(diff < cnt){
                        diff = cnt;
                        st = cur;
                        ed = j - 1;
                        cur = j + 1;
                    }
                    cnt = 0;
                }
                else{
                    if(cnt == 0) cur = j;
                    cnt++;
                }
            }
            if(diff & 1){
                pos = st + (((diff + 1)/2) - 1);
            }
            else{
                pos = st + ((diff/2) - 1);
            }
            m[pos] = 1;
            //v.push_back(pos);
        }

        int ls, rs;
        for(i = pos + 1, cnt = 0; i <= l; i++){
            if(m[i] == 1){
                rs = cnt;
                break;
            }
            else{
                cnt++;
            }
        }

        for(i = pos - 1, cnt = 0; i > 0; i--){
            if(m[i] == 1){
                ls = cnt;
                break;
            }
            else{
                cnt++;
            }
        }

        /*for(i = 0; i < k; i++){
            cout << v[i];
            if(i == k - 1) printf("\n");
            else printf(" ");
        }
        cout << pos << endl;
        cout << ls << endl;
        cout << rs << endl;*/
        printf("Case #%d: %d %d\n", t, max(ls, rs), min(ls, rs));
    }
    return 0;
}
