#include <bits/stdc++.h>
using namespace std;
char arr[60][60];
int r,c;
int leftUntilBeam(int i,int j) {
    for(int dx = 1;j-dx>=0;dx++) {
        if(arr[i][j-dx] == '#') return -1;
        if(arr[i][j-dx] != '.') return j-dx;
    }
    return -1;
}
int rightUntilBeam(int i,int j) {
    for(int dx = 1;j+dx < c;dx++) {
        if(arr[i][j+dx] == '#') return -1;
        if(arr[i][j+dx] != '.') return j+dx;
    }
    return -1;
}
int upUntilBeam(int i,int j) {
    while(--i >= 0) {
        if(arr[i][j] == '#') return -1;
        if(arr[i][j] != '.') return i;
    }
    return -1;
}
int downUntilBeam(int i,int j) {
    i++;
    while(i < r) {
        if(arr[i][j] == '#') return -1;
        if(arr[i][j] != '.') return i;
        i++;
    }
    return -1;
}
void solve() {
    scanf("%d %d",&r,&c);

    char s[1000];
    for(int i = 0;i < r;i++) {
        scanf("%s",s);
        for(int j = 0;j < c;j++) {
            arr[i][j] = s[j];
            if(arr[i][j] == '|' || arr[i][j] == '-')
                arr[i][j] = '?';
        }
    }
    /*for(int i = 0;i < r;i++) {
        for(int j = 0;j < c;j++) {
            printf("%c",arr[i][j]);
            if(arr[i][j] == '|' || arr[i][j] == '-')
                arr[i][j] = '?';
        }
        printf("\n");
    }
    printf("\n===\n\n");*/
    for(int i = 0;i < r;i++) {
        for(int j = 0;j < c;j++) {
            if(arr[i][j] == '?') {
                // check beam shooter hit
                if(leftUntilBeam(i,j)!=-1 || rightUntilBeam(i,j)!=-1) {
                    // force col
                    arr[i][j] = '|';

                }
                if(upUntilBeam(i,j)!=-1 || downUntilBeam(i,j)!=-1) {
                    arr[i][j] = '-';
                }
            }
        }
    }
    // check free pos
    for(int i = 0;i < r;i++) {
        for(int j = 0;j < c;j++) {
            if(arr[i][j] == '.') {
                // check beam shooter hit
                if(leftUntilBeam(i,j)==-1&& rightUntilBeam(i,j)==-1) {
                    if(upUntilBeam(i,j)!=-1) arr[upUntilBeam(i,j)][j] = '|';
                    else if(downUntilBeam(i,j)!=-1) arr[downUntilBeam(i,j)][j] = '|';
                }
                else if(upUntilBeam(i,j)==-1&& downUntilBeam(i,j)==-1) {
                    if(leftUntilBeam(i,j)!=-1) arr[i][leftUntilBeam(i,j)] = '-';
                    else if(rightUntilBeam(i,j)!=-1) arr[i][rightUntilBeam(i,j)] = '-';
                }
            }
        }
    }
    for(int i = 0;i < r;i++) {
        for(int j = 0;j < c;j++) {
            if(arr[i][j]== '?') {
                arr[i][j] = '-';
            }
        }
    }
    // last check
    bool correct = true;
    for(int i = 0;i < r;i++) {
        for(int j = 0;j < c;j++) {
            if(arr[i][j] == '-') {
                int jj = j;
                while(--jj>=0) {
                    if(arr[i][jj] == '#') break;
                    else if(arr[i][jj] == '-' || arr[i][jj] == '|') {
                        correct = false;
                        break;
                    }
                    else arr[i][jj] = '!';
                }
                jj = j;
                while(++jj<c) {
                    if(arr[i][jj] == '#') break;
                    else if(arr[i][jj] == '-' || arr[i][jj] == '|') {
                        correct = false;
                        break;
                    }
                    else arr[i][jj] = '!';
                }
            }
            else if(arr[i][j] == '|') {
                int ii = i;
                while(--ii>=0) {
                    if(arr[ii][j] == '#') break;
                    else if(arr[ii][j] == '-' || arr[ii][j] == '|') {
                        correct = false;
                        break;
                    }
                    else arr[ii][j] = '!';
                }
                ii = i;
                while(++ii<r) {
                    if(arr[ii][j] == '#') break;
                    else if(arr[ii][j] == '-' || arr[ii][j] == '|') {
                        correct = false;
                        break;
                    }
                    else arr[ii][j] = '!';
                }
            }
        }
    }
    /*for(int i = 0;i < r;i++) {
        for(int j = 0;j < c;j++) {
            printf("%c",arr[i][j]);
        }
        printf("\n");
    }
    printf("BEF\n");*/
    for(int i = 0;i < r;i++) {
        for(int j = 0;j < c;j++) {
            if(arr[i][j] == '.') correct = false;
            else if(arr[i][j] == '!') arr[i][j] = '.';
        }
    }
    if(!correct) printf("IMPOSSIBLE\n");
    else {
        printf("POSSIBLE\n");
        for(int i = 0;i < r;i++) {
            for(int j = 0;j < c;j++) {
                printf("%c",arr[i][j]);
            }
            printf("\n");
        }
    }

}
int main() {
    int tt;
    scanf("%d",&tt);
    for(int i = 0;i < tt;i++) {
        printf("Case #%d: ",i+1);
        solve();
    }
}
