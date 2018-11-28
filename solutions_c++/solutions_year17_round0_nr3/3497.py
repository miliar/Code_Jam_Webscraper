#include <iostream>
#include <cstdio>
using namespace std;

int cases, len;
long long n, k;
long long m, div, x, y, z, lft, rgt, mid;

long long Max(long long a, long long b)
{
    if(a>b) return a;
    return b;
}
long long Min(long long a, long long b)
{
    if(a>b) return b;
    return a;
}
void Solve()
{
    //memset(bit,0,sizeof(bit));
    cin>>n>>k;
    len=0;
    long long tmp=k+1;
    while(tmp){
        //bit[++len]=tmp&1;
        ++len;
        tmp=tmp>>1;
    }
    //2^len<=k+1<2^(len+1)
    //x+y=2^len, x*m+y*(m+1)=n
    --len;
    if(k+1==(1<<len)) --len;
    div=1<<len;
    m=(n+1)>>len;
    y=(n+1)%div;
    x=div-y;
    z=k+1-div;
    if(z>y){
        mid=m>>1;
        lft=mid-1;
        rgt=m-mid-1;
    }
    else if(z>0){
        mid=(m+1)>>1;
        lft=mid-1;
        rgt=m-mid;
    }
    /*else{//z==0;
        if(x>1) lft=rgt=m-1;
        else if(x){
            lft=m-1;
            rgt=m;
        }
        else{
            lft=rgt=m;
        }
    }
    */
    //cout<<"n="<<n<<" k="<<k<<" len="<<len<<" m="<<m<<endl;
    cout<<Max(lft, rgt)<<' '<<Min(lft, rgt)<<endl;
}

int main()
{
    // don't forget to comment these
    //freopen("c.in","r",stdin);
    //freopen("c.out","w",stdout);
    // don't forget to comment these
    scanf("%d",&cases);
    for(int kase=1;kase<=cases;++kase){
        printf("Case #%d: ",kase);
        //Init();
        Solve();
    }
    return 0;
}
