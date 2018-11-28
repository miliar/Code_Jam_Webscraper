#include<iostream>
#include<fstream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<stack>
#include<map>
#define intt long long
using namespace std;
const int MX=2e5+10;
int ans[MX];
main()
{
//    ifstream cin("A-large.in");
//    ofstream cout("A-large.out");
    int test=0;
//    for(int i=2;i<=1e3;i++)
//    {
//        for(int k=2;k<=i;k++)
//        {
//            test=max(test,(i-k+1)*k);
//
//        }
//    }
//    cout<<test<<endl;
    cin>>test;
    string s;
    int k;
    for(int ii=1;ii<=test;ii++)
    {
        cin>>s>>k;
        int len=s.size(),res=0;
        for(int i=0;i<len;i++)
            ans[i+1]=(s[i]=='+');
        for(int i=1;i+k-1<=len;i++)
        {
            if(ans[i]==0)
            {
                int cnt=k,ind=i;
                while(cnt--)
                {
                    ans[ind]=(ans[ind]+1)%2;
                    ind++;
                }
                res++;
            }
        }
        int ok=1;
        for(int i=1;i<=len;i++)
            ok=min(ok,ans[i]);
        cout<<"Case #"<<ii<<": ";
        if(ok==0) cout<<"IMPOSSIBLE\n";
        else cout<<res<<"\n";
    }

}

/*
250500*100=
+-+++++++

-++++++++
+++++++-+
*/
