#include<bits/stdc++.h>
using namespace std;

#define TEST(T) int T; sci(T); while(T--)
#define pb push_back
#define ui unsigned int
#define ll long long
#define ull unsigned long long
#define rev(v) reverse(v.begin(),v.end())
#define FOR(a,b) for(int i = (a); i <= (b); ++i)
#define FORD(a,b) for(int i = (a); i >= (b); --i)
#define rev(v) reverse(v.begin(),v.end())
#define sort3(ARR,n) sort(ARR,ARR+n,less<long int>())
#define sort4(ARR,n) sort(ARR,ARR+n,greater<long int>())
#define asort(v) sort(v.begin(),v.end(),less<long int>())
#define desort(v) sort(v.begin(),v.end(),greater<long int>())
#define display(shaan) for (std::vector<int>::const_iterator i = shaan.begin(); i != shaan.end(); ++i) std::cout << *i << ' ';
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);
#define sz(v) (int)v.size();
#define clr(V,val) memset(V,val,sizeof(V))
#define rep(X,A,N,C) for(X=A;X<=N;X+=C)
#define rept(X,A,N,C) for(X=A;X>=N;X-=C)
#define sci(X) scanf("%d",&X)
#define scl(X) scanf("%lld",&X)
#define scs(X) scanf("%s",&X)
#define scc(X) scanf("%c",&X)
#define pfi(X) printf("%d",X)
#define pfl(X) printf("%lld",X)
#define pfs(X) printf("%s",X)
#define pfc(X) printf("%c",X)
#define sp printf(" ")
#define nxt printf("\n")
const int MX=1e6+5;

vector< vector<int> >v;
int main()
{
    fastScan;
    int t;
    cin>>t;
    for(int chal=1;chal<=t;chal++){
        string s;
        cin>>s;
        if(s.length()==1)
        {
            cout<<"Case #"<<chal<<": ";
            cout<<s<<endl;
            continue;
        }
        int flag=0;
        FOR(0,s.length()-2){
            if(s.at(i)>s.at(i+1))
            {
                flag=1;
                break;
            }
        }
        if(!flag){
            cout<<"Case #"<<chal<<": "<<s<<endl;
        }
        else{
        char c;
        int cunt=0;
        for(int i=0;i<s.length()-1;i++){
            c=s.at(i);
            cunt=i;
            if(c>s.at(i+1))
            break;
            
        }
        int j=cunt;
        //cout<<"J "<<j<<endl;
        for(;j>=1;j--){
            cunt=j;
            if(s.at(j)!=s.at(j-1))
            break;
            
        }
        cunt=j;
        //cout<<"Cunt "<<j<<endl;
        char cun=s[cunt];
        if(s.at(0)!=1)cun--;
        s[cunt]=(char)cun;
        int i;
        if(s[0]=='0')
        i=1;
        else
        i=0;
        cout<<"Case #"<<chal<<": ";
        for(;i<=cunt;i++){
            cout<<s[i];
        }
        for(int i=(cunt+1);i<s.length();i++){
            cout<<"9";
        }
        cout<<endl;
        }
    }
    

 return 0;
}
//yo freaker, don't be a tatti seeker :P

// sys/resource rlimit l limit search