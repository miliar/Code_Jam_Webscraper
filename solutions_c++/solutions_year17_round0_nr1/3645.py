#include <bits/stdc++.h>

//#define f cin
//#define g cout
using namespace std;
ifstream f("d.in");
ofstream g("d.out");

const int NMax = 1003;

int t,c,k;
int v[NMax];
char str[NMax];

int main()
{
    f >> t;
    for(int co = 1; co <= t; ++co){
        f >> str >> k;
        int n = strlen(str);
        for(int i = 0; i < n; ++i){
            if(str[i] == '-'){
                v[i + 1] = 0;
            }else
                v[i + 1] = 1;
        }

        int ans1 = 0;

        for(int i = 1; i <= n - k + 1; ++i){

            if(v[i] == 0){
                ans1++;
                for(int j = i; j <= i + k - 1; ++j){
                    v[j] = 1 - v[j];
                }
            }
        }
        int ok = 0;
        for(int i = 1; i <= n; ++i){
            if(v[i] == 0){
                ok = 1;
            }
        }
        if(ok == 1){
            g << "Case #" << co << ": " << "IMPOSSIBLE" << '\n';
        }else{
            g << "Case #" << co << ": " << ans1 << '\n';
        }
    }
    return 0;
}
