#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <climits>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <list>
#include <sstream>  // Required for stringstreams

using namespace std;
typedef   long long ll;

double maxi =999999999999.0;
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("outputcodesmallC.txt", "w", stdout);

    int cases = 0 ;
    cin>>cases;
    for (int kk = 1; kk<cases+1; kk++) {
        printf("Case #%d: ",kk);
        ll N, Q;
        cin>>N>>Q;
        double horse[N+1][2];
        for (int i = 1 ; i<N+1; i++) {
            cin>>horse[i][0]>>horse[i][1];
        }
        double dist[N+1][N+1];
        for (int i=1; i<N+1; i++) {
            for (int j =1 ; j<N+1; j++) {
                cin>>dist[i][j];
                
            }
        }
        
        
        
        
        double city[N+1][N+1];
             ll x, y;
        dist[1][1]=0;
        for (int i=0; i<=N; i++) {
            dist[1][i] = dist[1][i-1]+dist[i-1][i];
        }
        for (int qr = 0 ; qr<Q;qr++) {
            cin>>x>>y;
            
            memset(city,-1,sizeof(city));
            city[2][1]=dist[1][2]/horse[1][1];
            double best[N+1];
            best[1]=0;
            best[2]=city[2][1];
         //   cout<<best[2]<<"*";
            for (int i =3;i<=N;i++) {
                double mina = maxi;
                best[i]=maxi;
                for (int j =1; j<i; j++) {
                    if(horse[j][0]>=dist[1][i]-dist[1][j]) {
                        city[i][j]=best[j]+(dist[1][i]-dist[1][j])/horse[j][1];
                       // cout<<city[i][j]<<"£"<<endl;
                        mina = min(city[i][j],mina);
                    }
                }
                best[i]=mina;
            }
            printf("%.6f ",best[N]);
            
        }
        cout<<endl;
        
    }
    
    
    return 0;
}

