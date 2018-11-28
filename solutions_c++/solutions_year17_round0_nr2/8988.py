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
using namespace std;
string tostring(LL n) {stringstream ss; ss << n; return ss.str();}
//LL toint(string s)  { LL sm; stringstream ss(s); ss>>sm; rt sm; /** st=123 to int=123 **/ }

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
int T,t=1;sci(T);
while(T--)
{
   LL n;sc("%lld",&n);
   LL i,j,k,l,a,b,c;
   string st,temp;
   while(1)
   {  l=0;
     st=tostring(n);
   temp=st;
   sort(st.begin(),st.end());
     if(st==temp)break;
     n--;
   }
   pf("Case #%d: ",t++);
    cout<<n<<endl;
}
    rt 0;
}
/*
lp0(i,sz(st))
     {
       b=st[i]-48;
       if(b<a)
       {
         l=1;
       }
       else if(b>a)
       {
           a=b;
       }
       if(l)break;
     }
*/
