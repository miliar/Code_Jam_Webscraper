#include<iostream>
#include<iomanip>
#include<algorithm>
#include<queue>
#include<set>
#include<cstdio>
#include<map>
#include<limits>
#include<cstring>
#include<string>
#include<sstream>
using namespace std;
typedef long long ll;
ll str2ll(string n){
    ll tn;
    stringstream ss;
    ss<<n;
    ss>>tn;
    return tn;
}
string ll2str(ll n){
    string tn;
    stringstream ss;
    ss<<n;
    ss>>tn;
    return tn;
}
void upda(ll n,ll&ans){
    if(n>ans)
        ans=n;
}
bool isup(string n){
    for(int i=0;i+1<n.size();++i)
        if(n[i]>n[i+1])
            return false;
    return true;
}

ll solve(string n){
    ll ans;
    ans=0;
    if(n.size()==1){
        upda(str2ll(n),ans);
    }else{
        upda(str2ll(string('9',n.size()-1)),ans);
        if(isup(n))
            upda(str2ll(n),ans);
        for(int i=0;i<n.size();++i){
            int fail=0;
            for(int j=0;j+1<i;++j){
                if(n[j]>n[j+1])
                    fail=1;
            }
            if(fail)
                continue;
            int pre;
            if(i==0)
                pre='0';
            else
                pre=n[i-1];
            if(pre>=n[i])
                continue;
            string tmp=n;
            tmp[i]=n[i]-1;
            for(int j=i+1;j<n.size();++j)
                tmp[j]='9';
            upda(str2ll(tmp),ans);
        }
    }
    return ans;
}
ll solve(ll n){
    return solve(ll2str(n));
}
ll bf(ll n){
    for(int i=n;i>=1;--i){
        string t=ll2str(i);
        if(isup(t))
            return i;
    }
}
void test(){
    for(int i=1;i<=1000000;++i){
        cout<<i<<":\n";
        ll t1=solve(i);
        cout<<t1<<endl;
        ll t2=bf(i);
        cout<<t2<<endl<<endl;
        if(t1!=t2)
            break;
    }
}

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    //test();
    int T;scanf("%d",&T);
    for(int I=1;I<=T;++I){
        static char n[1010];
        int l;
        scanf("%s",n+1);
        l=strlen(n+1);
        cout<<"Case #"<<I<<": "<<solve(n+1)<<endl;
    }
    return 0;
}
