#include<iostream>
#include<bits/stdc++.h>
#include<vector>
#include<map>
#include<cstdio>
#include<algorithm>
#define ll long long int
#define loop(i,n) for(ll i=0;i<n;i++)
#define loop2(i,a,b) for(ll i=a;i<b;i++)
#define mp(a,b) make_pair(a,b)
using namespace std;
bool compare(string a , string b)
{
    int an=a.size();
    int bn=b.size();
    if(an<bn)
    {
        return true;
    }
    if(bn<an)
    {
        return false;
    }
    return a<=b;

}

bool isSorted(string s)
{
    int n=s.length();
    for(int i=0;i<n-1;i++)
    {
        if(s[i]>s[i+1])
            return false;
    }
    return true;
}

ll power(ll a ,ll b)
{

    ll c=0;
    if(b==1)
        return a;
    if(b&1)//odd
    {
        c = power(a,b-1);
        return a*c;
    }
    else
    {
        c=power(a,b/2);
        return c*c;
    }

}
int main()
{

cin.tie(0);
cout.tie(0);

cin.sync_with_stdio(false);
cout.sync_with_stdio(0);

freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);






int t;
cin>>t;
for(ll te=1;te<=t;te++)
{

    string s;
    cin>>s;
    int n=s.length();
    string ans=s;



        if(isSorted(s))
          {
            cout<<"Case #"<<te<<": "<<s<<endl;
            continue;

          }



            int start=0;
            for(int i=0;i<n-1;i++)
            {
                if(s[i]>s[i+1])
                {
                ans[start]--;
                for(int j=start+1;j<n;j++)
                {
                    ans[j]='9';
                }
                break;
                }
                else if(s[i]<s[i+1])
                {
                    start=i+1;
                }

            }



            if(ans[0]=='0')
            {
                cout<<"Case #"<<te<<": ";
                for(int i=1;i<n;i++){
                    cout<<ans[i];
                }
                cout<<endl;
            }
            else{

                cout<<"Case #"<<te<<": "<<ans<<endl;

            }

    }






    return 0;
}




