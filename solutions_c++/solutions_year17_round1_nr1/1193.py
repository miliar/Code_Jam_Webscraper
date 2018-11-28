#include <bits/stdc++.h>
using namespace std;

const int maxR = 30, maxC = 30;
int r, c;
char table[maxR][maxC];



void work(){
    scanf("%d %d\n", &r, &c);
    for (int i = 0; i < r; ++i)
    {
        char line[maxC];
        scanf("%s\n", line);
        for (int j = 0; j < c; ++j)
        {
            table[i][j] = line[j];
        }
    }

    for(int i = 0; i < r; i++)
        for(int j = 0; j < c; j++){
            if(table[i][j] != '?'){
                int k = j-1;
                while(k >= 0 && table[i][k] == '?'){
                    table[i][k] = table[i][j];
                    k--;
                }
                k = j + 1;
                while(k < c && table[i][k] == '?'){
                    table[i][k] = table[i][j];
                    k++;
                }     
            }
        }
 
    int s = 0;
    while(table[s][0] == '?')
        s++; 

    if(s > 0){
        for(int ii = 0; ii < s; ii++)
            for(int j = 0; j < c; j++)
                table[ii][j] = table[s][j];
    }
     
    for(int i = s+1; i < r; i++){
        if(table[i][0] == '?'){
            for(int j = 0; j < c; j++)
                table[i][j] = table[i-1][j];
        }
    }

    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++)
            putchar(table[i][j]);
        putchar('\n');
    }

    return;
}

int main(){
    int t;
    scanf("%d\n", &t);
    for(int i = 1; i <= t; i++){
        printf("Case #%d: \n", i);
        work();
    }
    return 0;
}