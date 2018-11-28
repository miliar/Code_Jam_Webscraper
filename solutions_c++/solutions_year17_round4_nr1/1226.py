#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int A[10];

int main()
{
    ios_base::sync_with_stdio(0);
    int T;
    cerr<<"------ start -----"<<endl;
    cin>>T;
    for(int t = 1; t <= T; ++t)
    {
        cerr<<"----- "<< t<<" ------"<<'\n';

        memset(A, 0, sizeof(A));
        int n, p;
        cin>>n>>p;
        for(int i = 0; i < n; ++i)
        {
            int inp;
            cin>>inp;
            ++A[inp%p];
        }

        int ans = A[0];
        if(p == 2)
        {
            ans += A[1]/2 + bool(A[1]%2);
        }
        else if(p == 3)
        {
            int mi = min(A[1], A[2]);
            int ma = max(A[1], A[2]);
            ans += mi;
            ma -= mi;
            ans += ma/3 + bool(ma%3);
        }
        else
        {
            ans += A[2]/2;
            int mi = min(A[1], A[3]);
            int ma = max(A[1], A[3]);
            ans += mi;
            ma -= mi;
            if(A[2]%2)
            {
                ++ans;
                ma -= 2;
                ma = max(ma, 0);
            }
            ans += ma/4 + bool(ma%4);
        }

        cout<<"Case #"<<t<<": "<<ans<<'\n';
    }
    cerr<<"------ done -----"<<endl;
    return 0;
}
