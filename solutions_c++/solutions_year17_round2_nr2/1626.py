#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<queue>
using namespace std;

int main()
{
freopen("B-small-attempt3.in","r",stdin);
freopen("B-small-attempt3.out","w",stdout);
    int T;
    long long N,i,j;
    int C[10];
    int D[6];
    scanf("%d",&T);
    int ca=0;
    while(T--){
        ca++;

        cin>>N;
        char CCC[10]={' ','R','O','Y','G','B','V'};
        for (i=1;i<=6;i++)
            cin>>C[i];
        printf("Case #%d: ",ca);
        memset(D,0,sizeof D);
        D[1]=C[1]+C[2]+C[6];
        D[2]=C[2]+C[3]+C[4];
        D[3]=C[4]+C[5]+C[6];
        if (D[1]*2>N||D[2]*2>N||D[3]*2>N)//||C[1]<C[4]||C[3]<C[6]||C[2]<C[5])
        {

            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
        int first=1;
        for (i=1;i<=6;i=i+2)
            if (C[first]<C[i]) first=i;
            int last=0;
        for (i=1;i<=N;i++)
        {
            int ans;
            ans=first;
            for (j=1;j<=6;j=j+2)
                if (j!=last)
            if (C[ans]<C[j]||ans==last) ans=j;
            C[ans]--;
            last=ans;
            cout<<CCC[ans];
        }
        cout<<endl;
    }



    return 0;
}
