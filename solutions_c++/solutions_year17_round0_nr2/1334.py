#include<bits/stdc++.h>
#define rep(i,x,y) for(i=x;i<y;i++)
#define pb(f) push_back(f)

#define ll long long
#define scs(a) scanf("%s",a)
#define mp make_pair
#define fi first
#define se second
#define mod 1000000007LL
#define inf 100000000000000009LL

const int N=200005;
using namespace std;
typedef pair<ll,ll> pii;
typedef vector<int> vi;
typedef vector< pii > vpii;
using namespace std;

FILE *fin=freopen("2.in","r",stdin); FILE *fout=freopen("out.txt","w",stdout);
int main(){
    int t;
    string s;int k;
    cin>>t;
    int cas=0;
    while(t--){
        cas++;
        cout<<"Case #"<<cas<<": ";
        cin>>s;
        if(s.length()==1) {
            cout<<s<<endl;continue;
        }
        int last=s.length();
        for(int i=(int)s.length()-2;i>=0;i--){
            if(s[i]>s[i+1]){
                s[i]-=1;last=i+1;
            }
        }
        for(int i=last;i<s.length();i++) s[i]='9';
        int i=0;while(s[i]=='0') i++;
        while(i<s.length()){ cout<<s[i];i++;}
        cout<<endl;
    }
}
