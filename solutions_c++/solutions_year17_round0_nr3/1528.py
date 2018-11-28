#include<stdio.h>
#include<map>
using namespace std;
#define lint long long
lint n, k;
map<lint,lint> s;
int main()
{
    lint tt, T, t;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld", &T);
    map<lint,lint>::reverse_iterator rit;
    map<lint,lint>::iterator x1, x2;
    for(tt=1; tt<=T; ++tt)
    {
        scanf("%lld%lld", &n, &k);
        s.clear();
        s.insert(pair<lint,lint>(n, 1));
        t=0;
        while(true)
        {
            rit = s.rbegin();
            lint x = rit->first;
            lint cnt = rit->second;
            t += cnt;
            if(t >= k)
            {
                printf("Case #%lld: %lld %lld\n", tt, x/2, (x-1)/2);
                break;
            }
            s.erase(x);
            x1 = s.find(x/2);
            if(x1 != s.end())
                x1->second += cnt;
            else s.insert(pair<lint,lint>(x/2, cnt));
            x2 = s.find((x-1)/2);
            if(x2 != s.end())
                x2->second += cnt;
            else s.insert(pair<lint,lint>((x-1)/2, cnt));
        }
    }
}
