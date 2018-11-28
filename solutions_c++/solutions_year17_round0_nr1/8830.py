                  /** Al-Amin Mahfuzur Rahman **/
             /** Email :- 7mahfuzur.rahman@gmail.com **/
              /**  FB :- tinyurl.com/7mahfuz   **/
      /** Institute :- Institute of science,trade and technology **/

#include <bits/stdc++.h>
#define rt return
#define sci(x) scanf("%d",&x)
#define scl(x) scanf("%I64d",&x)
#define scf(x) scanf("%f",&x)
#define LL long long
#define sc scanf
#define pf printf
#define pfi(x) printf("%d",x)
#define pfl(x) printf("%I64d",x)
#define NL printf("\n")
#define gap printf(" ")
#define YES printf("YES\n")
#define NO printf("NO\n")
#define Yes printf("Yes\n")
#define No printf("No\n")

#define MOD 1000000007
#define PI acos(-1.0)
#define sz(x) x.size()
#define sqr(x) ((x)*(x))
#define ek first
#define dui second
#define dist(x1,x2,y1,y2) sqrt(sqr(x1-x2)+sqr(y1-y2))

/** Vector **/
#define pb(x) push_back(x)
#define Maxvec(vector) *max_element(vector.begin(),vector.end())
#define Minvec(vector) *min_element(vector.begin(),vector.end())
#define Cntvec(vector,key) count(vector.begin(),vector.end(),key)
#define Revvec(vector) reverse(vector.begin(),vector.end())
#define cv(vector) vector.clear()
#define EraseV(vector,n) vector.erase(vector.begin(),vector.begin()+n)
#define eraseV(vector,n) vector.erase (vector.begin()+n)
#define Vswap(v1,v2) v1.swap(v2)
/** SET **/
#define setLB(set,n) set.lower_bound(n)
#define setUP(set,n) set.upper_bound(n)
#define setfind(set,n) set.find(n)
#define ins(n) insert(n)
/**String **/
#define Revstr(st) reverse(st.begin(),st.end())
#define line(st) getline(cin,st)
#define Sswap(st1,st2) st1.swap(st2)
#define portxy(st,x,y) st.substr(x,y)/**Portion from a string x to y taa**/
#define portz(st,z) st.substr(z) /**Portion of str from z to last **/
#define sfind(st,key) st.find(key)/** find the pos **/
#define stdlt(st,x,y) st.erase(x,y)/** erase(beg+x)/erase(beg+x,end-y) **/
#define kill(st) st.clear()
/** Array **/
#define Cntkey(arr,n,key) count(arr,arr+n,key)/** arr te kotobar key asee ta chking **/
#define Revarr(arr,n) reverse(arr,arr+n)
#define Maxarr(arr,n) *max_element(arr,arr+n)
#define Minarr(arr,n) *min_element(arr,arr+n);
/** Array must be sorted before use lower and upper bound  **/
#define LB(arr,n,key) *lower_bound(arr,arr+n,key)-1
#define UB(arr,n,key) *upper_bound(arr,arr+n,cnt)-1
#define mem(arr,val) memset(arr,val,sizeof(arr))
#define CLR(a) memset(a,0,sizeof(a))
#define Aswap(a1,a2) a1.swap(a2)/** must a1==a2 **/
/**accumulate(a+1,a+n,a[0],myfunc)or accumulate(a,a+n,1/0,mufunc)or accumulate(a,a+n,variable)**/

#define lp0(i,n) for(i=0;i<n;i++)
#define lp00(i,n) for(i=0;i<=n;i++)
#define lp1(i,n) for(i=1;i<n;i++)
#define lp11(i,n) for(i=1;i<=n;i++)
#define lpab(i,a,b) for(i=a;i<b;i++)
#define lpAB(i,A,B) for(i=A;i<=B;i++)

#define MAX 100000
#define max3(x,y,z) max(x,max(y,z))
#define min3(x,y,z) min(x,min(y,z))
/**to chk 2 arr equal or not = if(equal(arr1,arr2,arr2+n)) its a bool**/
using namespace std;
//template <class T> string tostring(T n) {stringstream ss; ss << n; return ss.str();}
//string tostring(int n) {stringstream ss; ss << n; return ss.str();}
//LL pow(LL n,LL m){LL ans=1;for(int i=1;i<=m;i++){ans=ans*n;}rt ans;}
//LL ModInverse(LL n,LL m){return bigmod(n,m-2,m)};
//LL bigmod(LL b,LL p){if(p == 0)return 1;LL my = bigmod(b,p/2);my*=my;my%=mod;if(p & 1)my*=b,my%=mod;return my;}
//bool isVowel(char ch){ ch=toupper(ch); if(ch=='A'||ch=='U'||ch=='I'||ch=='O'||ch=='E') rt true; rt false;}
//bool isConst(char ch){if (isalpha(ch) && !isVowel(ch)) rt true; rt false;}
//int toint(string s)  { int sm; stringstream ss(s); ss>>sm; rt sm; /** st=123 to int=123 **/ }
//int gcd(int a,int b) {a=abs(a);b=abs(b); if(!b) return a; return gcd(b,a%b);}
//int lcm(int a,int b) {a=abs(a);b=abs(b); return (a/gcd(a,b))*b;}
//string Dtostring(double n) { ostringstream  ss; ss << n; return ss.str();}

//int dx[]={2, 1, -1, -2, -2, -1,  1,  2};//knight's x's 8move
//int dy[]={1, 2,  2,  1, -1, -2, -2, -1};//knight's y's 8move
//int dx[] = {+1,-1,+0,+0};//One step x's 4 way move
//int dy[] = {+0,+0,-1,+1};//One step y's 4 way move
//int dx[] = {-1, -1, -1,  0, 0,  1, 1, 1};//One step x's 8 way move
//int dy[] = {-1,  0,  1, -1, 1, -1, 0, 1};//One step y's 8 way move

int main()
{
     freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
int T,t=1;sci(T);
while(T--)
{
    string st,s;int n;
    cin>>st>>n;
    int i,j,k=0,l=0,x,y,len=sz(st);

    for(i=0;i<len-n+1;i++)
    {
        if(st[i]=='-')
        {
          for(j=i;j<i+n;j++)
          {
             if(st[j]=='-')st[j]='+';
             else if(st[j]=='+')st[j]='-';
          }
         l++;
        }

    }

    lp0(i,len)
    {
        if(st[i]=='-'){k=1;break;}
    }
    if(k)
    {
        pf("Case #%d: IMPOSSIBLE\n",t++);
    }
    else
    {
        pf("Case #%d: %d\n",t++,l);
    }


}
    rt 0;
}
