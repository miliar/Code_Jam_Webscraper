#pragma comment(linker, "/stack:640000000")

#include<bits/stdc++.h>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
#define ll long long int
#define scanl(a) scanf("%lld",&a)
#define scanii(a,b) scanf("%d%d",&a,&b)
#define scaniii(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define scanll(a,b) scanf("%lld%lld",&a,&b)
#define scanlll(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define scani(a) scanf("%d",&a)
#define clr(a) memset(a,0,sizeof(a))
#define clr_(a) memset(a,-1,sizeof(a))
#define pb(a) push_back(a)
#define pii pair<int,int>
#define sqr(a) a*a
#define eps 1e-9
#define inf INT_MAX
#define pi acos(-1.0)
#define ff first
#define ss second
#define INF 1e18
#define endl '\n'
#define vsort(v) sort(v.begin(),v.end())
vector<char>v;
int n,m,flag;
char in[30][30];
bool check(){
    pii st[30],en[30];
//    v.clear();v.pb('C');v.pb('O');v.pb('D');
//    v.pb('E');v.pb('J');v.pb('A');v.pb('M');
    for(int i=0;i<v.size();i++){
            //cout<<v[i]<<" ";
        for(int j=0;j<n;j++){
                st[j].ff=-1;st[j].ss=-1;
                en[j].ff=-1;en[j].ss=-1;
                int f=0,g=0,temp_tot=0,tot=0;
            for(int k=0;k<m;k++){
                if(in[j][k]==v[i])tot++;
                if(in[j][k]==v[i] && f==0){
                       // cout<<j<<" "<<k<<" "endl;
                    st[j]=pii(j,k);
                    f=1;
                }
                int k1=k;
                while(in[j][k1]==v[i] && k1<m && g==0){
                        temp_tot++;
                        en[j]=pii(j,k1);
                        k1++;
                }
               if(en[j].ff!=-1 && en[j].ss!=-1)g=1;
            }
            //cout<<v[i]<<endl;
            //cout<<temp_tot<<" hfghj "<<tot<<endl;
            if(temp_tot!=tot)return false;
        }
           int j;
           for(j=0;j<n;j++){
                if(st[j].ss==-1 || en[j].ss==-1)continue;
                break;
           }
           j++;
           for(;j<n;j++){
           //cout<<st[j-1].ss<<" "<<st[j].ss<<endl;
            //cout<<en[j-1].ss<<" "<<en[j].ss<<endl;
             if(st[j].ss==-1 || en[j].ss==-1)break;
            if(st[j].ss!=st[j-1].ss || en[j].ss!=en[j-1].ss)return false;
        }
        for(;j<n;j++){
             if(st[j].ss!=-1 || en[j].ss!=-1)return false;
        }
    }
        return true;

}
void print(){
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++)cout<<in[i][j];
        cout<<endl;
    }
}
void call(int len){
    //if(len==5)  print();
    if(flag)return;
   /// if(len==0)print();
    ///cout<<len<<" ";
    if(len==0 && check()){
          ///  cout<<1;
        flag=1;
        print();
        return ;
    }
        for(int j=0;j<n;j++){
            if(flag)break;
            for(int k=0;k<m;k++){
                if(flag)break;
                for(int i=0;i<v.size();i++){
                    if(flag)break;
                if(in[j][k]=='?'){
                    in[j][k]=v[i];
                    call(len-1);
                    in[j][k]='?';
                }
            }
        }
    }
}
int main()
{
    /// ios_base::sync_with_stdio(0);
    /// cin.tie(0);
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int cs=1;cs<=t;cs++){
        v.clear();flag=0;
        cin>>n>>m;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cin>>in[i][j];
                if(in[i][j]!='?')v.pb(in[i][j]);
            }
        }

        //cout<<check();
      ///  for(int i=0;i<v.size();i++){cout<<v[i]<<" ";}
        //cout<<v.size()<<endl;
        //cout<<n<<" "<<m<<endl;
        cout<<"Case #"<<cs<<":"<<endl;
        call(n*m-v.size());
    }
    return 0;
}

