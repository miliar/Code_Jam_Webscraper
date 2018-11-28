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

    freopen("A-large.in","r",stdin);
    freopen("sol.txt","w",stdout);
    int t;
    cin>>t;
    for(int x = 1; x <= t; x++){
        string str;
        cin>>str;
        int n = str.length();
        int k;
        cin>>k;
        int ans = 0;
        bool flag = false;
        for(int i =0; i <= n-k; i++){
            if(str[i]=='-'){
                ans++;
                for(int j = i; j < i+k; j++){
                    if(str[j] == '-')
                        str[j] = '+';
                    else
                        str[j] = '-';
                }
            }
        }
        for(int i = n-k; i < n; i++){
            if(str[i] == '-')
                flag = true;
        }

        cout<<"Case #"<<x<<": ";

        if(flag)
            cout<<"IMPOSSIBLE\n";
        else
            cout<<ans<<"\n";

    }
    return 0;
  }







