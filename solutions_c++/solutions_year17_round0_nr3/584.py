#include<bits/stdc++.h>
#define y0 asdasdasdsas
#define y1 asdsadasdasd
using namespace std;

map<long long, long long, greater<long long> > s;

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    cin.tie(0);ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    for(int test=1;test<=T;test++)
    {
        printf("Case #%d: ",test);
        long long n, k;
        cin >> n >> k;
        s.clear();
        s[n]=1;
        while(true)
        {
            pair<long long,long long> p = *s.begin();
            s.erase(s.begin());
            long long len = p.first;
            if(k<=p.second)
            {
                if(len%2)
                    printf("%lld %lld\n",(len-1)/2,(len-1)/2);
                else
                    printf("%lld %lld\n",len/2,len/2-1);
                break;
            }
            else
            {
                k -= p.second;
                s[len/2] += p.second;
                if(len%2)
                    s[len/2] += p.second;
                else
                    s[len/2-1] += p.second;
            }
        }
    }

}

