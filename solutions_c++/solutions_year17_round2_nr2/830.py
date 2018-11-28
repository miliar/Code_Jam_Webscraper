#include <cstdio>

int main(){
    freopen("B-large (1).in","r",stdin);
    freopen("1bBlargeout.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++){
        int N, R, O, Y, G, B, V;
        scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
        int r = R-G, y = Y-V, b = B-O;
        /*if (r<0||(r==0&&R>0!(O==0&&Y==0&&B==0&&V==0))||y<0||(y==0&&Y>0&&R==0&&O==0&&G==0&&B==0)||b<0||(b==0&&B>0&&!(R==0&&Y==0&&G==0&&V==0))){

        }
        else if (r>y+b||y>b+r||b>y+r){
            printf("Case #%d: IMPOSSIBLE\n", t);
        }
        else
        else if (r>=y&&r>=b){


        }*/
        bool rf = false, yf = false, bf = false;
        if (r<0||y<0||b<0){
            printf("Case #%d: IMPOSSIBLE\n", t);
        }
        else if (r==0&&R>0){
            if (O==0&&Y==0&&B==0&&V==0){
                char S[N+1];
                int ind = 0;
                for (int i = 0; i < R; i++){
                    S[ind++] = 'R';
                    S[ind++] = 'G';
                }
                S[N] = '\0';
                printf("Case #%d: %s\n", t,S);
            }
            else {
                printf("Case #%d: IMPOSSIBLE\n", t);
            }
        }
        else if (y==0&&Y>0){
            if (R==0&&O==0&&G==0&&B==0){
                char S[N+1];
                int ind = 0;
                for (int i = 0; i < Y; i++){
                    S[ind++] = 'Y';
                    S[ind++] = 'V';
                }
                S[N] = '\0';
                printf("Case #%d: %s\n", t,S);
            }
            else {
                printf("Case #%d: IMPOSSIBLE\n", t);
            }
        }
        else if (b==0&&B>0){
            if (R==0&&Y==0&&G==0&&V==0){
                char S[N+1];
                int ind = 0;
                for (int i = 0; i < B; i++){
                    S[ind++] = 'B';
                    S[ind++] = 'O';
                }
                S[N] = '\0';
                printf("Case #%d: %s\n", t,S);
            }
            else {
                printf("Case #%d: IMPOSSIBLE\n", t);
            }
        }
        else if (r>y+b||y>b+r||b>y+r){
            printf("Case #%d: IMPOSSIBLE\n", t);
        }
        else if (r>=y && r>=b){
            char S[N+1];
            int ind = 0;
            for (int i = 0; i < r; i++){
                S[ind++] = 'R';
                if (!rf){
                    for (int j = 0; j < G; j++){
                        S[ind++] = 'G';
                        S[ind++] = 'R';
                    }
                    rf = true;
                }
                if (i<y){
                    S[ind++] = 'Y';
                    if (!yf){
                        for (int j = 0; j < V; j++){
                            S[ind++] = 'V';
                            S[ind++] = 'Y';
                        }
                        yf = true;
                    }
                }
                if (i>=r-b){
                    S[ind++] = 'B';
                    if (!bf){
                        for (int j = 0; j < O; j++){
                            S[ind++] = 'O';
                            S[ind++] = 'B';
                        }
                        bf = true;
                    }
                }
            }
            S[N] = '\0';
            printf("Case #%d: %s\n", t,S);
        }
        else if (y>=r && y>=b){
            char S[N+1];
            int ind = 0;
            for (int i = 0; i < y; i++){
                S[ind++] = 'Y';
                if (!yf){
                    for (int j = 0; j < V; j++){
                        S[ind++] = 'V';
                        S[ind++] = 'Y';
                    }
                    yf = true;
                }
                if (i<r){
                    S[ind++] = 'R';
                    if (!rf){
                        for (int j = 0; j < G; j++){
                            S[ind++] = 'G';
                            S[ind++] = 'R';
                        }
                        rf = true;
                    }
                }
                if (i>=y-b){
                    S[ind++] = 'B';
                    if (!bf){
                        for (int j = 0; j < O; j++){
                            S[ind++] = 'O';
                            S[ind++] = 'B';
                        }
                        bf = true;
                    }
                }
            }
            S[N] = '\0';
            printf("Case #%d: %s\n", t,S);
        }
        else if (b>=y && r<=b){
            char S[N+1];
            int ind = 0;
            for (int i = 0; i < b; i++){
                S[ind++] = 'B';
                if (!bf){
                    for (int j = 0; j < O; j++){
                        S[ind++] = 'O';
                        S[ind++] = 'B';
                    }
                    bf = true;
                }
                if (i<y){
                    S[ind++] = 'Y';
                    if (!yf){
                        for (int j = 0; j < V; j++){
                            S[ind++] = 'V';
                            S[ind++] = 'Y';
                        }
                        yf = true;
                    }
                }
                if (i>=b-r){
                    S[ind++] = 'R';
                    if (!rf){
                        for (int j = 0; j < G; j++){
                            S[ind++] = 'G';
                            S[ind++] = 'R';
                        }
                        rf = true;
                    }
                }
            }
            S[N] = '\0';
            printf("Case #%d: %s\n", t,S);
        }
    }
}
