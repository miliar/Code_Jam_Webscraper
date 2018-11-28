#include <bits/stdc++.h>

using namespace std;

long long n, ar[50];

int dig(long long n)
{
    int c = 0;
    while(n>0){
        c++;
        ar[c] = n%10;
        n /= 10;
    }
    reverse(ar+1, ar+c+1);
    return c;
}

void solve(int y)
{
    scanf("%lld", &n);
    int d = dig(n);
    bool t = false;
    int g;
    long long s = 0;
    for(int i=2;i<=d;i++){
        if(ar[i]<ar[i-1]){
            t = true;
            g = i;
            break;
        }
    }
    g--;
    if(t){
        while(g>1&&ar[g-1]==ar[g])g--;
        ar[g]--;
        for(int i=g+1;i<=d;i++)ar[i] = 9;
    }
    for(long long i=d, k=1;i>=1;i--,k*=10){
        s += ar[i]*k;
    }
    printf("Case #%d: %lld\n", y, s);
}
int t;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B_output_l.txt", "w", stdout);
    scanf("%d", &t);
    for(int i=1;i<=t;i++)solve(i);
    return 0;
}
