#include <bits/stdc++.h>

#define ll long long

using namespace std;

char buf[100];
char bufcpy[100];

int main()
{
    #ifdef FILEIO
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    //ios_base::sync_with_stdio(false);

    int T;
    scanf("%d\n", &T);
    for (int test = 1; test <= T; test++) {
        gets(buf);
        int n = strlen(buf);
//continue;
        ll ans = 0;
        for (int i = 0; i <= n; i++) {
            strcpy(bufcpy, buf);
            if (bufcpy[i] != '0' && i < n) {
                bufcpy[i]--;
                for (int j = i+1; j < n; j++)
                    bufcpy[j] = '9';
            }

            char max_val = '9';
            for (int j = n-1; j >= 0; j--) {
                if (bufcpy[j] < max_val)
                    max_val = bufcpy[j];
                bufcpy[j] = max_val;
            }

            ans = max(ans, atoll(bufcpy));
        }

        cout << "Case #" << test << ": " << ans << endl;
    }
    
}
