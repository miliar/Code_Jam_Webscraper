#include <bits/stdc++.h>
using namespace std;
#define readfiles freopen("/home/2016/akaba2/CppApplication_1/in.txt","r",stdin);freopen("/home/2016/akaba2/CppApplication_1/out.txt","w",stdout)
#define clr(x,y) memset(x,y,sizeof(x))
#define pb push_back
#define mp make_pair
#define eps (1e-9)
#define oo (0x7fffffff)
#define OO (0x7fffffffffffffff)
#define PI acos(-1)
#define sqr(x) ((x)*(x))
#define moder (1000000007l)
#define ABS(x) ((x>0)?x:-x)
#define LOG2(x) ((log10(x))/(log10(2)))
#define UNSET(n,x) (n&(~(1 << x)))
#define SET(n,x) (n|(1<<x))
typedef long long int ll;
typedef unsigned long long int ull;
#define MAXN 1005ul

void solve() {
    int cases;
    cin>>cases;
    int k = 0;
    while (cases--) {
        k++;
        int num[20] = {0};
        ull n;
        cin>>n;
        int idx = 0;
        while (n) {
            num[idx++] = n % 10;
            n /= 10;
        }
        while (1) {
            int finished = 0;
            int s2f = num[0];
            for (int i = 1; i < 20; i++) {
                if (num[i] <= s2f)
                    s2f = num[i];
                else {
                    num[i]--;
                    for(int j=0;j<i;j++){
                        num[j]=9;
                    }
                    break;
                }
                if (i == 19)
                    finished = 1;
            }
            if (finished)
                break;
        }

        cout<<"Case #"<<k<<": ";
        int first = 0;
        for (int i = 20; i >= 0; i--) {
            if (num[i] != 0) {
                first = 1;
                cout<<num[i];
            } else if (num[i] == 0 && first)
                cout<<"0";
        }
        cout<<"\n";
    }
}

int main() {
#ifndef ONLINE_JUDGE
    //freopen("B-small-attempt0.in","r",stdin);
    //readfiles;
    double begin = clock();
#endif
    solve();
    return 0;
#ifndef ONLINE_JUDGE
    printf("%.4f", (clock() - begin) / CLOCKS_PER_SEC);
#endif
}