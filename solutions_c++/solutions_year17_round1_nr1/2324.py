#include <bits/stdc++.h>
using namespace std;

int main() {
    int T, R, C;
    bool used[30];
    char cake[30][30], last_char;
    scanf("%d", &T);
    for (int i=1;i<=T;i++){
        memset(used, false, sizeof(used));
        scanf("%d %d", &R, &C);
        getchar();
        vector<char> available_chars;
        for (int j=0;j<R;j++){
            last_char='?';
            for (int k=0;k<C;k++){
                scanf("%c", &cake[j][k]);
                if (cake[j][k]>=65 && cake[j][k]<=90){
                    used[cake[j][k]-65]=true;
                    last_char=cake[j][k];
                    for (int l=0;l<k;l++){
                        if (cake[j][l]=='?')
                            cake[j][l]=last_char;
                    }
                }
                else if (last_char!='?')
                    cake[j][k]=last_char;
            }
            getchar();
        }
        for (int j=0;j<26;j++){
            if (!used[j]){
                available_chars.push_back(j+65);
            }
        }
        printf("Case #%d:\n", i);
        for (int j=0;j<R;j++){
            if (cake[j][0]!='?'){
                int k=j+1;
                while (k<R && cake[k][0]=='?'){
                    for (int l=0;l<C;l++)
                        cake[k][l]=cake[k-1][l];
                    k++;
                }
                k=j-1;
                while (k>=0&&cake[k][0]=='?'){
                    for (int l=0;l<C;l++)
                        cake[k][l]=cake[k+1][l];
                    k--;
                }
            }
        }
        int idx=0;
        bool contiguous = true;
        for (int j=0;j<R;j++){
            if (!contiguous)
                idx++;
            if (cake[j][0]=='?'){
                for (int k=0;k<C;k++)
                    cake[j][k]=available_chars[idx];
                contiguous=true;
            }
            else{
                contiguous=false;
            }
        }

        for (int j=0;j<R;j++){
            for (int k=0;k<C;k++){
                printf("%c", cake[j][k]);
            }
            printf("\n");
        }
    }
}
