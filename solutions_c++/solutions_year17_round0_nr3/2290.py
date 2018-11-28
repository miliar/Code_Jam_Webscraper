#include <bits/stdc++.h>
#define mx 100011
#define mp make_pair
#define pb push_back
#define ppb pop_back
#define mod 1000000009
#define ff first
#define ss second
#define ll long long
#define PII pair<int,int>
#define inf 1000000000000000
#define RIGHT 131072
#define SIZE 262144
using namespace std;
void solve(ll n,ll k){
    if(k==1){
        cout<<n/2<<" "<<(n-1)/2<<endl;
        return;
    }
    k--;
    ll val1=(n-1)/2,val2=n/2;
    ll freq1=1,freq2=1;
    for(ll i=1;i<600;i++){
        ll temp = freq1+freq2;
        if(temp>=k){
            if(freq2>=k){
                cout<<val2/2<<" "<<(val2-1)/2<<endl;
            }
            else{
                cout<<val1/2<<" "<<(val1-1)/2<<endl;
            }
            return;
        }
        k-=temp;
        set<ll>myset;
        set<ll>::iterator it;
        myset.insert(val1/2);
        myset.insert(val2/2);
        myset.insert((val1-1)/2);
        myset.insert((val2-1)/2);
        ll val3=0,val4=0,freq3=0,freq4=0;
        if(myset.size()==2){
            it=myset.begin();
            val3 = *it;
            it++;
            val4 = *it;
            if(val1/2==val3)freq3+=freq1;
            if( (val1-1)/2==val3 )freq3+=freq1;
            if(val2/2==val3)freq3+=freq2;
            if( (val2-1)/2==val3 )freq3+=freq2;

            if(val1/2==val4)freq4+=freq1;
            if( (val1-1)/2==val4 )freq4+=freq1;
            if(val2/2==val4)freq4+=freq2;
            if( (val2-1)/2==val4 )freq4+=freq2;
        }
        else{
            it=myset.begin();
            val3 = *it;
            val4 = *it;
            freq3 += 2*freq1;
            freq4 += 2*freq2;
        }
        val1 = val3;
        val2 = val4;
        freq1= freq3;
        freq2= freq4;
        if(val1==0){
            val1=val2;
            freq1=freq2/2;
            freq2=freq2-freq1;
        }
        if(val1==0 && val2==0){
            cout<<"0 0"<<endl;
            return;
        }
        //cout<<i<<endl;
    }
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    ll t;
    scanf("%lld",&t);
    ll caseno=0;
    while(t--){
        ll n,k;
        cin>>n>>k;
        cout<<"Case #"<<++caseno<<": ";
        solve(n,k);
    }
    return 0;
}
