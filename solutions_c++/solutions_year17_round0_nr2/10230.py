//By Huseyn Hajiyev
#include <bits/stdc++.h>
//#include <boost/multiprecision/cpp_int.hpp>
//using boost::multiprecision::cpp_int;
#define FAST_READ ios_base::sync_with_stdio(false);
#define in freopen("input.txt", "r", stdin);
#define out freopen("output.txt", "w", stdout);
#define VI vector<int>
#define VIL vector<long long>
#define COUT(n, a) cout<< fixed << setprecision(a) << n<<endl
#define huscout(n) cout<<n<<endl
#define husscanint(n) scanf("%d",&n)
#define husscanll(n) scanf("%lld",&n)
#define husscandouble(n) scanf("%lf",&n)
#define husprintint(n)  printf("%d",n)
#define husprintll(n) printf("%lld",n)
#define MAXN 200010

using namespace std;



string to_string(int n){stringstream ss;ss<<n;string s=ss.str();return s;}
int main(){
in;
out;
FAST_READ;
long long n,cnt,kk,cis,t,tidy;
cin>>t;
for(long long ii=1;ii<=t;ii++){
cin>>n;
for(long long i=n;i>=1;i--){
cis=i;
string ccc=to_string(cis);
cnt=0;
kk=0;/*
while(cis>0)
{
int q=cis%10;
cis/=10;
if(cis%10<=q)cnt++;
kk++;
cout<<q<<endl;
}
*/
//cout<<ccc<<endl;
for(long long iii=0;iii<ccc.size()-1;iii++){
if(ccc[iii]-'0'<=ccc[iii+1]-'0')cnt++;
else break;
//cout<<ccc[iii]-'0'<<" "<<ccc[iii+1]-'0'<<endl;
}
//cout<<cnt<<endl;
//cout<<kk<<endl;
if(cnt==ccc.size()-1){tidy=i;break;}


}
cout<<"Case #"<<ii<<": "<<tidy<<endl;



}

return 0;
}
