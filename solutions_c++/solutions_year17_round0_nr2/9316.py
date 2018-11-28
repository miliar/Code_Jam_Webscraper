//#include <bits/stdc++.h>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<iostream>
#include<algorithm>
#include<queue>
#include<cmath>
#include<stack>
#include<set>
#include<vector>
#include<map>
#include<sstream>
#include<ctime>
#define ll long long
#define LL long long
#define iosfalse ios::sync_with_stdio(false);
#define lowbit(x) x&-x

using namespace std;
//B
bool istd(char* a,int len)
{
    for(int i=1;i<len;i++)
    {
        if(a[i-1]<=a[i])
            continue;
        else {
            return false;
        }
    }
    return true;
}
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int it=1;it<=t;it++)
    {
        char str_num[20];
        cin>>str_num;
        int len=strlen(str_num);
        char answer[20];
        if(istd(str_num,len))
            {
                strcpy(answer,str_num);
                cout<<"Case #"<<it<<": "<<answer<<endl;
                continue;
            }
        if(str_num[len-1]=='0'&&str_num[0]=='1')
        {
            for(int i=0;i<len-1;i++)
                answer[i]='9';
            answer[len-1]='\0';
        }
        else {
            int dep=0;
        while(str_num[dep]==str_num[dep+1]) dep++;
            if(str_num[dep]<=str_num[1+dep])
            {
                for(int i=1;i<len;i++)
                {
                    if(str_num[i-1]<=str_num[i])
                    {
                        answer[i-1]=str_num[i-1];
                    }
                    else {
                        answer[i-1]=(char)(str_num[i-1]-1);
                        for(;i<len;i++)
                            answer[i]='9';
                    }
                }
            }
            else {
                answer[0]=(char)(str_num[0]-1);
                for(int i=1;i<len;i++)
                    answer[i]='9';
            }
            answer[len]='\0';
        }
        while(answer[0]=='0')
            strcpy(answer,answer+1);
        cout<<"Case #"<<it<<": "<<answer<<endl;
    }
    return 0;
}

//gcj
//A
/*
int vis[1005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int it=1;it<=t;it++)
    {
        memset(vis,0,sizeof vis);
        string str;
        int k;
        int ans=0;
        cin>>str>>k;
        for(int i=0;i<str.size();i++)
        {
            if(str[i]=='+')
                {
                    if(vis[i]&1)
                    {
                        ans++;
                        if(i+k-1<str.size())
                        {
                            for(int j=i;j<i+k;j++)
                                vis[j]++;
                        }else {
                            for(int j=str.size()-k;j<str.size();j++)
                                vis[j]++;
                        }
                    }
                }
            else {
                if(vis[i]%2==0)
                    {
                        ans++;
                        if(i+k-1<str.size())
                        {
                            for(int j=i;j<i+k;j++)
                                vis[j]++;
                        }else {
                            for(int j=str.size()-k;j<str.size();j++)
                                vis[j]++;
                        }
                    }
            }
        }
        bool ok=true;
        for(int i=0;i<str.size();i++)
            {
                if((str[i]=='+'&&(vis[i]&1))||(str[i]=='-'&&(vis[i]%2==0)))
                {
                    ok=false;break;
                }
            }
        if(ok)
            cout<<"Case #"<<it<<": "<<ans<<endl;
        else cout<<"Case #"<<it<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}
*/
//BTLE
/*
int A[300005];
int cop[300005];
ll v[300005];
ll m,n;
int main()
{
    cin>>n>>m;
    for(int i=0;i<n;i++)
        cin>>A[i];
    for(int i=0;i<n;i++)
        cin>>v[i];
    ll S=0,c=0,st=0,len=0;
    for(int i=0;i<n;i++)
    {
        len++;
        if(A[st+len-1]<A[st+len-2])
        sort(A+st,A+st+len);
        for(int j=st;j<st+len;j++)
        {
            S+=A[j]*v[j-st];
        }
        if(S>m)
        {
            c=c+1;
            st=st+len;
            len=0;

        }else {

        }
        if(i+1<n)
        cout<<c<<" ";
        else cout<<c;
        S=0;
    }
    cout<<endl;
    return 0;
}*/

