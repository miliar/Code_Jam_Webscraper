// aarifshuvo   ``CSEJU

#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define SZ(x) ((int)(x).size())
#define scl(x) scanf("%lld", &x)
#define scll(x,y) scanf("%lld %lld", &x, &y)
#define all(x) (x).begin(),(x).end()
#define mem(a,d) memset(a,d,sizeof a)
#define REP(i,n) for(int i=0;i<n;i++)
#define REV(i,n) for(int i=n-1;i>=0;i--)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define pri(a) cout<<a<<endl
#define prii(a,b) cout<<a<<" "<<b<<endl
using namespace std;

#define inf 12345678912

int main()
{
   // freopen("D:/gjam17/inp.txt", "r", stdin);
   // freopen("D:/gjam17/out.txt", "w", stdout);

    ll i,t,cs=0,k;
    string s,tmp;
    scl(t);
    while(t--)
    {
        cin>>s;
        scl(k);

        tmp = s;
        bool fl = 1, fl2=1;
        ll cnt=0, cnt2=0;

        i=0;
        while(i+k<=SZ(s))
        {
            if(s[i]=='-')
            {
                cnt++;
                REP(j,k)
                {
                    if(s[i+j]=='+') s[i+j]='-';
                    else s[i+j]='+';
                }
            }
            i++;
        }
        for(; i<SZ(s); i++) if(s[i]=='-') fl=0;
//
//        pri(s);

        reverse(all(tmp));
//        pri(tmp);
        i=0;

        while(i+k<=SZ(tmp))
        {
            if(tmp[i]=='-')
            {
                cnt2++;
                REP(j,k)
                {
                    if(tmp[i+j]=='+') tmp[i+j]='-';
                    else tmp[i+j]='-';
                }
            }
            i++;
        }

        for(; i<SZ(tmp); i++) if(tmp[i]=='-') fl2=0;
//        pri(tmp);
//      for(; i<SZ(s); i++) if(s[i]=='-') fl=0;
////
////
////        for(i=0; i<=SZ(tmp)-k;i++)
////        {
////            cnt2++;
////            if(tmp[i]=='-')
////            {
////                for(int j=0; j<k; j++)
////                {
////                    tmp[i+j] = '+';
////                }
////                i+=k;
////                i--;
////            }
////            prii(i,tmp[i]);
////        }

//

        printf("Case #%lld: ", ++cs);
        if(fl==0 and fl2==0) puts("IMPOSSIBLE");
        else
        {
            if(fl==1 and fl2==1)  printf("%lld\n", min(cnt,cnt2));
            else if(fl==1) printf("%lld\n", cnt);
            else printf("%lld\n", cnt2);
        }
    }
    return 0;
}
