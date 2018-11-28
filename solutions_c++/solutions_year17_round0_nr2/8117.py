#include<bits/stdc++.h>
#define Wale_ed ios_base::sync_with_stdio(0);cin.tie(0);
#define ll long long
#define ull unsigned long long
#define ld long double
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.out","w",stdout);
    Wale_ed
    string s,ss;
    int n,i;
    int t;
    cin>>t;
    vector<int> v;
    for (int cas=1; cas<=t; cas++)
    {
        cin>>s;
        cout<<"Case #"<<cas<<": ";
        while(true)
        {
            n=1;
            i=1;
            while(s[i-1]<=s[i]&&i<s.size())
            {
                i++;
                n++;
            }
            if(n==s.size())
            {

                break;
            }
            if(s[i-1]-1=='0')
            {
                ss="";
                for (i=0; i<s.size()-1; i++)
                    ss+='9';
                s=ss;
            }
            else
            {
                s[i-1]--;
                for (i; i<s.size(); i++)
                    s[i]='9';
            }
        }
        cout<<s<<endl;
    }
    return 0;
}
