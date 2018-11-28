#include <bits/stdc++.h>
using namespace std;
using ll=long long;
int cas;

// const int N=105;
// int s[N], e[N];
// int d[N][N];


// double dp[N][N][N];

// void floyd(int n){

// }


pair<int,char> a[6], b[3];

const char *s="ROYGBV";
int main(){
    int T;
    cin >> T;
    for(; T--; ){
        printf("Case #%d: ", ++cas);
        // //////////////////////////////////

        int n;
        cin >> n;
        int ma=0;

        for(int i=0; i<6; i++){
            cin >> a[i].first;
            ma=max(ma, a[i].first);
            a[i].second=s[i];
        }

        if(ma>n/2){
            puts("IMPOSSIBLE");

            continue;
        }

        b[0]=a[0], b[1]=a[2], b[2]=a[4];
        sort(b, b+3, greater<pair<int,char>>());

        int c1=n-2*b[0].first;
        int c2=b[1].first-c1;
        int c3=b[2].first-c1;

        // int c4=a[0].first-c1;
        // int b0=0,b1=0, b2=0;
        for(int i=0; i<c1; i++){
            putchar(b[0].second), putchar(b[1].second), putchar(b[2].second);
            // b0++, b1++, b2++;
        }
        for(int i=0; i<c2; i++){
            putchar(b[0].second), putchar(b[1].second);
            // b0++, b1++;
        }
        for(int i=0; i<c3; i++){
            // b0++, b2++;
            putchar(b[0].second), putchar(b[2].second);
        }
        puts("");
        // assert(b0==a[0].first && b1==a[1].first && b2==a[2].first);

        // int n, q;
        // cin >> n >>  q;
        // for(int i=0; i<n; i++)
        //     cin >> e[i] >> s[i];
        // for(int i=0; i<n; i++)
        //     for(int j=0; j<n; j++)
        //         cin >> d[i][j];

        // for(int i=0; i<n; i++)
        //     d[i][i]=0;

        // for(int i=0; i<n; i++)
        //     for(int j=0; j<n; j++)
        //         for(int k=0; k<n; k++)
        //             if(i==j && k==i) dp[i][j][k]=0;
        //             else dp[i][j][k]=-1;

        // for(int i=0; i<n; i++)
        //     for(int j=i+1; j<n; j++)
        //         if(d[i][j-1]!=-1 && d[j-1][j]!=-1)
        //             d[i][j]=d[i][j-1]+d[j-1][j];

        // for(int i=0; i<n; i++)
        //     for(int j=i+1; j<n; j++)
        //         for(int k=i; k<j; k++)
        //             if(d[k][k]!=-1)





        // for(int k=0; k<n; k++)
        //     for(int i=0; i<n; i++)
        //         for(int j=0; j<n; j++)
        //             if(i!=j && i!=k && j!=k && d[i][k]!=-1 && dp[k][j]!=-1)




        /////////////////////////////////////////////

    }
    return 0;
}