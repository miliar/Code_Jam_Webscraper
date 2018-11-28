#include <bits/stdc++.h>

using namespace std;

const int maxN = 33;

char tab[maxN][maxN];


char GetChar(int x1,int y1,int x2,int y2){

    for(int i = x1; i <= x2; ++i){
        for(int k = y1; k <= y2; ++k){
            if(tab[i][k] != '?'){
                return tab[i][k];
            }
        }
    }
    assert(1 == 0);
    return 'X';
}

void Pintar(int x1,int y1,int x2,int y2){

    char character = GetChar(x1,y1,x2,y2);
    for(int i = x1; i <= x2; ++i){
        for(int k = y1; k <= y2; ++k){
                tab[i][k] = character;
        }
    }

}

void Solve(int numbercase){

    int rows , colums;
    cin >> rows >> colums;

    for(int i = 0; i < rows; ++i){
        scanf("%s",tab[i]);
    }

    int last = 0;
    int found = 0;
    for(int i = 0; i <= rows; ++i){
        bool exist = false;
        if(i < rows){
            for(int k = 0; k < colums; ++k){
                if(tab[i][k] != '?'){
                    exist = true;
                }
            }
            if(exist){
                found++;
            }
        }
        if(i == rows || (found > 1 && exist)){
            int x1 = last;
            int x2 = i - 1;

            int f = 0;
            int l = 0;
            for(int k = 0; k <= colums; ++k){
                bool e = false;
                if(k < colums){
                    for(int r = x1; r <= x2; ++r){
                        if(tab[r][k] != '?'){
                            e = true;
                        }
                    }
                    if(e){
                        f++;
                    }
                }
                if(k == colums || (f > 1 && e) ){
                    int y1 = l;
                    int y2 = k - 1;
                    Pintar(x1,y1,x2,y2);
                    l = k;
                }
            }
            last = i;
        }
    }


    printf("Case #%d:\n",numbercase);
    for(int i = 0; i < rows; ++i){
        printf("%s\n",tab[i]);
    }
}


int main(){

    freopen("A-large.in","r",stdin);
    freopen("output.c","w",stdout);

    int tc;
    cin >> tc;
    for(int numbercase = 1; numbercase <= tc; numbercase++){
        Solve(numbercase);
    }



    return 0;
}
