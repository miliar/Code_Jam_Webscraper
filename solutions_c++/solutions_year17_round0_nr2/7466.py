/***********************TUFAAN***********************/
#include<bits/stdc++.h>
#define pi acos(-1.0)
#define pb push_back
#define LL long long
#define LIM 100000
using namespace std;
int _I(){int x; scanf("%d",&x); return x;}
LL _L(){LL x; scanf("%lld",&x); return x;}
LL gcd(LL x,LL y){if(x%y==0) return y; else return gcd(y,x%y);}
LL lcm(LL x,LL y){x/=gcd(x,y); return x*y;}
int kdx[8]={-2,-2,-1,-1,1,1,2,2};
int kdy[8]={-1,1,-2,2,-2,2,-1,1};
bool prime[2];
vector<int> v;
map<int, int> mp;
void sieve(){
    int i,j; prime[1]=1; v.pb(2);
    for(i=4;i<=LIM;i+=2) prime[i]=1;
    for(i=3;i<=LIM;i+=2) if(!prime[i]){ v.pb(i); for(j=i+i+i;j<=LIM;j+=i+i) prime[j]=1;}
}
int cases=0;
string chng(string a, int x){
        if(x == 0){
                if(a[x] == '1'){
                        string temp;
                        int sz = a.size();
                        for(int  i = 1; i < sz; i++){
                                temp += a[i];
                        }
                        return temp;
                }
                else {
                        a[x]--;
                }
                return a;
        }
        if(a[x] == '0' ){
                a[x] = '9';
                a = chng(a,x-1);
        }
        else a[x]--;
        return a;
}
bool chk(string a){
        int l = a.size(),i;
        for(i = 0; i < l-1; i++){
                if(a[i] > a[ i+1 ]) return 0;
        }
        return 1;
}
void lipu_mira(){
        int i,j,k,l;
        string n;
        cin>>n;
        l = n.size();
                bool flag = 1;
                for(i = l-1; i > 0; i--){
                        if(n[i] == '0'){
                                n[i] = '9';
                                n = chng(n, i-1);
                        }
                        else if((n[i] < n[i-1]) || n[i-1] == '0'){
                                n[i] = '9';
                                n = chng(n, i-1);
                        }
                }
                flag = chk(n);
                if(!flag){
                        for(i = 0; i < l-1; i++){
                                if(n[i] > n[ i+1 ]) break;
                        }
                        i++;
                        for( ; i < l; i++){
                                n[i] = '9';
                        }
                }

        printf("Case #%d: ",++cases);
        cout<<n;
        puts("");
}
int main()
{

    //freopen("B-large.in", "r", stdin);
    //freopen("input.txt", "w", stdin);
    //freopen("output.out", "w", stdout);
    //sieve();
    int t = _I();
    while(t--)
    lipu_mira();
    return 0;
}
