#include <cstdio>
#include <cstring>

#define REP(i,a,b) for (int i = (a); i < (b); ++i)
#define foreach(i, c) for (__typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)


#define MAX 30

int main () {


    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int TC;
    scanf("%d",&TC);
    int k = 0;

    while(TC--) {

        int R, C;
        scanf("%d %d\n",&R,&C);
        char matrix[MAX][MAX];

        REP (i,0,R) {
            REP(j,0,C) {
                scanf("%c\n",&matrix[i][j]);
            }
        }


        REP(i,0,R) {
            char pintar = '-';
            int flag = 0;
            REP(j,0,C) {
                if (matrix[i][j] != '?') {

                    if (flag == 0)
                        pintar = matrix[i][j];
                    else
                        REP(k,0,flag) {
                            matrix[i][k] = matrix[i][j];
                        }
                            flag = 0;

                        pintar = matrix[i][j];


                }else {
                    if (pintar == '-')
                        flag++;
                    else {
                        matrix[i][j] = pintar;
                        flag = 0;
                    }
                }
            }

           REP(j,0,C)
                if (matrix[i][j] == '?')
                        matrix[i][j] = pintar;
        }



        REP(i,0,C) {
            char pintar = ',';
            int flag = 0;
            REP(j,0,R) {
                if (matrix[j][i] != '-') {

                    if (flag == 0)
                        pintar = matrix[j][i];
                    else
                        REP(k,0,flag) {
                            matrix[k][i] = matrix[j][i];
                            flag = 0;
                            pintar = matrix[j][i];
                        }

                }else {
                    if (pintar == ',')
                        flag++;
                    else {
                        matrix[j][i] = pintar;
                        flag = 0;
                    }
                }
            }

            REP(j,0,R)
                if (matrix[j][i] == ',')
                        matrix[j][i] = pintar;
        }


        REP(i,0,C) {
            char pintar = ',';
            int flag = 0;
            REP(j,0,R) {
                if (matrix[j][i] != '-') {

                    if (flag == 0)
                        pintar = matrix[j][i];
                    else
                        REP(k,0,flag) {
                            matrix[k][i] = matrix[j][i];
                            flag = 0;
                            pintar = matrix[j][i];
                        }

                }else {
                    if (pintar == ',')
                        flag++;
                    else {
                        matrix[j][i] = pintar;
                        flag = 0;
                    }
                }
            }

            REP(j,0,R)
                if (matrix[j][i] == ',')
                        matrix[j][i] = pintar;
        }


        printf("Case #%d:\n",++k);
        REP(i,0,R) {
            REP(j,0,C) {
                printf("%c",matrix[i][j]);
            }
            printf("\n");
        }

    }




return 0;
}
