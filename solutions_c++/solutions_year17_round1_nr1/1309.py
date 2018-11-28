#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <map>
#include <algorithm>
#include <set>
///!AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
typedef __int128_t Int;
using namespace std;
void solve()
{
    char arr[26][26];
    int R,C;
    cin>>R>>C;
    for(int i=0;i<R;i++)
    {
        //for(int j=0;j<C;j++)
        //{
            cin>>arr[i];//[j];
        //}
    }
    for(int i=0;i<R;i++)
    {
        char cur=arr[i][0];
        for(int j=1;j<C;j++)
        {
            char N=arr[i][j];
            if(N!='?'){
                if(N!=cur)
                {
                    if(cur=='?')
                    {
                        for(int k=j;k>=0;k--)
                            arr[i][k]=N;
                    }
                    cur=N;
                }
            }
            else
            {
                arr[i][j]=cur;
            }
        }
    }

    for(int i=0;i<C;i++)
    {
        char cur=arr[0][i];
        for(int j=1;j<R;j++)
        {
            char N=arr[j][i];
            if(N!='?'){
                if(N!=cur)
                {
                    if(cur=='?')
                    {
                        for(int k=j;k>=0;k--)
                            arr[k][i]=N;
                    }
                    cur=N;
                }
            }
            else
            {
                arr[j][i]=cur;
            }
        }
    }
    for(int i=0;i<R;i++)
    {
        cout<<endl;
        for(int j=0;j<C;j++)
        {
            cout<<arr[i][j];
        }
    }
}
int main()
{
    freopen("A-large(2).in","r",stdin);
    freopen("out.txt","w+",stdout);

    int T;
    cin>>T;
    //cerr<<"Test ";
    for(int iT=0;iT<T;iT++)
    {
        cout<<"Case #"<<iT+1<<": ";
        solve();
        cout<<"\n";
    }
    return 0;
}
