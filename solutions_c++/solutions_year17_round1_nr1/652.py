#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

string A[25];

int main()
{
    ios_base::sync_with_stdio(0);
    int T;
    cerr<<"------ start -----"<<endl;
    cin>>T;
    for(int t = 1; t <= T; ++t)
    {
        cerr<<"----- "<< t<<" ------"<<'\n';
        int r, c;
        cin>>r>>c;
        for(int i = 0; i < r; ++i)
        {
            cin>>A[i];
            cerr<<A[i]<<'\n';
        }
        for(int i = 0; i < r; ++i)
        {
            for(int j = 0; j < c; ++j)
            {
                if(A[i][j] != '?')
                {
                    for(int l = j-1; l >= 0 && A[i][l]=='?'; --l)
                        A[i][l] = A[i][j];
                }
                else if(j > 0)
                {
                    A[i][j] = A[i][j-1];
                }
            }
        }
        for(int i = 1; i < r; ++i)
        {
            for(int j = 0; j < c; ++j)
            {
                if(A[i][j] == '?')
                    A[i][j] = A[i-1][j];
            }
        }
        for(int i = r-2; i >= 0; --i)
        {
            for(int j = 0; j < c; ++j)
            {
                if(A[i][j] == '?')
                    A[i][j] = A[i+1][j];
            }
        }
        cout<<"Case #"<<t<<":\n";
        for(int i = 0; i < r; ++i)
        {
            for(int j = 0; j < c; ++j)
                assert(A[i][j] != '?');
            cout<<A[i]<<'\n';
        }
    }
    cerr<<"------ done -----"<<endl;
    return 0;
}
