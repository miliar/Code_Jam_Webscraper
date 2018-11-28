#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <iostream>

using namespace std;


const int maxn = 1e3 + 10;
const int MOD = 1e9 + 7;
const double eps = 1e-7;
const int INF = 2e9;

int k[maxn],s[maxn];
    int D,n;
bool check(double x){
    for (int i = 0; i < n; ++i){
        if ((D-k[i])*1.0/s[i] > D*1.0/x + 1e-10)return 0;
    }
    return 1;
}

void main_part(){

    scanf("%d%d",&D,&n);
    double max_time = 0;
    for (int i = 0; i < n; ++i){
        scanf("%d%d",&k[i],&s[i]);
        max_time = max(max_time, (D - k[i])*1.0/s[i]);
    }


    printf("%.8f\n",D/max_time);

}
int main(){
    freopen("A-large.in.txt","r",stdin);freopen("a.txt","w",stdout);
    int T;

    scanf("%d",&T);
    //cout<<T<<endl;
    //return 0;
    for (int cas = 1; cas <= T; ++cas){
        printf("Case #%d: ",cas);
        main_part();
    }
    return 0;
}
