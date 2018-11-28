#include <stdio.h>
#include <vector>

int P[6];
int X[6];
char corr[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};

int main(){
    int T;
    scanf("%d", &T);

    for (int i = 1; i<=T; i++){
        int N;
        scanf("%d",&N);

        std::vector<int> v;
        for (int j = 0; j<6; j++){
            int T;
            scanf("%d",&T);
            P[j] = T;
            X[j] = 0;
            v.push_back(T);
            //printf("%d\n",T);
        }
        for (int j = 6; j>0; j--){
            int best = 0;
            for (int k = 0; k<6; k++){
                if (v[k]>v[best]){
                    best = k;
                }
            }
            X[best] = j;
            //printf("X %d = %d\n",best,j);
            v[best] = -1;
        }
        std::vector<char> ans;

        int lastIndex = 6;
        int answerFound;
        int answer;
        int isGood = true;
        //printf("Doing test case %d\n",i);
        for (int j = 0; j<N; j++){
            answerFound = false;
            for (int k = 0;k<6; k++){

                if (k!=lastIndex && P[k]>0 &&(!answerFound||P[k]>P[answer]||
                    (P[k]==P[answer] && X[k]>X[answer]))){
                    answerFound = true;
                    answer = k;
                }
            }

            if (!answerFound){
                isGood = false;
                break;
            }

            //printf("answer = %d\n",answer);
            lastIndex = answer;
            P[answer]--;
            ans.push_back(corr[answer]);
        }

        if (!isGood || ans[0]==ans[N-1]){
            printf("Case #%d: IMPOSSIBLE\n",i);
            fprintf(stderr, "Case %d is impossible\n",i);
        } else{
            printf("Case #%d: ",i);
            for (char c: ans){
                printf("%c",c);
            }
            printf("\n");
        }
    }
}
