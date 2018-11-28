/*
ID: smfaisa1
LANG: C++
TASK: milk3
*/

//NOTE TO SELF:
//    1.GOtta learn more about hashing base selection and how it affects the probability of collisions
//    2.Expected value eqn building
//    3.2D hashing
//    4.Combinatorics
//    5.

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
long long get_hash(string& str, int a, int b, long long base, int mod, ll hash_val)
{/*from index a to b inclusive of string str*/

    for(int i=a; i<=b; i++)
	{
	    hash_val = hash_val*base + str[i]-'A';
        hash_val%=mod;
	}
	return hash_val;
}
long long extract_hash(ll hash_arr[], ll pow_base[], int a, int b)
{
/*     h1 = extract_hash(hashes, pow_base, 0, i);
 *     h2 = extract_hash(r_hashes, pow_base, len-1-id, len-1-id+i);
 */


    if(a>b) swap(a,b);//cout<<a<<"-"<<b<<endl;
    if(a==0) return hash_arr[b];

    int dis = b-a+1;
    ll temp = hash_arr[b];
    ll temp2 = hash_arr[a-1]*pow_base[dis];
    temp2 %=MOD;

    ll res = temp - temp2;
    res+=MOD;
    res%=MOD;

    return res;
}
void all_hash(ll hashes[], string& str, int len, bool rev = false)
{
/*     To perform a reverse hashing, provide the last param with true.
 *     Otherwise, no need to provide any value at all.
 */

    ll h1=0,h2=0;
    if(!rev)
        go(i, len)
        {
            h1 = get_hash(str, i,i,BASE, MOD, h1);
            hashes[i] = h1;

        }
    else
        go(i, len)
        {
            h2 = get_hash(str, len-i-1,len-i-1,BASE, MOD, h2);
            hashes[i] = h2;
        }
}

ll pow_base[1000000];

int main()
{
	//ios_base::sync_with_stdio(0);  cin.tie(0);
	FI("in.txt");
	FO("output.txt");

	int T;
	cin>>T;
	go(tt,T)
	{
	    int k;
	    string str;
	    cin>>str>>k;
        int res = 0, len = str.length();
        go(i,len-k+1)
        {
            if(str[i]=='+') continue;
            goo(j,i,k+i)
            {
                str[j]=(str[j]=='+'? '-':'+');
            }
            res++;//cout<<i<<" "<<str<<endl;
        }
        bool flag = true;
        goo(i,len-k,len)
        {
            if(str[i]!=str[0]) {
                flag = false;
                break;
            }
        }
        cas(tt+1);
        if(flag) cout<<res<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
	}
    return 0;
}
