#include <map>
#include <set>
#include <stack>
#include <cmath>
#include <queue>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define FOR(i, j, k) for(int i = j;i<= k;i++)
#define ll long long
const int maxn  =50;
void fastmod(int a, int b)
{
    while(b)
    {
        b >>= 1;
        a *= a ;
        a %= 100;
    }
}
int T;
int N,P;
int q[maxn][maxn];
int p[maxn];

int R[maxn];
int main(){
    freopen("/Users/hermione/Desktop/in.txt","r",stdin);
    freopen("/Users/hermione/Desktop/temp.txt", "w", stdout);
    cin >> T;
    
    FOR(z, 1, T){
        cin >> N >> P;
        fastmod(1,1);
        for(int i = 1;i <= N;i++)  cin >> R[i];
        fastmod(1,2);
        for(int i = 1;i <= N;i++){
            for(int j = 1;j <= P;j++)
                cin >> q[i][j];
        
            sort(q[i] + 1,q[i] + 1 + P);
        }
        fastmod(2,1);
        for(int i = 1;i <= N;i++)
            p[i] = 1;

        int ans = 0;
        fastmod(3,4);
        for(int s = 1;s <= 1000000;s++){
            bool flag = 1;
            for(int i = 1;i <= N;i++){
                ll d = ceil(0.9 * s * R[i]);
                //cout << d << endl;
                while(p[i] <= P && q[i][p[i]] < d) p[i]++;
                d = ceil(1.1 * s * R[i]);
                ll dd = floor(1.1 * s * R[i]);
                if(q[i][p[i]] > dd || p[i] > P) flag = false;
            }
            if(flag){
                ans++;
                s = s - 1;
                for(int i = 1;i <= N;i++) p[i]++;
            }
            bool f = 0;
            for(int i = 1;i <= N;i++)
                if(p[i] > P)
                    f = 1;
            if(f) break;
        }
        printf("Case #%d: ",z);
        printf("%d\n", ans);
    }
    return 0;
}