#include<bits/stdc++.h>
using namespace std;
#define lli long long int
const lli mod=1e9+7;
void fast() {std::ios::sync_with_stdio(false);cin.tie(NULL);}
lli power(lli a,lli b){lli ans=1;while(b!=0){ if(b%2==1){ans*=a;}b/=2;a*=a;} return ans;}
lli invmod(lli a) {return pow(a,mod-2);}
#define vi vector<int>
#define vlli vector<lli>
#define pb push_back
#define F first
#define S second
#define si(n) scanf("%d",&n)
#define sli(n) scanf("%lld",&n)
#define printi(n) printf("%d\n",n)
#define printli(n) printf("%lld\n",n)
#define all(vi) (vi.begin(),vi.end())
#define forn(i,n) for(int i=0;i<n;i++)
void print(int a[],int n){for(int i=0;i<n;i++) cout<<a[i]<<" ";}

int main()
{
    int t,k;
    si(t);
    string s;
    
    for(int tc=1;tc<=t;tc++){
        cin>>s;
        si(k);
        int l=s.size();
        int ans=0;
        
        for(int i=0;i<=l-k;i++){
            if(s[i]=='+') continue;
            else{
                ans++;
                for(int j=i;j<=i+k-1;j++){
                    if(s[j]=='+') s[j]='-';
                    else s[j]='+';
                }
            }
            //cout<<"s is "<<s<<endl;
        }
        int x=0;
        for(int i=l-k+1;i<l;i++){
            if(s[i]=='-') {x=1;break;}
        }
        
        if(x==1) printf("Case #%d: IMPOSSIBLE",tc);
        else printf("Case #%d: %d",tc,ans);
        
        printf("\n");
    }
    return 0;
}