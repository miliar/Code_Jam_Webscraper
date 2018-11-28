#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){

        int N,P;
        cin >> N;
        cin >> P;
        int a;
        int G[4]={};
        for (int i = 0;  i <N ; i++){
            cin >> a;
            G[a%P]++;
        }
        int ans = G[0];
        //sprintf("ans1 = %d\n",ans);
        if (P == 2){
            ans += G[1]/2;
            //printf("ans2.1 = %d\n",ans);
            ans += G[1]%2;
            //printf("ans2.2 = %d\n",ans);
        } else if (P == 3){
            int m12 = min(G[1],G[2]);
            int M12 = max(G[1],G[2]);
            ans += m12;
            //printf("ans3.1 = %d\n",ans);
            M12 -= m12;
            ans += M12/3;
            //printf("ans3.2 = %d\n",ans);
            if (M12 %3 > 0){
                ans++;
            }
            //printf("ans3.3 = %d\n",ans);
        } else if (P == 4){
            int m13 = min(G[1],G[3]);
            int M13 = max(G[1],G[3]);
            ans += m13;
            M13-=m13;
            G[2] += M13/2;
            ans += G[2]/2;
            if (G[2] %2 ==1 || M13%2 == 1){
                ans ++;
            }
        }

        printf("Case #%d: %d\n",t,ans);
    }
}
