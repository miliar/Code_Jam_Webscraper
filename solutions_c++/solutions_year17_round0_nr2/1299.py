#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
    ios_base::sync_with_stdio(0);
    int T;
    cerr<<"------ start -----"<<endl;
    cin>>T;
    string n;
    for(int t = 1; t <= T; ++t)
    {
        cerr<<"----- "<< t<<" ------"<<'\n';
        cin>>n;
        auto pn = n;
        for(int j = 1; j < (int)n.size(); ++j)

        {
            if(n[j] < n[j-1])
            {
                --n[j-1];
                for(int i = j--; i < (int)n.size(); ++i)
                    n[i] = '9';
                if(--j<0) j = 0;
            }
        }
        assert(pn >= n);
        if(n[0] == '0')
            n = n.substr(1);
        for(int i = 1; i < (int)n.size(); ++i)
            assert(n[i]>=n[i-1]);
        cout<<"Case #"<<t<<": "<<n<<'\n';
    }
    cerr<<"------ done -----"<<endl;
    return 0;
}
