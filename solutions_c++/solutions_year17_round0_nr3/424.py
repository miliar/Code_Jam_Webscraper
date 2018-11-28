#include <iostream>
#include <utility>
using namespace std;
pair<long long,long long> f(long long len,long long K)
{
    long long l,r;
    if(len%2)
        l = len/2, r = len/2;
    else
        l = len/2-1, r = len/2;
    if(K == 1)
        return make_pair(l,r);
    else
    {
        if(l==r)
        {
            if((K-1)%2)
                return f(l,(K-1)/2+1);
            else
                return f(l,(K-1)/2);
        } else
        {
            if((K-1)%2) {
                return f(r, (K - 1) / 2 + 1);
            }
            else {
                return f(l, (K - 1) / 2);
            }
        }
    }
}
int main()
{
    long long n,N,K;
    cin >>n;
    for(int i = 1;i<=n;i++) {
        cin >> N >> K;
        cout << "Case #" << i << ": ";
        pair<long long, long long> ans = f(N, K);
        cout << ans.second << ' ' << ans.first << endl;
    }
}