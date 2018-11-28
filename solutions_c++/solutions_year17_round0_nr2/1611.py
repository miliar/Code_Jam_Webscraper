/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
 * Created By : Aditya Agarwal
 * IT, MNNIT-ALLAHABAD 
 * aditya.mnnit15@gmail.com
 _._._._._._._._._._._._._._._._._._._._._.*/


#include<bits/stdc++.h>
using namespace std;

#define MP make_pair
#define pb push_back
#define rep(i,n) for(int i=0;i<n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
#define PER(i,a,b) for(int i=b;i>=a;i--)
#define X first
#define Y second

 //i/o
#define inp(n) scanf("%d",&n)
#define inpl(n) scanf("%lld",&n)
#define inp2(n,m) inp(n), inp(m)
#define inp2l(n,m) inpl(n), inpl(m)


//cost
#define MOD 1000000007
#define MOD_INV 1000000006
#define MAX 100009
#define INF 999999999
#define mp make_pair
typedef long long ll;
typedef pair< pair<ll,ll>,ll > pairs;

int main(){
    int t,p=1;
    inp(t);
    while(t--){
        string s;
        cin>>s;
        int n=s.length();
        for(int i=0;i<n-1;i++){
            if(s[i]>s[i+1]){
                s[i]=s[i]-1;
                for(int j=i+1;j<n;j++)
                    s[j]='9';
                for(int j=i-1;j>=0;j--){
                    if(s[j]>s[j+1]){
                        s[j]-=1;
                        s[j+1]='9';
                    }
                    else
                        break;
                }
                break;
            }
        }
        ll cnt=0;
        rep(i,n)
            cnt=cnt*10+(s[i]-'0');
        if(1)
            printf("Case #%d: %lld\n",p++,cnt);
    
    }

    return 0;
}
