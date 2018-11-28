#include <bits/stdc++.h>
using namespace std;

long long f(long long x){
    return max(x,0LL);
}

int main(){

    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int t;
    long long n , k , a , b , ans;
    map<long long , long long > m;
    scanf("%d",&t);
    for(int T = 1 ; T <= t ; ++T){
        scanf("%lld%lld",&n,&k);
        m.clear();
        m[n] = 1;
        a = n;
        b = -1;

        while(k > m[a] + m[b]){
            k -= m[a];
            k -= m[b];
            //cout << a << ' ' << b << endl;
            //cout << m[a] << ' ' << m[b] << endl;
            if(b == -1){
                if(a&1){
                    m[a>>1] = m[a] + m[a];
                    a >>= 1;
                }else{
                    m[a>>1] = m[a];
                    m[(a-1)>>1] = m[a];
                    b = (a-1)>>1;
                    a >>= 1;
                }
            }else{
                m[a>>1] += m[a];
                m[(a-1)>>1] += m[a];
                m[b>>1] += m[b];
                m[(b-1)>>1] += m[b];
                if(a&1){
                    a = b>>1;
                    b = a-1;
                }else{
                    a = a>>1;
                    b = a-1;
                }
            }
        }

        if(a < b)
            swap(a,b);


        if(k <= m[a])
            printf("Case #%d: %lld %lld\n",T,f(a>>1),f((a-1)>>1));
        else
            printf("Case #%d: %lld %lld\n",T,f(b>>1),f((b-1)>>1));

    }

	return 0;
}
