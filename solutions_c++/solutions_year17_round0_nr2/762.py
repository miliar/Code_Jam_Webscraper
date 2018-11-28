
/*****************************************
Author: lizi
Email: lzy960601@outlook.com
****************************************/
  
#include<bits/stdc++.h>
  
using namespace std;
  
const double eps=1e-10;
const double pi=3.1415926535897932384626433832795;
const double eln=2.718281828459045235360287471352;
  
#define LL long long
#define IN freopen("Bl.in", "r", stdin)
#define OUT freopen("Bl.out", "w", stdout)
#define scan(x) scanf("%d", &x)
#define mp make_pair
#define pb push_back
#define sqr(x) (x) * (x)
#define pr(x) printf("Case %d: ",x)
#define prn(x) printf("Case %d:\n",x)
#define prr(x) printf("Case #%d: ",x)
#define prrn(x) printf("Case #%d:\n",x)
#define lowbit(x) (x&(-x))

string s;
int T;

void solve(int x)
{
    for(int i=x+1;i<s.length();i++)s[i]='9';
    s[x]--;x--;
    while(x>=0 && s[x]>s[x+1])
    {
        s[x+1]='9';
        s[x]--;x--;
    }
}

void pri(string st)
{
    int u=0;
    while(st[u]=='0')u++;
    for(int i=u;i<st.length();i++)cout<<st[i];
    cout<<endl;
}

int main()
{
    IN;OUT;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>s;
        cout<<"Case #"<<t<<": ";
        if(s.length()==1)
        {
            cout<<s<<endl;
            continue;
        }
        for(int i=0;i<s.length();i++)
        {
            if(i==s.length()-1)break;   
            if(s[i]>s[i+1])
            {
                solve(i);
                break;
            }
        }
        pri(s);
    }
    return 0;
}
