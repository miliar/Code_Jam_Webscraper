#include <iostream>
#include<bits/stdc++.h>
using namespace std;
typedef vector <int> vi;
typedef vector <long long> vill;

#define sc(a) scanf("%d",&a)
#define scll(a) scanf("%I64d",&a)
#define pf(a) printf("%d\n",a)
#define pfll(a) printf("%I64d\n",a)
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define pb(a) push_back(a)
#define fore(i,a,b) for(i=a;i<b;i++)
#define PI 3.14159265
int tidy(long long n,long long k){
    if(n==0){
        return 1;
    }
    if(n%10<=k){
        return tidy(n/10,n%10);
    }else{
        return 0;
    }
}


int main(){
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long long t,k=0;
    cin>>t;
    while(t--){
        k++;
        long long n,flag=0,l,i;
        cin>>n;
        for(i=n;i>0;i--){
            if(tidy(i/10,i%10))
                break;
        }
        cout<<"Case #"<<k<<": "<<i<<"\n";
    }
    return 0;
}
