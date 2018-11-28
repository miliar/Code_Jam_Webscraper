#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
bool constraintC[24*60];
bool constraintJ[24*60];
int dp[24*60][721][2][2]; // time of day, C time units, first person, last person
int safemin(int a, int b){
    if(a == -1) return b;
    else if(b == -1) return a;
    else return min(a, b);
}
int main(){
    int numcases; scanf("%d", &numcases);
    for(int ccase = 0; ccase < numcases; ccase++){
        memset(constraintC, false, sizeof(constraintC));
        memset(constraintJ, false, sizeof(constraintJ));
        int AC, AJ; scanf("%d%d", &AC, &AJ);
        for(int i = 0; i < AC; i++){
            int from, to; scanf("%d%d", &from, &to);
            for(int i2 = from; i2 < to; i2++){
                constraintC[i2] = true;
            }
        }
        for(int i = 0; i < AJ; i++){
            int from, to; scanf("%d%d", &from, &to);
            for(int i2 = from; i2 < to; i2++){
                constraintJ[i2] = true;
            }
        }
        for(int i = 0; i < 24*60; i++){
            for(int i2 = 0; i2 <= 720; i2++){
                for(int i3 = 0; i3 < 2; i3++){
                    for(int i4 = 0; i4 < 2; i4++){
                        int totunits = i + 1;
                        int Cunits = i2, Junits = totunits - i2;
                        if(i3 == 0){
                            if(constraintC[i]) dp[i][i2][i3][i4] = -1;
                            else if(Cunits < 0 || Junits < 0)
                                dp[i][i2][i3][i4] = -1;
                            else if(Cunits == 0) dp[i][i2][i3][i4] = -1;
                            else if(i == 0){
                                if(i3 != i4) dp[i][i2][i3][i4] = -1;
                                else if(Cunits == 1 && Junits == 0)
                                    dp[i][i2][i3][i4] = 0;
                                else dp[i][i2][i3][i4] = -1;
                            }
                            else{
                                int take = dp[i-1][i2-1][i3][i4];
                                int nottake = dp[i-1][i2-1][1-i3][i4];
                                if(take == -1 && nottake == -1)
                                    dp[i][i2][i3][i4] = -1;
                                else if(take == -1) dp[i][i2][i3][i4] = nottake + 1;
                                else if(nottake == -1) dp[i][i2][i3][i4] = take;
                                else dp[i][i2][i3][i4] = min(take, nottake + 1);
                            }
                        }
                        else{
                            if(constraintJ[i]) dp[i][i2][i3][i4] = -1;
                            else if(Cunits < 0 || Junits < 0)
                                dp[i][i2][i3][i4] = -1;
                            else if(Junits == 0) dp[i][i2][i3][i4] = -1;
                            else if(i == 0){
                                if(i3 != i4) dp[i][i2][i3][i4] = -1;
                                else if(Cunits == 0 && Junits == 1)
                                    dp[i][i2][i3][i4] = 0;
                                else dp[i][i2][i3][i4] = -1;
                            }
                            else{
                                int take = dp[i-1][i2][i3][i4];
                                int nottake = dp[i-1][i2][1-i3][i4];
                                if(take == -1 && nottake == -1)
                                    dp[i][i2][i3][i4] = -1;
                                else if(take == -1) dp[i][i2][i3][i4] = nottake + 1;
                                else if(nottake == -1) dp[i][i2][i3][i4] = take;
                                else dp[i][i2][i3][i4] = min(take, nottake + 1);
                            }
                        }
                        //if(ccase == 0 && i < 10 && i3 == 1 && i2 < 10) printf("%d ", dp[i][i2][i3]);
                    }
                }
            }
            //if(ccase == 0 && i < 10) printf("\n");
        }
        int minCC = dp[24*60 - 1][720][0][0];
        int minJJ = dp[24*60 - 1][720][1][1];
        int minCJ = dp[24*60 - 1][720][0][1];
        int minJC = dp[24*60 - 1][720][1][0];
        if(minCJ != -1) minCJ++;
        if(minJC != -1) minJC++;
        int ans = safemin(safemin(minCC, minJJ), safemin(minCJ, minJC));
        printf("Case #%d: %d\n", ccase + 1, ans);
    }
    return 0;
}
