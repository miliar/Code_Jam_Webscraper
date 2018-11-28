#include <bits/stdc++.h>
using namespace std;
#define ll          long long
#define MOD         1000000007
#define ll          long long
#define pb          push_back
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define endl        '\n'
#define PI          3.14159265359d
#define sz(x)       (int)x.size()
#define INF         INT_MAX
int main()
{
    freopen("C:/Users/User/Desktop/in.txt","r",stdin);
    freopen("C:/Users/User/Desktop/out.txt","w",stdout);
    int t,T,i,j;
    string s;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>s;
        for(i=0;i<s.length()-1;i++)
            if(s[i]>s[i+1])
            {
                for(j=i+2;s[j];j++)
                    s[j]='9';
                for(;i>=0;i--)
                    if(s[i]>s[i+1])
                    {
                        s[i+1]='9';
                        s[i]--;
                    }
                break;
            }
        cout<<"Case #"<<t<<": ";
        for(i=0;s[i];i++)
            if(s[i]!='0')
                break;
        for(;s[i];i++)
            cout<<s[i];
        cout<<endl;
    }
    return 0;
}
