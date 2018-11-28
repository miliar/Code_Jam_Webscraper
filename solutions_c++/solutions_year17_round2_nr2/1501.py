#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;

int n;
int num[6], ans[1010], tmp[1010], is_ans;
int cnt = 0;
bool cmp(int a, int b){
    return num[a] > num[b];
}


void DFS(int now, int pre, int first){
    if(now == n){
        for(int i = 0; i < n; i++){
            ans[i] = tmp[i];
        }
        is_ans = 1;
        return;
    }
    ++cnt;
    if(cnt > 10000000){
        return;
    }
    int can[6], cc = 0;
    int d;
    for(int i = 0; i < 6; i++){
        if(num[i] > 0 && i != pre){
            d = (i-pre+6) % 6;
            if(d == 0 || d == 1 || d == 5){
                continue;
            }
            if(now == n - 1){
                d = (i-first+6) % 6;
                if(d == 0 || d == 1 || d == 5){
                    continue;
                }
            }
            can[cc++] = i;
        }
    }
    sort(can, can + cc, cmp);
    for(int i = 0; i < cc && is_ans == 0; i++){
        tmp[now] = can[i];
        --num[can[i]];
        DFS(now+1, can[i], first);
        ++num[can[i]];
    }

}



int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    
    char fstr[] = "ROYGBV";

    for(int f = 1; f <= T; f++){
        cin >> n;
        for(int i = 0; i < 6; i++){
            cin >> num[i];
        }
        is_ans = 0;
        cnt = 0;
        for(int i = 0; i < 6; i++){
            if(num[i] > 0){
                tmp[0] = i;
                num[i]--;
                DFS(1, i, i);
                break;
            }
        }
        cout << "Case #" << f << ": ";
        if(is_ans == 0){
            cout << "IMPOSSIBLE" << endl;
        }else{
            for(int i = 0; i < n; i++){
                //cout << ans[i];
                printf("%c", fstr[ans[i]]);
            }
            cout << endl;
        }
    }

    return 0;
}
