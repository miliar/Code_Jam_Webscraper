#include <stdio.h>
#include <stdarg.h>
#define DEBUG 0
#if  DEBUG >0 
#  define debug_print(msg) stderr_printf msg
#else
#  define debug_print(msg) (void)0
#endif

void
stderr_printf(const char *fmt, ...)
{
  va_list ap;
  va_start(ap, fmt);
  vfprintf(stderr, fmt, ap);
  va_end(ap);
}
#include <bits/stdc++.h>
        #define s(a) cin >> a;
        #define s2(a,b) cin >> a>> b;
        #define s3(a,b,c) cin >> a>> b>> c;
        #define s4(a,b,c,d) cin >> a>> b >> c >> d;
        #define sp(b) cout << b << "\n";
        #define sp2(b,c) cout << b << " "<<c <<endl; 
        #define sp3(a,b,c) cout <<a <<" "<< b << " "<<c <<endl; 
        #define p(a) ////printf("%lld\n",a);
        #define p2(a,b) ////printf("%lld %lld",a,b);
        #define pm(a) ////printf("a\n");
        #define test(t) while(t>0)
        #define sl(a) a.length()
        #define f(a,b,c) for(a=b;a<c;a++)
        #define fr(a,b,c) for(a=c-1;a>=b;a--)
        #define v(a,b) vector<a> b;
        #define pb(a,b) a.push_back(b);
        #define ll long long
        #define mem(a,b) memset(a,b,sizeof(a));
        #define fillar(ar,n) f(i,0,n) s(ar[i]);
        #define diff(a,b) abs(a-b);
       #define show(a) std::cout << #a << "is " << (a) << std::endl
        #define shows(a) std::cout << #a << " is " << (a)  << " ,";
        #define nl printf("\n");
        using namespace std;
        #define pi(a) cout << a ;
        #define ps(a) cout << a << " ";
        #define MOD 1000000007
        #define flush fflush(stdout);
struct flist
{
    int val;
    int pos;
    
};
ll solve(int thi){
    string ss;
    s(ss);
    int n=sl(ss);
    int anss[n];
    int in[n];
    int i;
    cout << "Case #"<< thi<<": ";
    if(n==1){
        cout << ss << endl;
        return 0;
    }
    f(i,0,n){
        in[i]=ss[i]-'0';
    }
    int maxx=in[n-1];
    int last=n-1;
    fr(i,0,n-1){
        if(in[i]>maxx){
           last=i;
           maxx=in[i]-1; 
        }
        else{
            maxx=in[i];
        }
    }
    if(last==n-1){
        cout << ss << endl ;
        return 0;
    }
    if(last==0 && in[0]==1){
        string ans="";
        f(i,0,n-1){
            ans +="9";
        }
        cout << ans  << endl;
        return 0;
    }
    string ans=ss;
    ans[last]=(ss[last]-1);
    f(i,last+1,n){
        ans[i]='9';
    }
    cout << ans << endl;
    return 0;

}
int main(){
        ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);

        int t;
        s(t);
        int x=t;
        test(t){
             // printf("hey \n");
             solve(x-t+1);
             // printf("done\n");
             t--;
        }

}

          
  