//lonlife 13A
/*
ll a[500005];
ll b[500005];
int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>a[i];
    for(int i=0;i<n;i++)
        cin>>b[i];
    sort(a,a+n);
    sort(b,b+n);
    ll ans=0;
    for(int i=0;i<n;i++)
        ans+=a[i]*b[i];
    cout<<ans<<endl;
    return 0;
}
*/



//B codeforeces
/*
int main()
{
    ll b,q,l,m;
    set<ll>st;
    cin>>b>>q>>l>>m;
    for(int i=0;i<m;i++)
    {
        int t;
        cin>>t;
        st.insert(t);
    }
    if(llabs(b)>l)
    {
        cout<<0<<endl;
        return 0;
    }
    if(q==1)
    {
        if(st.count(b)==0&&llabs(b)<=l)
            cout<<"inf"<<endl;
        else
            cout<<0<<endl;
    }else if(q==-1)
    {
        if((st.count(b)&&st.count(-b))||(llabs(b)>l))
            cout<<0<<endl;
        else cout<<"inf"<<endl;
    }else if(q==0||b==0)
    {
        if(b==0)
        {
            if(st.count(b))
            cout<<0<<endl;
            else cout<<"inf"<<endl;
        }else {
            if(st.count(q)){
                if(st.count(b)||llabs(b)>l)
                 cout<<0<<endl;
                else cout<<1<<endl;
            }
            else if(llabs(b)<=l)
                cout<<"inf"<<endl;
            else cout<<0<<endl;
        }
    }
    else{
        if(llabs(b)<=l)
        st.insert(b);
        while(llabs(b*q)<=l)
        {
            b*=q;
            st.insert(b);
        }
        cout<<st.size()-m<<endl;
    }
    return 0;
}*/
//C
/*
ll a[100005];
ll b[100005];
ll d[100005];
int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>a[i];
    ll ans=-1e18;
    for(int i=0;i+1<n;i++)
        b[i]=abs(a[i]-a[i+1]);
    for(int t=0;t<2;t++)
    {
        if(t==0)
        {
            for(int i=1;i<n;i+=2)
                b[i]=-b[i];
            d[0]=b[0];
            ans=max(ans,d[0]);
            for(int i=1;i<n-1;i++)
                {
                    if(d[i-1]>0)
                        d[i]=d[i-1]+b[i];
                    else d[i]=b[i];
                    ans=max(ans,d[i]);
                }
        }else{
            for(int i=0;i+1<n;i++)
                b[i]=-b[i];
            d[1]=b[1];
            ans=max(ans,d[1]);
            for(int i=2;i<n-1;i++)
                {
                    if(d[i-1]>0)
                        d[i]=d[i-1]+b[i];
                    else d[i]=b[i];
                    ans=max(ans,d[i]);
                }
        }
    }
    cout<<ans<<endl;
    return 0;
}*/

