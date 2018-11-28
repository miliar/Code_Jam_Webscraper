#include <bits/stdc++.h>

using namespace std;

int const N = 105;

long long n;
long long Pow[N];
int a[N];

int main()
{
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    Pow[0] = 1;
    for(int i=1; i<=18; i++)
        Pow[i] = Pow[i-1] * 10;
    for(int _=1; _<=T; _++){
        cout << "Case #" << _ << ": ";

        int cnt = 0;
        cin >> n;
        n++;
        while(n){
            a[++cnt] = n % 10;
            n /= 10;
        }
        reverse(a+1, a+cnt+1);

        long long Num = 0, ans = 0;
        for(int i=1; i<=cnt; i++){
            if(a[i]-1 >= a[i-1]){
                ans = (Num * 10 + a[i] - 1) * Pow[cnt-i] + Pow[cnt-i] - 1;
                Num = Num * 10 + a[i];
            }
            else{
                if(a[i] == a[i-1]){
                    Num = Num * 10 + a[i];
                }
                else
                    break;
            }
        }
        cout << ans << endl;
    }
}
