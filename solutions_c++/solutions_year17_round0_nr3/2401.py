#include <bits/stdc++.h>

using namespace std;

#define fo "A.out"

int main()
{
    //freopen(fo,"w",stdout);
    int T; cin >> T;
    int test=0;
    while (T--)
    {
        long long N,K;
        test++;
        cin >> N >> K;
        K--;
        long long L=(N-1)/2;
        long long R=N-1-L;
        long long slL=1, slR=1;
        while (K>slL+slR)
        {
            K-=slL+slR;
            if (L==R)
            {
                L=(L-1)/2;
                R=R-1-L;
                slL*=2;
                slR*=2;
            }
            else
            if ((L-1)%2)
            {
                slR=slR*2+slL;
                L=(L-1)/2;
                R=(R-1)/2;
            }
            else
            {
                slL=slL*2+slR;
                L=(L-1)/2;
                R=L+1;
            }
        }
        cout << "Case #" << test << ": ";
        if (K==0) cout << R << " " << L;
        else if (K>slR) cout << L-1-(L-1)/2 << " " << (L-1)/2;
        else cout << R-1-(R-1)/2 << " " << (R-1)/2;
        cout << '\n';
    }
}