//A
/*
int a[100005];
int main()
{
    int n,k;
    cin>>n>>k;
    for(int i=0;i<n;i++)
        cin>>a[i];
    sort(a,a+n);
    int ans=0;
    for(int i=0;i<n;i++)
    {
        if(a[i]<=0)
            continue;
        ans+=a[i]/(2*k);
        a[i]%=(2*k);
        if(a[i]<=0)
            continue;
        if(a[i]>k)
            ;
        else if(i+1<n)
            a[i+1]-=k;
        ans++;
    }
    cout<<ans<<endl;
    return 0;
}
*/
//有时候二分逼近时可以规定迭代一定次数(int 类型不超过32次)
//AC
/*
int p,q,r,s,t,u;
double fun(double x)
{
    return p*exp(-x)+q*sin(x)+r*cos(x)+s*tan(x)+t*x*x+u;
}
const double eps=1e-14;
int main()
{
    while(cin>>p>>q>>r>>s>>t>>u)
    {
        if(fun(0)<-eps||fun(1)>eps)
            cout<<"No solution"<<endl;
        else{
            double l=0,r=1;
            //for(int i=0;i<100;i++)
            while(l<r-1e-8)
            {
                double mid=(l+r)/2;
                if(fun(mid)>0)
                    l=mid;
                else r=mid;
            }
            printf("%.4f\n",l);
        }
    }
    return 0;
}*/
//E
/*
map<int,long long>mp;
int main()
{
    int two=1;
    for(int i=0;two<1e9;i++)
    {
        mp[i]=two;
        two*=2;
    }//i->29
    int t;
    cin>>t;
    while(t--)
    {
        int n,k;
        cin>>n>>k;
        vector<int>vec;
        while(n>0){
        for(int i=29;i>=0;i--)
            {
                while(n>=mp[i])
                {
                    vec.push_back(mp[i]);
                    n-=mp[i];
                }
            }
        }
        sort(vec.begin(),vec.end());
        int num=vec.size();
        int out=0;
        stack<int>st;
        for(int j=num-1;j>=0;j--)
            st.push(vec[j]);
        while(st.size()>k)
        {
            out+=st.top();
            st.pop();
        }
        out=st.top()-out;
        cout<<out<<endl;
    }
    return 0;
}*/
//C
/*
int a[60];
int dp[30][60];
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        for(int i=0;i<n-1;i++)
            cin>>a[i];
        for(int i=0;i<n-1;i++)
        {
            dp[0][i]=1;
            dp[1][i]=1;
            dp[2][i]=2;
            dp[3][i]=4;
            for(int j=4;j<=a[i];j++)
                dp[j][i]=dp[j-1][i]+dp[j-2][i]+dp[j-3][i];
        }
        long long ans=1;
        for(int i=0;i<n-1;i++)
            ans=(ans*dp[a[i]][i])%10007;
        cout<<ans<<endl;
    }
    return 0;
}*/
//H
/*
int n;
int a[100005];
int main()
{
    iosfalse
    int t;
    cin>>t;
    while(t--)
    {
        cin>>n;
        ll l=1,r=1;
        map<int,int>mp;
        for(int i=0;i<n;i++)
            {
                cin>>a[i];
                r+=a[i];
                mp[a[i]]++;
            }
        sort(a,a+n);
        if(a[0]!=1)
        {
            cout<<1<<endl;
            continue;
        }
        for(l=2;;l++)
        {
            if(mp.count(l)==0)
               {
                   l=l+l;
                   if(mp.count(l)==0)
                        break;
               }
        }
        set<long long>st;
        map<int,int>::iterator ip;
        int N=mp.size(),i=0;
        for(ip=mp.begin();ip!=mp.end();ip++,i++)
        {
        }

    }
    return 0;
}*/
//D
/*
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int a,b,c;
        cin>>a>>b>>c;
        ll ans=0;
        ans+=a*b+(a/30)*c;
        cout<<ans<<endl;
    }
    return 0;
}*/
//A
/*
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int a,b,c;
        cin>>a>>b>>c;
        cout<<(a/2-(c/4-b))<<endl;
    }
    return 0;
}*/
//uva 10870
/*
const int MAXN=20;
const int MAXM=20;
long long  mmd;
struct Matrix{
int n,m;
long long a[MAXN][MAXM];
void m_clear()
{
    n=0;m=0;
    memset(a,0,sizeof a);
}
Matrix operator + (const Matrix &b) const {
    Matrix tmp;
    tmp.m_clear();
    tmp.n=n;tmp.m=m;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
                tmp.a[i][j]=a[i][j]+b.a[i][j];
    return tmp;
}
Matrix operator - (const Matrix &b) const {
    Matrix tmp;
    tmp.m_clear();
    tmp.n=n;tmp.m=m;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
                tmp.a[i][j]=a[i][j]-b.a[i][j];
    return tmp;
}
Matrix operator * (const Matrix &b) const {
    Matrix tmp;
    tmp.m_clear();
    tmp.n=n;tmp.m=b.m;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            for(int k=0;k<m;k++)
                tmp.a[i][j]=(tmp.a[i][j]+a[i][k]*b.a[k][j]%mmd)%mmd;
    return tmp;
}
};
Matrix m_pow(Matrix A,int n)
{
    Matrix tmp;
    tmp.m_clear();
    tmp.n=A.n;tmp.m=A.n;
    for(int i=0;i<A.n;i++)
        tmp.a[i][i]=1;
    while(n>0)
    {
        if(n&1)
            tmp=tmp*A;
        A=A*A;
        n>>=1;
    }
    return tmp;
}
int a[20],f[20];
int main()
{
    int d,n;
    while(cin>>d>>n>>mmd){
    if(d==0&&n==0&&mmd==0)
        break;
    Matrix A;
    A.m_clear();
    A.n=d;A.m=d;
    for(int i=0;i<d;i++)
        cin>>A.a[d-1][d-i-1];
    for(int i=0;i<d;i++)
        cin>>f[i];
    for(int i=0;i<d-1;i++)
        A.a[i][i+1]=1;
    A=m_pow(A,n-d);
    long long ans_fn=0;
    for(int i=0;i<d;i++)
        ans_fn=(ans_fn+A.a[d-1][i]*f[i]%mmd)%mmd;
    cout<<ans_fn<<endl;
    }
    return 0;
}*/
/*
//poj 3280

int add[30],del[30];
int main()
{

    int n,m;
    cin>>n>>m;
    string str;
    cin>>str;
    for(int i=1;i<=n;i++)
    {
        cin>>add[i]>>del[i];
    }




    return 0;
}*/
///来一发ac自动机

