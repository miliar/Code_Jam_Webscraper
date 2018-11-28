#include"iostream"
#include"cstring"
#include"cstdio"
#include"queue"
#include"set"
#include"map"
#include"algorithm"
#include"cmath"
#define clr(a) memset(a,0,sizeof(a))
#define mdzz int mid=(L+R)>>1;
#define ls pos<<1
#define rs pos<<1|1
#define lson L,mid,ls
#define rson mid+1,R,rs
#define fr first
#define sc second
using namespace std;

typedef long long LL;

const int N = 1e3+5;
const int M = 2e6+5;
const int INF = 0x3f3f3f3f;

set<pair<LL,LL> >st;
set<pair<LL,LL> >::iterator it;
map<LL,LL> mark;

void Insert(LL v,LL num){
    if(!v) return;
    if(mark.find(v)!=mark.end()){
        num+=mark[v];
        st.erase(make_pair(v,mark[v]));
        mark[v]=num;
    }
    st.insert(make_pair(v,num));
    mark[v]=num;
}

void display(){
    for(it=st.begin();it!=st.end();it++) cout<<(*it).first<<' '<<(*it).second<<endl;
}

int T,cas=1;
LL n,k;

int main(){
    //freopen("C-large.in","r",stdin);
    //freopen("C-large.out","w",stdout);
    for(scanf("%d",&T);T;T--){
        scanf("%lld%lld",&n,&k);
        st.clear();mark.clear();
        st.insert(make_pair(n,1));
        mark[n]=1;
        LL cnt=0;
        while(1){
           // display();cout<<endl;
            it=st.end();it--;
            pair<LL,LL> now = *it;
            st.erase(now);
            cnt+=now.second;
            //cout<<now.first<<' '<<now.second<<endl;
            if(cnt>=k){
                LL minv,maxv;
                if(now.first&1) maxv=minv=now.first/2;
                else minv=now.first/2-1,maxv=now.first/2;
                printf("Case #%d: %lld %lld\n",cas++,maxv,minv);
                break;
            }
            if(now.first!=1){
                if(now.first%2){
                    LL nxt=now.first/2;
                    LL num=now.second*2;
                    Insert(nxt,num);
                }else{
                    Insert(now.first/2,now.second);
                    Insert(now.first/2-1,now.second);
                }
            }
        }
    }
    return 0;
}
/*
1
1000 1000
*/
