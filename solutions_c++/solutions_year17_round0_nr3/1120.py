#include<bits/stdc++.h>
//#include <boost/multiprecision/cpp_int.hpp>
#define PI acos(-1)
#define fast() ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define ll long long int
#define mem(a,b) memset(a,b,sizeof(a))
#define MX 1000005
#define MXX 1000005
#define  s second
#define f first
#define mod 1000000007
#define inf 200000000000
//int ex[]={1,-1,0,0};
//int wye[]={0,0,1,-1};
using namespace std;
ll t,n,k,an1,an2,cnt=0,now,cur;
set<ll>st;
map<ll,ll>mp;
set<ll>::reverse_iterator rit;
int main()
{
    //fast();
    freopen("C-large.in","r",stdin);
    freopen("output_c_large_file.out","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>n>>k;
        st.insert(n);
        mp[n]=1;
        cnt=0;
        while(1){
            rit=st.rbegin();
            now=mp[*rit],cur=*rit;
            if(cur&1) mp[cur>>1]+=(now<<1),st.insert(cur>>1),an1=cur>>1,an2=an1;
            else mp[cur>>1]+=now,mp[(cur>>1)-1]+=now,st.insert(cur>>1),st.insert((cur>>1)-1),an1=cur>>1,an2=an1-1;
            if(cnt+now>=k){
                break;
            }
            st.erase(cur);
            cnt+=now;
        }
        cout<<"Case #"<<i<<": ";
        cout<<an1<<" "<<an2<<endl;
        mp.clear();
        st.clear();
    }
    return 0;
}
/* 5
1000000 1000000
1000000 1000000
1000000 1000000
1000000 1000000
1000000 1000000
*/
