#include<bits/stdc++.h>
#define ll long long
using namespace std;
#define INF 1000000000000

int main()
{
    ifstream cin; cin.open("A-large.in"); ofstream cout; cout.open("fileout.txt"); //comment while testing.
    ll t;
    cin>>t;
    for(int testcase=1;testcase<=t;testcase++)
    {
        // Solve problem
        ll ans=0;
        string s;
        int k;
        cin>>s;
        cin>>k;
        int n=s.length();
        for(int i=0;i<= n-k;i++)
        {
            if(s[i]=='-'){
                for(int j=0;j<k;j++)
                {
                    if (s[i+j] == '+')
                        s[i+j] ='-';
                     else
                        s[i+j] ='+';
                }
                ans++;
            }
        }
        int now=0;
        for(int i=0;i<n;i++)
            if(s[i] == '-')
                now=1;

        if(now==0){
            cout<<"Case #"<<testcase<<": "<<ans<<endl; // answer
        }
        else{
            cout<<"Case #"<<testcase<<": IMPOSSIBLE"<<endl; // answer
        }

    }
    return 0;
}
