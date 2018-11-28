#include<bits/stdc++.h>
#define MOD 1000000007
#define SIZE 1000007
#define ll long long
#define INF LLONG_MAX
#define in(x) scanf("%d",&x)
#define llin(x) scanf("%lld",&x)
#define pr(x) printf("%d",x)
#define llpr(x) printf("%lld",x)
#define line() printf("\n");
#define spc() printf(" ");
#define f(i,a,b) for(i=a;i<b;i++)
#define pb(x) push_back(x)
#define pf(x) push_front(x)
#define F first
#define S second
#define boost ios::sync_with_stdio(false)
using namespace std;

typedef pair<ll,ll> ii;
typedef vector<ii> vii;
typedef vector<ll> vi;

int main() {
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    //boost;
    int tc,i,j;
    ll N;
    string num;
    cin>>tc;
    for(int tc1=1;tc1<=tc;tc1++){
        cin>>N;
        num = "";
        while(N){
            num = (char)((N%10)+48) + num;
            N/=10;
        }
        N = num.length();
        if(N>1){
            for(i=1;i<N;i++)
                if(num[i]<num[i-1]) break;
            if(i<N){
                for(j=i;j<N;j++) num[j]='9';
                if(num[i-1]=='1'){
                    for(j=0;j<i;j++) num[j]='9';
                    num = num.substr(1,N-1);
                }
                else{
                    char ch = num[i-1];
                    for(j=i-1;j>=0;j--){
                        if(num[j]!=ch) break;
                        num[j]='9';
                    }
                    num[j+1]=(ch-1);
                }
            }
        }
        cout<<"Case #"<<tc1<<": "<<num;
        cout<<"\n";
    }
	return 0;
}

