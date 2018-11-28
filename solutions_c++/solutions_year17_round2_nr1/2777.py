/*
ID: smfaisa1
LANG: C++
TASK: numtri
*/
#include <bits/stdc++.h>
using namespace std;
//////////////////Declarations/////////////////////
typedef vector<int> vi;
typedef vector<pair<int, int> > vii;
typedef vector<string> vs;
typedef long long ll;
#define pb push_back
#define mp make_pair
//////////////////Constants////////////////////////
#define PI acos(-1.0)
#define MOD 1000000007
#define BASE 347
#define EPS 1e-9
////////////////////IO/////////////////////////////
#define ln cout<<endl
#define sp cout<<" "
#define cas(x) cout<<"Case #"<<x<<": "

#define FI(x) freopen(x,"r",stdin)
#define FO(x) freopen(x,"w",stdout)
//////////////////loops//////////////////////////////
#define go(i,n) for(int i=0; i<n; i++)
#define goo(i,k,n) for(int i=k; i<n; i++)
#define itr(i,arr,tp) for(tp :: iterator i = arr.begin(); i!=arr.end(); i++)
#define dump(arr,n) for(int i=0; i<n; i++) cout<<arr[i]<<endl;
#define dumpab(arr,a,b) for(int i=a; i<b; i++) cout<<arr[i]<<endl;
#define dump2(arr,row,col) for(int i=0; i<row; i++){for(int j=0; j<col; j++) oi(arr(i));ln;)}
//////////////////Pre-Calc///////////////////////////
#define pow_base_ini(pow_base, pow) pow_base[0]=1;for(int i=1;i<=pow;i++){pow_base[i]=(pow_base[i-1]*BASE)%MOD;pow_base[i]%=MOD;}
//////////////////functions//////////////////////////
vector<string> split(string str, char delim=' ') {
    stringstream ss(str);
    string s;
    vector<string> v;
    while(getline(ss,s,delim)) v.push_back(s);
    return v;
}
long long s2i(string str, int base)
{
    return strtol(str.c_str(), 0, base);
}
template <class T>
int findMin(T arr[],int n)
{
    int i,id=0;
    T m;
    m=arr[0];
    for(i=0;i<n;i++)
    {
        if(m > arr[i]) {
            m=arr[i];
            id=i;
        }
    }
    return id;
}
template <class T>
int findMax(T arr[],int n)
{
    int i,id=0;
    T m;
    m=arr[0];
    for(i=0;i<n;i++)
    {
        if(m < arr[i]) {
            m=arr[i];
            id=i;
        }
    }
    return id;
}

template <typename T>
T mmul(T a, T b, T m) {
    a %= m;
    T result = 0;
    while (b) {
        if (b % 2) result = (result + a) % m;
        a = (a + a) % m;
        b /= 2;
    }
    return result;
}

template <typename T>
T bigmod(T a, T b, T m) {
    a %= m;
    T result = 1;
    while (b) {
        if (b % 2) result = mmul(result, a, m);
        a = mmul(a, a, m);
        b /= 2;
    }
    return result;
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main()
{
    //ios_base::sync_with_stdio(0);  cin.tie(0);
    FI("in.txt");
    FO("output.txt");
    int T;
    cin>>T;
    go(tt, T)
    {
        double n,d,t=0;
        cin>>d>>n;
        go(i,n)
        {
            double k,s;
            cin>>k>>s;
            if((d-k)/s > t) t = (d-k)/s;
        }
        double res = d/t;
        cas(tt+1);
        printf("%.6f\n",res);
    }
    return 0;
}
