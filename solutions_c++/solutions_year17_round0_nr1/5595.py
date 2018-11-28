#include <iostream>
#include <fstream>
#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <stack>
#include <cstring>
#include <cmath>

#define MN 1000010
#define INF 2147483647
#define PI 3.14159265359
#define pairr pair<int, int>
#define pairrr pair<int, pairr>
#define f first
#define s second
#define pb push_back
#define ll long long
#define MOD 10000007
#define IO ios_base::sync_with_stdio(false); cin.tie();
#define PQT pairr
#define PQL priority_queue<PQT, vector<PQT>, less<PQT> >
#define PQG priority_queue<PQT, vector<PQT>, greater<PQT> >

using namespace std;

string s;
int t,k,i,j,t1,ans;

int main()
{
    IO
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t1;
    for (t=1;t<=t1;t++)
    {
        cin>>s>>k;
        for (i=0;i<=s.length()-k;i++)
        {
            if (s[i]=='-')
            {
                for (j=i;j<i+k;j++)
                {
                    if (s[j]=='-') s[j]='+';
                    else s[j]='-';
                }
                ans++;
            }
        }
        for (;i<s.length();i++)
        {
            if (s[i]=='-')
            {
                ans=-1;
                break;
            }
        }
        cout<<"Case #"<<t<<": ";
        if (ans==-1) cout<<"IMPOSSIBLE\n";
        else cout<<ans<<endl;
        ans=0;
    }
    return 0;
}
