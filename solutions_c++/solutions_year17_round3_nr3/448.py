#include <bits/stdc++.h>

#define ff first
#define ss second
#define mp make_pair

using namespace std;

typedef long long ll;

const double PI = acos(-1);

double v[55];

int main(){
    int T;

    scanf("%d", &T);

    for(int t = 1; t <= T; t++){
        int n,k;
        double u;

        scanf("%d%d%lf", &n,&k,&u);

        for(int i = 0; i < n; i++)
            scanf("%lf", &v[i]);
        v[n] = 1.0;

        sort(v, v+n);

        for(int i = 0; i < n; i++){
            double goal = v[i+1] - v[i];
            if(goal*(i+1) <= u){
                u -= goal*(i+1);
                for(int j = 0; j <= i; j++)
                    v[j] = v[i+1];
            }
            else{
                for(int j = 0; j <= i; j++)
                    v[j] += u/(i+1);
                break;
            }
        }

        double  ans = 1;
        for(int i = 0; i < n; i++)
            ans *= v[i];

        printf("Case #%d: %.15lf\n",t,ans);
    }
    
    return 0;
}