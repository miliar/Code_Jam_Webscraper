#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int t,cs=0,k;
    string str;
    cin>>t;
    while(t--)
    {
        cs++;
        cin>>str;
        cin>>k;
        int cnt=0;
        int n=str.length();
        for(int i=0;i<=n-k;i++)
        {
            if(str[i]=='-')
            {
                for(int j=0;j<k;j++)
                {
                    if(str[i+j]=='-') str[i+j]='+';
                    else str[i+j]='-';
                }
                cnt++;
            }
        }
        bool fl=true;
        for(int i=0;i<n;i++)
        {
            if(str[i]=='-')
                fl=false;
        }
        if(!fl)
            cout<<"Case #"<<cs<<": IMPOSSIBLE\n";
        else
            cout<<"Case #"<<cs<<": "<<cnt<<"\n";\
    }
    return 0;
}
/*
7
--------- 2
Case #1: IMPOSSIBLE
---------- 2
Case #2: 5
-+-+-+-+-+-+-+-+-+-+-+ 3
Case #3: IMPOSSIBLE
-+-+-+-+-+-+-+-+-+-+-+ 2
Case #4: IMPOSSIBLE
*/
