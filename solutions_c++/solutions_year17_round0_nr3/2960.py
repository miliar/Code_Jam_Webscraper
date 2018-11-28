  #include<iostream>
  #include<bits/stdc++.h>
  #include<cstdio>
  #include<algorithm>
  #include<vector>
  #include<string>
  #include<map>
  #include<queue>
  #include<cmath>
  #include<math.h>
  #include<stack>
  #include<sstream>
  #include<list>


  using namespace std;


  typedef long long ll;
  typedef long l;

  #define floop(i,n) for(ll i=0;i<n;i++)
  #define floopk(i,n,k) for(ll i=0;i<n;i+=k)
  #define si(n) scanf("%ld",&n)
  #define po(n) printf("%ld",n)


  int main(){

   freopen("C-large.in","r",stdin);
   freopen("sol.txt","w",stdout);
    int t;
    cin>>t;
    for(int x = 1; x <= t; x++){
        long long n, k;
        cin>>n>>k;
        long long lt,rt,xx,yy;
        long long temp = 1;
        long long ans = 0;
        while(ans < k){
            ans+=temp;
            temp*=2;
        }
        temp/=2;
        ans-=temp;
        n-=ans;
        xx = n/(ans+1);
        yy = n%(ans+1);
        k = k-ans;
        if(k <= yy){
            lt = xx/2;
            rt = lt;
            if(xx%2!=0)
                rt++;

        }
        else{
            xx--;
            lt = xx/2;
            rt = lt;
            if(xx%2!=0)
                rt++;
        }
        cout<<"Case #"<<x<<": ";
        cout<<rt<<" "<<lt<<"\n";
    }
    return 0;
  }








