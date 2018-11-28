#include <bits/stdc++.h>

using namespace std;

#define foru(i,a,b) for(int i=a; i<=b; i++)
#define ford(i,a,b) for(int i=a; i>=b; i--)
#define reset(a,b) memset(a,b,sizeof(a))
#define ha return 0
typedef long long int64;

string s;
int64 n, m;

string convert(int64 a){
    string ans="";
    while (a>0){
        int r=a%10;
        ans=char(r+48)+ans;
        a/=10;
    }
    return ans;
}

int main()
{
    freopen("input.inp","r",stdin);
    freopen("output.out","w",stdout);
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    int ntest;
    cin>>ntest;
    foru(test,1,ntest){
        cin>>n;
        s=convert(n);
        m=s.size();

        int tg;
        while (true){
            tg=-1;
            foru(i,1,m-1) if (s[i-1]>s[i]){
                tg=i;
                break;
            }
            if (tg==-1) break;
            s[tg-1]--;
            foru(i,tg+1,m) s[i-1]='9';
        }

        cout<<"Case #"<<test<<": ";
        foru(i,1,m) if (s[i-1]!='0'){
            tg=i;
            break;
        }

        foru(i,tg,m) cout<<s[i-1];
        cout<<"\n";
    }

    return 0;
}
