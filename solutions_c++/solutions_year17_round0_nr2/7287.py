#include<bits/stdc++.h>
using namespace std;

typedef long long int ll;

ll tidy_build(ll num){
    bool f = true;
    int sz;
    char s[20];
    ll tidy, last;

    sprintf(s, "%lld", num);
    tidy = last = 0;
    sz = strlen(s);

    for(int i=0; i<strlen(s); i++) {
        tidy*=10;
        if(!f) continue;
        if(last <= s[i]-'0') {
            last = s[i]-'0';
            tidy+=last;
        }
        else f = false;
    }
    return ((f == true)?tidy:tidy_build(tidy-1));
}

int main()
{
    ll s;
    int n;
    scanf("%d", &n);

    for(int C=1; C<=n; C++) {
       scanf("%lld", &s);
       printf("Case #%d: %lld\n", C, tidy_build(s));
    }
}

