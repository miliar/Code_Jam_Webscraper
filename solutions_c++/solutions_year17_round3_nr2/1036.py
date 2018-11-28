#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pi;
int Ac, Aj;
vector<pi> inputA, inputB;

int canMerge(pi a, pi b){
    if(b.second-a.first <= 720) {
        return 1;
    }

    if(1440-b.first + a.second <= 720){
        return 1;
    }


    return 0;
}

int main(){ 
    int cases;
    scanf("%d", &cases);

    for(int e = 0; e<cases; e++){
        scanf("%d %d", &Ac, &Aj);
        inputA.clear();
        inputB.clear();

        for(int i =0; i<Ac; i++){
            int x, y;
            scanf("%d %d", &x, &y);
            inputA.push_back(pi(x,y));
        }
        sort(inputA.begin(), inputA.end());

        for(int i =0; i<Aj; i++){
            int x, y;
            scanf("%d %d", &x, &y);
            inputB.push_back(pi(x,y));
        }
        sort(inputB.begin(), inputB.end());

        if((Ac == 1 && Aj == 1) || (Ac==1 && Aj == 0) || (Ac==0 && Aj==1) ){
            printf("Case #%d: %d\n", e+1, 2);
        } else if (Ac == 2) {
            int ans = canMerge(inputA[0], inputA[1]);

            if(ans == 1){
                printf("Case #%d: %d\n", e+1, 2);
            } else {
                printf("Case #%d: %d\n", e+1, 4);
            }
        } else if (Aj == 2){
            int ans = canMerge(inputB[0], inputB[1]);
            if(ans == 1){
                printf("Case #%d: %d\n", e+1, 2);
            } else {
                printf("Case #%d: %d\n", e+1, 4);
            }
        } 

    }


    return 0;
}