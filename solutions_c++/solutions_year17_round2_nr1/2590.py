/// In The Name Of Allah
#include<bits/stdc++.h>
#define pb push_back
#define ll long long
#define F first
#define S second
#define OO 100000000
#define mod 1000000007
using namespace std;
const int N=1001000;
int arr[N][5],n,x,s,a,b,c,d,k,t;
long double minT;
int freq[N][5];
int main(){
    freopen("A-large (2).in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    while(t--){
        cin>>d>>n;
        minT=-OO*100;
        for(int i=0 ; i<n ; i++){
            cin>>x>>s;
            if(x>=d) continue;
            double dis=d-x;
            minT=max(minT,(long double)dis/s);
        }
        cout<<"Case #"<<++k<<": ";
        //cout<<minT<<endl;
        cout<<fixed<<setprecision(6)<<(double)d/minT<<endl;
    }
}