///hdu 2426 ac 还有问题
/*
const int maxn = 501;
const int INF = (1<<31)-1;
int w[maxn][maxn];
int lx[maxn],ly[maxn]; //顶标
int linky[maxn];
int visx[maxn],visy[maxn];
int slack[maxn];
int nx,ny;
bool find(int x)
{
    visx[x] = true;
    for(int y = 0; y < ny; y++)
    {
        if(visy[y])
            continue;
        int t = lx[x] + ly[y] - w[x][y];
        if(t==0)
        {
            visy[y] = true;
            if(linky[y]==-1 || find(linky[y]))
            {
                linky[y] = x;
                return true;        //找到增广轨
            }
        }
        else if(slack[y] > t)
            slack[y] = t;
    }
    return false;                   //没有找到增广轨（说明顶点x没有对应的匹配，与完备匹配(相等子图的完备匹配)不符）
}

int KM()                //返回最优匹配的值
{
    int i,j;
    memset(linky,-1,sizeof(linky));
    memset(ly,0,sizeof(ly));
    for(i = 0; i < nx; i++)
        for(j = 0,lx[i] = -INF; j < ny; j++)
            if(w[i][j] > lx[i])
                lx[i] = w[i][j];
    for(int x = 0; x < nx; x++)
    {
        for(i = 0; i < ny; i++)
            slack[i] = INF;
        while(true)
        {
            memset(visx,0,sizeof(visx));
            memset(visy,0,sizeof(visy));
            if(find(x))                     //找到增广轨，退出
                break;
            int d = INF;
            for(i = 0; i < ny; i++)          //没找到，对l做调整(这会增加相等子图的边)，重新找
            {
                if(!visy[i] && d > slack[i])
                    d = slack[i];
            }
            for(i = 0; i < nx; i++)
            {
                if(visx[i])
                    lx[i] -= d;
            }
            for(i = 0; i < ny; i++)
            {
                if(visy[i])
                     ly[i] += d;
                else
                     slack[i] -= d;
            }
        }
    }
    int result = 0;
    for(i = 0; i < ny; i++)
    {
        if(linky[i]>-1)
            {
            if(w[linky[i]][i]>=0)
                result += w[linky[i]][i];
            else return -1;
            }
    }
    return result;
}
int main()
{
    int m;
    int id=1;
    while(scanf("%d %d %d",&nx,&ny,&m)!=EOF)
    {
        if(ny<nx)//不处理会死循环
        {
            printf("Case %d: -1",id++);
            continue;
        }
        for(int i=0;i<nx;i++)
            for(int j=0;j<ny;j++)
            {
                w[i][j]=-inf;
            }
        int u,v,weight;
        for(int i=0;i<m;i++)
           {
            scanf("%d %d %d",&u,&v,&weight);
            if(weight>=0)///important!!!不加就wa
            w[u][v]=weight;
           }
        int ans=KM();
        printf("Case %d: ",id++);
        printf("%d\n",ans);
    }
    return 0;
}*/


