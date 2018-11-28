#include <bits/stdc++.h>
using namespace std;
void O_o() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
 }
int main()
{
    O_o();
    freopen ("A-small-practice.in","r",stdin);
    int t, ans, k;
    string s;
    cin >> t;
    for(int ii = 1; ii <= t; ii++){
        int n, i;
    cin >> n;
    for(i = n; i > 0; i--){
        int num = i, last;
        bool mono = true;
        last = num % 10;
        while(num != 0 && mono) {
            if(num % 10 > last)
                mono = false;
            else {
                last = num % 10;
                num /=10;
            }

        }
        if(mono)
            break;
    }
    freopen ("A-small-practice.out","a",stdout);
        printf("Case #%d: %d\n", ii, i);

}
    return 0;

}

