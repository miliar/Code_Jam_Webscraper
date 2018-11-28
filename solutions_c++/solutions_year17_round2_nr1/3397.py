#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    double M,R;
    int A,B,T,i,D,N;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
        M=0;
        scanf("%d %d",&D,&N);
        while(N--){
            scanf("%d %d",&A,&B);
            R=D-A;
            R=1.0*R/B;
            M=max(R,M);
        }
        cout<<"Case #"<<i<<": "<<fixed<<setprecision(6)<<D/M<<endl;
    }

    return 0;
}
