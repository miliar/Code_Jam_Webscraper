#include<bits/stdc++.h>
using namespace std;

#define sin(x) scanf("%d",&x)
#define sin2(x,y) scanf("%d%d",&x,&y)
#define sin3(x,y,z) scanf("%d%d%d",&x,&y,&z)

#define pb push_back
#define mp make_pair
#define y1 asdnqw
#define next mdamdamda
#define right praviy
#define x first
#define y second
#define kub(x) ((x)*(x)*(x))
#define int long long
const double eps=0.1;
const int inf=1e16+6;
const int N=101;
int tt,t,k,q;
string s;
int tcount;
void f(int i){
    if(s[i]=='+')s[i]='-';
        else s[i]='+';
}
 main(){
     //cin.tie(0);ios_base::sync_with_stdio(0);
     freopen("input.txt","r",stdin);
     freopen("output.txt","w",stdout);
     cin>>t;
     for(;t--;){
            ++tcount;
        cin>>s>>k;
     // cout<<"#"<<s<<endl;
        q=0;
        for(int i=0;i+k-1<s.size();++i){
            if(s[i]=='-'){
                ++q;
                for(int j=i;j<i+k;++j)
                    f(j);
            }
           // cout<<endl<<s<<endl;
        }

     tt=0;
     for(int i=0;i<s.size();++i)
        if(s[i]=='-')tt=1;
        cout<<"Case #"<<tcount<<": ";
     if(tt)cout<<"IMPOSSIBLE";
     else cout<<q;
    // cout<<' '<<q;
     cout<<endl;
     }
}