///0222B 字典树wa 在文件夹
///cf div2 398
///B
/*
ll a[100005];
ll donet[100005];
int main()
{
    ll ts,tf,t,n;
    cin>>ts>>tf>>t>>n;
    for(int i=1;i<=n;i++)
        {
            cin>>a[i];
            if(i==1)
            {
                if(a[i]<ts)
                    donet[i]=ts+t;
                else
                    donet[i]=a[i]+t;
            }else {
                if(a[i]<donet[i-1])
                    donet[i]=donet[i-1]+t;
                else donet[i]=a[i]+t;
            }
        }
    ll ans=a[1]-1,answait=inf;
    donet[0]=ts;
    for(int i=1;i<=n;i++)
    {
        int arr=a[i]-1;
        if(arr>tf-t)
            continue;
        int tmpwait;
        if(arr<donet[i-1])
        tmpwait=donet[i-1]-arr;
        else if(donet[i-1]>0&&donet[i-1]<=tf-t)
            tmpwait=0;
        else tmpwait=inf;
        if(tmpwait<answait)
        {
            answait=tmpwait;
            ans=arr;
        }
    }
    if(donet[n]<=tf-t&&donet[n]>=0)
        ans=donet[n];
    if(ans>tf-t||ans<0) ///wa10
        ans=tf-t;
    cout<<ans<<endl;
    return 0;
}
*/
//lonlife rd10
///E  ql
/*
long long getll ( string s )
{
    return atoll(s.c_str());
}
vector<long long>vec;
int main()
{
    for(int i=1;i<=9;i++)
    {
        for(int j=0;j<=i;j++)
        {
            string num1(j,'1');
            string num2(i-j,'6');
            string num=num1+num2;
            sort(num.begin(),num.end());
            do{
                vec.push_back(getll(num));
            }while(next_permutation(num.begin(),num.end()));
        }
    }
    sort(vec.begin(),vec.end());
    cout<<vec.size()<<endl;
    ///Tle
    for(int i=1;i<vec.size();i++)
    {
        cout<<" 1 "<<endl;
        int isbk=0;
        while(!isbk)
        {
            cout<<" 22 "<<endl;
            int presize=vec.size();
            for(int j=i;j<presize;j++)
            {
                ll tmp=vec[i]*vec[j];
                //cout<<tmp<<endl;
                if(tmp<1e10)
                    vec.push_back(tmp);
                else break;
            }
            sort(vec.begin(),vec.end());
            unique(vec.begin(),vec.end());
            if(presize=vec.size())
                isbk=1;
        }
    }
    cout<<vec.size()<<endl;
    ///
    int T;
    scanf("%d",&T);
    for(int it=0;it<T;it++)
    {
        ll L,R;
        scanf("%I64d%I64d",&L,&R);
        ll st,ed;

    }
    return 0;
}

*/
///wanafly
//B贪心思路wa
/*
int b[100005];
int p[100005];
int main()
{
    int n,m,a;
    scanf("%d %d %d",&n,&m,&a);
    for(int i=0;i<n;i++)
        scanf("%d",&b[i]);
    for(int j=0;j<m;j++)
        scanf("%d",&p[j]);
    sort(b,b+n);
    sort(p,p+m);
    int r=0;
    int ta=a;
    long long s=0;
    int i,j;
    for(i=0,j=0;i<n&&j<m;)
    {
        if(b[i]>=p[j])
        {
            r++;s+=p[j];i++;j++;
        }else if(a>0&&b[i]+a>=p[j])
        {
            a-=(p[j]-b[i]);r++;s+=p[j];i++;j++;
        }else i++;
    }
    if(s>=ta)
        s-=ta;
    else s=0;
    cout<<r<<" "<<s<<endl;
    return 0;
}*/
//Dkmp
//
/*
int Next[200005];
void getNext(long long* b,int m)
{
    int j,k;
    j=0;k=-1;
    Next[0]=-1;
    while(j<m)
    {
        if(k==-1||b[j]==b[k]) Next[++j]=++k;
        else k=Next[k];
    }
}
long long a[200005];
long long b[200005];
int n,m;
int KMP_Index()
{
    int i=0,j=0;
    getNext(b,m);
    int answer=0;
    int det=a[i]-b[j];
    while(i<n)
    {
        //cout<<i<<" "<<a[i]<<"   " <<j<<" "<<b[j]<<endl;
        if(j==-1||a[i]-b[j]==det)
        {
            if(j==-1)
                det=a[i+1]-b[j+1];
            i++;j++;
        }else {
            j=Next[j];

            }
        if(j==m) {answer++;
        j=Next[j];det=a[i]-b[j];
        }
    }
    return answer;
}
int main()
{
    scanf("%d %d",&n,&m);
    for(int i=0;i<n;i++)
        scanf("%I64d",&a[i]);
    for(int i=0;i<m;i++)
        scanf("%I64d",&b[i]);
    int ans=KMP_Index();
    cout<<ans<<endl;
    return 0;
}
*/
///like the problem of poj use radar
/*
struct P
{
    int x,y;
    double dx;
}p[1005];
int cmp(P a,P b)
{
    if(a.x!=b.x)
        return a.x<b.x;
    else return abs(a.y)>abs(b.y);
}
int main()
{
    int n,d,sq=1;
    while(cin>>n>>d)
    {
        if(n==0&&d==0)
            break;
        for(int i=0;i<n;i++)
        {
            cin>>p[i].x>>p[i].y;
            p[i].dx=sqrt(d*d-p[i].y*p[i].y);
        }
        sort(p,p+n,cmp);
        int ans=1,allzero=1;
        int id=0,pre=0,prr=0;
        for(;id<n;id++)
        {
            if(p[id].y<=0) {allzero=1;continue;}
            else allzero=0;
            if((p[id].x-p[id].dx<=p[pre].x+p[pre].dx&&p[pre].x+p[pre].dx<=p[id].x+p[id].dx)
                ||(p[id].x-p[id].dx<=p[prr].x+p[prr].dx&&p[prr].x+p[prr].dx<=p[id].x+p[id].dx))
            ;
            else//easy wrong
            {
                ans++;
                prr=pre;
                pre=id;
            }
        }
        if(allzero) ans=-1;
        cout<<"Case "<<sq++<<": "<<ans<<endl;
    }

    return 0;
}*/
/*
//poj1753 wa
int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};
int id=0;
int check(int pan[][4],int col)
{
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
    {
        if(pan[i][j]!=col)
            return 0;
    }
    return 1;
}
void print(int a[][4])
{
    cout<<"·Ö¸îÏß~~~~~~"<<id++<<endl;
    for(int i=0;i<4;i++)
        {for(int j=0;j<4;j++)
            printf("%d",a[i][j]);
            printf("\n");
        }
}
int find_ans(int &ans,int x,int y,int mp[][4],int bw)
{
    int cur_ans=ans+1;
    int pan[4][4];
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            pan[i][j]=mp[i][j];
    pan[x][y]^=1;
    for(int t=0;t<4;t++)
        {
            int tx=x+dx[t];int ty=y+dy[t];
            if(tx>=0&&tx<4&&ty>=0&&ty<4)
                pan[tx][ty]^=1;
        }
        //cout<<cur_ans<<endl;
    print(pan);
    cout<<"     "<<ans<<endl;
    if(check(pan,bw))
        return ans=cur_ans;
    for(int i=x;i<4;i++)
        for(int j=(i==x)?y+1:0;j<4;j++)
    {
        if(pan[i][j]!=bw){
        return ans= find_ans(cur_ans,i,j,pan,bw);

        }
    }
    //if(x==3&&y==3)
    return ans=inf;
}

int main()
{
    int color[4][4];
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
    {
        char c;
        cin>>c;
        if(c=='b')
            color[i][j]=1;
        else if(c=='w')
            color[i][j]=0;
    }
    int answer=inf;
    if(check(color,0)||check(color,1))
        {
            answer=0;
        //cout<<"okokokok"<<endl;
        }
    else{

    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
    {
        int ans=0;
        if(color[i][j]==1)//to all 0
        {
            find_ans(ans,i,j,color,0);
            answer=min(ans,answer);

        }
        // print(color);
    }
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
    {
        int ans=0;
        if(color[i][j]==0)//to all 1
        {find_ans(ans,i,j,color,1);
        answer=min(ans,answer);}
        break;
    }

    }
    if(answer==inf)
        cout<<"Impossible"<<endl;
    else cout<<answer<<endl;
    return 0;
}*/
