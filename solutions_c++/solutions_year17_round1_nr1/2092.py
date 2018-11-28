#include <iostream>
#include <cstdio>
using namespace std;

int R, C;
char arr[50][50], tmp;
int frn_mark, bak_mark, top_mark, btn_mark;

void lr_check();
void tb_check();

int main(void){
    int kase;
    cin >> kase;
    for(int cs = 1; cs <= kase; cs++){
        cin >> R >> C;
        tmp = getchar();
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C+1; j++){
                tmp = getchar();
                arr[i][j] = tmp;
            }
        }
        lr_check();
        tb_check();
        cout << "Case #" << cs << ":" << endl;
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++){
                cout << arr[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}

void lr_check(){
    // From left to right
    for(int i = 0; i < R; i++){
        frn_mark = 0;
        for(int j = 0; j < C; j++){
            if(arr[i][j] == '?') frn_mark++;
        }
        if(frn_mark == C){continue;}
        frn_mark = 0;
        for(int j = 0; j < C; j++){
            if(arr[i][j] == '?') frn_mark++;
            else if(arr[i][j] != '?'){
                for(int k = frn_mark; k > 0; k--){
                    arr[i][j-k] = arr[i][j];
                }
                frn_mark = 0;
            }
        }
    }
    // From right to left
    for(int i = 0; i < R; i++){
        bak_mark = 0;
        for(int j = C-1; j >= 0; j--){
            if(arr[i][j] == '?') bak_mark++;
        }
        if(bak_mark == C){continue;}
        bak_mark = 0;
        for(int j = C-1; j >= 0; j--){
            if(arr[i][j] == '?') bak_mark++;
            else if(arr[i][j] != '?'){
                for(int k = bak_mark; k > 0; k--){
                    arr[i][j+k] = arr[i][j];
                }
                bak_mark = 0;
            }
        }
    }
}

void tb_check(){
    //From top to bottom
    for(int j = 0; j < C; j++){
        top_mark = 0;
        for(int i = 0; i < R; i++){
            if(arr[i][j] == '?') top_mark++;
        }
        if(top_mark == R){continue;}
        top_mark = 0;
        for(int i = 0; i < R; i++){
            if(arr[i][j] == '?') top_mark++;
            else if(arr[i][j] != '?'){
                for(int k = top_mark; k > 0; k--){
                    arr[i-k][j] = arr[i][j];
                }
                top_mark = 0;
            }
        }
    }
    // From bottom to top
    for(int j = 0; j < C; j++){
        btn_mark = 0;
        for(int i = R-1; i >= 0; i--){
           if(arr[i][j] == '?') btn_mark++; 
        }
        if(btn_mark == R){continue;}
        btn_mark = 0;
        for(int i = R-1; i >= 0; i--){
            if(arr[i][j] == '?') btn_mark++;
            else if(arr[i][j] != '?'){
                for(int k = btn_mark; k > 0; k--){
                    arr[i+k][j] = arr[i][j];
                }
                btn_mark = 0;
            }
        }
    }
}
