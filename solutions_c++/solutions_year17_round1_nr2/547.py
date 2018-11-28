#include <bits/stdc++.h>

using namespace std;

int n,p;
int t;
int req[55];
int arr[55][55];
int prog[55];

pair<int,int> getrange(int a, int b){
    int k = a * 10 / (b * 11);
    if (k * b * 11 < a * 10) k++;
    int l = a * 10 / (b * 9);
    return make_pair(k,l);
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    for(int test = 1; test <= t; test++){
        cin >> n >> p;
        for (int i = 0; i < n; i++) prog[i]=0;
        for (int i = 0; i < n; i++){
            cin >> req[i];
        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j < p; j++){
                cin >> arr[i][j];
            }
            sort(arr[i], arr[i]+p);
        }
        int ans = 0;
        int s = 1;
        bool b = 0;
        while(1){
            pair<int,int> r = getrange(arr[0][prog[0]], req[0]);
            if (s < r.first) s = r.first;
            else if (s > r.second){
                prog[0]++;
                if (prog[0]==p) break;
                continue;
            }
            int cnt = 55;
            for (int i = 0; i < n; i++){
                pair<int,int> q = getrange(arr[i][prog[i]], req[i]);
                if (s > q.second){
                    prog[i]++;
                    i--;
                    if (prog[i]==p){
                        b = 1;
                        break;
                    }
                    continue;
                }
                int c=0;
                for (int j = 0; prog[i]+j<p; j++){
                    q = getrange(arr[i][prog[i]+j], req[i]);
                    if (q.first <= s && s <= q.second){
                        c++;
                    }
                    else break;
                }
                cnt = min(cnt, c);
            }
            if (b) break;
            ans += cnt;
            for (int i = 0; i < n; i++){
                prog[i] += cnt;
                if (prog[i]>=p) {
                    b=1; break;
                }
            }
            if (b) break;
            s++;
        }
        cout << "Case #" << test << ": " << ans << "\n";
    }
    return 0;
}
