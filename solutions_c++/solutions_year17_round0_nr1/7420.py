#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair

typedef long long int ll;
typedef vector< pair<int,int> > vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<long long int> vll;
typedef pair<int,int> pii;

const ll INF= ll (1e18);
const int MOD= 1e9+7;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.in","w",stdout);
    int t;
    cin>>t;
    int n=1;
    while(t--)
    {
        string s;
        int k;
        int cc=0;
        cin>>s>>k;
        int l=s.length();
        for(int i=0;i<=(l-k);i++)
        {
            if(s[i]=='-')
            {
                for(int j=i;j<i+k;j++)
                {
                    //cout<<s[j]<<"s"<<endl;

                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';

                }
                cc++;

            }
        }
        int flag=0;
        //cout<<s<<endl;
        for(int i=0;i<l;i++)
        {
            if(s[i]=='-')
                {
                    flag=1;
                    break;
                }
        }
        if(flag==0)
        {
            cout<<"Case #"<<n<<": "<<cc<<endl;
        }
        else
            cout<<"Case #"<<n<<": IMPOSSIBLE"<<endl;

        n++;



    }

    return 0;

}
