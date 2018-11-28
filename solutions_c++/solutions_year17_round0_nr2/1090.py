#include<bits/stdc++.h>
//#include <boost/multiprecision/cpp_int.hpp>
#define PI acos(-1)
#define fast() ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define ll long long int
#define mem(a,b) memset(a,b,sizeof(a))
#define MX 100005
#define MXX 1000005
#define  s second
#define f first
#define mod 1000000007
#define inf 200000000000
//int ex[]={1,-1,0,0};
//int wye[]={0,0,1,-1};
using namespace std;
int t,k,a[25],tmp,siz;
string s;
bool flag;

int main()
{
    //fast();
    freopen("B-large.in","r",stdin);
    freopen("output_b_large_file.out","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>s;
        siz=s.size();
        for(int j=0;j<siz;j++) a[j]=s[j]-'0';
        for(int j=siz-1;j>0;j--){
            if(a[j]<a[j-1]){
                a[j-1]--;
                tmp=j;
                while(tmp<siz) a[tmp]=9,tmp++;
            }
        }
        if(a[0]==0) tmp=1;
        else tmp=0;
        cout<<"Case #"<<i<<": ";
        for(int j=tmp;j<siz;j++) cout<<a[j];
        cout<<endl;
    }
    return 0;
}

