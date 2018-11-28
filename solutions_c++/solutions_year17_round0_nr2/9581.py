#include<bits/stdc++.h>

using namespace std;
int main (){
long long n,m;
int c=1,d=10,k,x=0,y=0,t;
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
cin>>t;
while(t--){
    k=0;
    scanf("%lld",&n);
    printf("Case #%d: ",c++);
    m=n;
    if(n%d==n){
        printf("%lld\n",n);
        continue;
    }
    x=n%d;
     n=n/d;
    do{ k++;



        y=n%d;
         n=n/d;
        if(x<y){
            m=n*pow(10,k+1)+y*pow(10,k)-1;
            y--;
            }
          x=y;
    }while(n);
    printf("%lld\n",m);
    }


return 0;


}
