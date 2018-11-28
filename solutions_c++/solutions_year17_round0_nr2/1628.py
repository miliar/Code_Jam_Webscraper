#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=(int)a;i<=(int)b;i++)
#define rip(i,a,b) for(int i=(int)a;i>=(int)b;i--)
#define ll long long
#define MOD 1000000007
#define N 200005
#define f first
#define s second
#define pb push_back
#define pii pair<int,int>
#define matrix vector<vector<ll>>
#define PI acos(-1)
#define INF 10000000
#define LSOne(S) (S & (-S))
int main() {
   freopen("/home/vikhyat/Desktop/in.txt","r",stdin);
   freopen("/home/vikhyat/Desktop/out.txt","w",stdout);
   // ios_base::sync_with_stdio(false);
//	cin.tie(0);
	//cout.tie(0);
    int t;
    cin>>t;
    rep(_,1,t)
    {
        cout<<"Case #"<<_<<": ";
        string s;
        cin>>s;
        int l=s.length();
        rep(i,1,l-1)
        {
            if(s[i]<s[i-1])
            {
                int j=i-1;
                while(j>=0&&s[j]==s[i-1])
                j--;
                j++;
                s[j]=char(s[i-1]-1);
                rep(k,j+1,l-1)
                s[k]='9';
                break;
            }
        }
        int i=0;
        while(s[i]=='0')
        i++;
        rep(j,i,l-1)
        cout<<s[j];
        cout<<endl;

    }
    return 0;
}
