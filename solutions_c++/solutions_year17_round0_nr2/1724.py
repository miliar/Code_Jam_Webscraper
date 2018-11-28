#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<n;++i)

long long gen(long long x,int i){
    while(i--){
        x = x*10+9;
    }
    return x;
}

long long solve(long long n){
    int a[25],b[25];
    int p = 0;
    while(n>0){
        a[p++] = n%10;
        n/=10;
    }
    --p;

   // for(int i=0;i<=p;++i)
  //      cout<<a[i]<<' ';cout<<'\n';

    long long ma = 1;
    long long c=0;
    long long ch = 0;
    a[p+1]=0;
    for(int i=p;i>=0;--i){
        c = c*10+a[i];
        if(a[i]<a[i+1])
            break;
        if(c>ma)
            ma = c;

        if(a[i]==a[i+1])
            continue;

        ch = gen(c-1,i);
//        cout<<"ccc "<<ch<<'\n';
        if(ch>ma)
            ma = ch;
    }
    return ma;
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    string s;
    int n,k;
    forn(i,t){


        long long n;
        cin>>n;

        long long ans = solve(n);

        printf("Case #%d: ",i+1);
        cout<<ans<<'\n';

    }
}
