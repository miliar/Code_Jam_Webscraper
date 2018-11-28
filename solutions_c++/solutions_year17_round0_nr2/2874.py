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

    freopen("B-large.in","r",stdin);
    freopen("sol.txt","w",stdout);
    int t;
    cin>>t;
    for(int x = 1; x <= t; x++){
        string str;
        cin>>str;
        int n = str.length();
        int j = n;
        for(int i = 1; i < n; i++){
            if(str[i] < str[i-1]){
                j = i;
                while(i > 0 && str[i-1] > str[i]){
                    str[i-1] = str[i-1]-1;
                    str[i] ='9';
                    i--;
                }
                break;
            }
        }
        for( ; j < n; j++){
            str[j] = '9';
        }


        cout<<"Case #"<<x<<": ";
        if(str[0]=='0'){
            for(int i = 1; i <n; i++)
                cout<<"9";
            cout<<"\n";
        }
        else
            cout<<str<<"\n";

    }
    return 0;
  }








