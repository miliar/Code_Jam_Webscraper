#include <stdio.h>
#include <limits>
#include <algorithm>
using namespace std;
int main(){
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int T;
    scanf("%d", &T);
    int i = 0;
    long double d;
    int n;
    int j;
    long double k;
    long double s;
    long double ans;
    while (i < T){
        scanf("%Lf %d", &d, &n);
        j = 0;
        ans = numeric_limits<long double>::max();
        while (j < n){
            scanf("%Lf %Lf", &k, &s);
            ans = min(ans, d*s/(d-k));
            j++;
        }
        i++;
        printf("Case #%d: %.6Lf\n", i, ans);
    }
}