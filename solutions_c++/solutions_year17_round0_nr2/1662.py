#include <bits/stdc++.h>
using namespace std;

#define sz(v)        ((int)v.size())
#define ll           long long
#define all(v)       (v.begin()) , (v.end())
#define rall(v)      (v.rbegin()) , (v.rend())
#define SetTo(v, a)  memset(v,a,sizeof(v))

bool isTidy(int n)
{
    int prv = 9;
    while(n){
        int a = n%10;
        n /= 10;
        if(a > prv)
            return 0;
        prv = a;
    }
    return 1;
}

long long get(long long num)
{
    char s[100];
    sprintf(s,"%I64d", num);
    int n = strlen(s);

    for(int i=n-2;i>=0;i--){
        if(s[i] > s[i+1]){
            s[i]--;
            for(int j=i+1;j<n;j++)
                s[j] = '9';
        }
    }

    return atoll(s);
}
int main ()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    long long n;
    scanf("%d", &tc);
    for(int test=1;test <= tc ;test++)
    {
        scanf("%I64d", &n);
        printf("Case #%d: %I64d\n", test, get(n));
    }
    return 0;
}
