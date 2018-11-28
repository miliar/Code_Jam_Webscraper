#include <iostream>
#include <algorithm>
#include <string>
#include <stdlib.h>
using namespace std;
struct cosa{
    int l[30];
}sum[30][30];
char arr[30][30], ans[30][30];
int t,r,c,caso;
bool usa[30][30],res;
cosa cero;
cosa suma(cosa a, cosa b){
    cosa ans;
    for (int i=0;i<30;i++){
        ans.l[i] = a.l[i]+b.l[i];
    }
    return ans;
}
cosa resta(cosa a, cosa b){
    cosa ans;
    for (int i=0;i<30;i++){
        ans.l[i] = a.l[i]-b.l[i];
    }
    return ans;
}

cosa rango(int x1, int y1, int x2, int y2){
    if (x2<x1){
        swap(x2, x1);
    }
    if (y2<y1){
        swap(y2, y1);
    }
    cosa ans = sum[x2][y2];
    if (x1>0){
        ans = resta(ans, sum[x1-1][y2]);
    }
    if (y1 > 0){
        ans = resta(ans, sum[x2][y1-1]);
    }
    if (x1>0 && y1>0){
        ans = suma(ans, sum[x1-1][y1-1]);
    }
    return ans;
}

int cantidad_letras(cosa a){
    int ans =0;
    for (int i=0;i<30;i++){
        ans += min(1,a.l[i]);
    }
    return ans;
}

int letra_activa(cosa a){
    if (cantidad_letras(a) != 1)
        return -1;
    for (int i=0;i<30;i++){
        if (a.l[i]>0){
            return i;
        }
    }
    return -1;
}

void rellena_ans(int x1,int y1,int x2, int y2,int letra){
    if (x1>x2){
        swap(x1,x2);
    }
    if (y1>y2){
        swap(y1,y2);
    }
    for (int i=x1;i<=x2;i++){
        for (int j=y1;j<=y2;j++){
            ans[i][j] = 'A' + letra;
        }
    }
}

void rellena_usa(int x1,int y1,int x2, int y2,bool val){
    if (x1>x2){
        swap(x1,x2);
    }
    if (y1>y2){
        swap(y1,y2);
    }
    for (int i=x1;i<=x2;i++){
        for (int j=y1;j<=y2;j++){
            usa[i][j] = val;
        }
    }
}

bool hay_usados(int x1,int y1,int x2, int y2){
    if (x1>x2){
        swap(x1,x2);
    }
    if (y1>y2){
        swap(y1,y2);
    }
    for (int i=x1;i<=x2;i++){
        for (int j=y1;j<=y2;j++){
            if (usa[i][j])
                return true;
        }
    }
    return false;
}

void rect(int x, int y){
    int i=x,j=y;
    bool enc = false;
    if (!res){
        if (x<r && y<c){
            while (i<r && !res && !enc){
                while(j<c && !res && !enc){
                    if (!usa[i][j] && !res){
                        enc = true;
                        for (int k=0;k+i<r && !res;k++){
                            for (int l=0;l+j<c && !res;l++){
                                cosa r = rango(i,j,k+i,l+j);
                                int letra = letra_activa(r);
                                if (letra!=-1 && !hay_usados(i,j,i+k,j+l)){
                                    rellena_ans(i,j,i+k,j+l,letra);
                                    rellena_usa(i,j,i+k,j+l, true);
                                    rect(i + ((j<c-1)?0:1),((j<c-1)?j+1:0));
                                    rellena_usa(i,j,i+k,j+l, false);
                                }
                            }
                        }
                    }
                    j++;
                }
                j=0;
                i++;
            }
            if (!enc){
                res = true;
            }
        } else {
            res = true;
        }
    }
}
int main(int argc, const char * argv[]) {
    cin >> t;
    while (t--){
        caso++;
        res = false;
        cin >> r >> c;
        for (int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                sum[i][j] = cero;
                usa[i][j] = false;
                cin >> arr[i][j];
                if (arr[i][j]!='?'){
                    sum[i][j].l[arr[i][j]-'A']++;
                }
                if (i>0){
                    sum[i][j] = suma(sum[i][j], sum[i-1][j]);
                }
                if (j>0){
                    sum[i][j] = suma(sum[i][j], sum[i][j-1]);
                }
                if (i>0 && j>0){
                    sum[i][j] = resta(sum[i][j], sum[i-1][j-1]);
                }
            }
        }
        cout << "Case #" << caso << ":\n";
        rect(0,0);
        for (int i=0;i<r;i++){
            for (int j=0;j<c;j++){
                cout << ans[i][j];
            }
            cout << "\n";
        }
    }
}
