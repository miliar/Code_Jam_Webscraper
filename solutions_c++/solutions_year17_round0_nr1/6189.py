#include <bits/stdc++.h>
using namespace std;
#define rep(i, x, y) for(int i = (x); i <= (y); ++i)
#define bug(a) cout << #a << " = " << a << endl;
#define fbug(a, x, y) { cout << #a << ": "; rep(_, x, y) cout << a[_] << ' '; cout << endl; }
#define pb push_back
#define mp make_pair
#define endd "\n"
#define fast ios::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define input freopen("inp.txt","r",stdin)
#define output freopen("out.txt","w",stdout)
#define loop(i,n) for(int i=0;i<n;i++)
#define rloop(i,n) for(int i=n-1;i>=0;i--)
#define ll long long
#define Z size()
#define NN 1000001
#define pii pair<int,int>
#define setp(x) fixed<<setprecision(x)
#define ff first
#define ss second
#define all(x) x.begin(),x.end()
#define pi 3.14159265358979323846264338327950288419716939937510

/*int power(int a , int b)
{
    int res = 1 ;
    while(b)
    {
        if(b%2) {
            res = (res * a) % mod ;
        }
        b/=2 ;
        a = (a*a) % mod ;
    }
    return res ;
}
*/
string s;
int m;
int main(){//input;
   // output;
    int t;
    cin>>t;
    for(int k=0;k<t;k++){
    cin>>s>>m;
    int ans=0,ck=0;
    for(int i=0;i<s.Z;i++){
        if(s[i]=='-'){
//bug(i);
//bug(i+m);
            if(i+m<=s.Z){
                ans++;
            for(int j=i;j<i+m;j++){

                s[j]=(s[j]=='-'?'+':'-');

            }
           // bug(s);
        }
        else{
        ck=1;
        break;
    }
    
    }
    }
    if(!ck)cout<<"Case #"<<k+1<<": "<<ans<<endd;
    else cout<<"Case #"<<k+1<<": IMPOSSIBLE"<<endd;








}

}
