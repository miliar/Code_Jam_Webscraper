#include <bits/stdc++.h>

using namespace std;

const int maxN = 1005;

int need[maxN];
int grid[maxN][maxN];
int L[maxN][maxN] , R[maxN][maxN];
void Solve(int numbercase){

    int ingredients , packages;
    scanf("%d %d",&ingredients,&packages);
    for(int i = 0; i < ingredients; ++i){
        scanf("%d",&need[i]);
    }

    vector<int> possibles;
    for(int i = 0; i < ingredients; ++i){
        for(int k = 0; k < packages; ++k){
            scanf("%d",&grid[i][k]);
        }
        sort(grid[i] , grid[i] + packages);

        for(int k = 0; k < packages; ++k){
            L[i][k] = (grid[i][k] * 10 + 11 * need[i] - 1) / (11 * need[i]);
            R[i][k] = (grid[i][k] * 10) / (9 * need[i]);
            possibles.push_back(L[i][k]);
            possibles.push_back(R[i][k]);
        }
    }
    sort(possibles.begin() , possibles.end());
    int position = 0;
    vector<int> index(ingredients , 0);

    int answer = 0;
    while(position < possibles.size()){
            for(int i = 0; i < ingredients; ++i){
                if(index[i] >= packages){
                    break;
                }
            }

            bool isright = false;
            for(int i = 0; i < ingredients; ++i){
                if(L[i][index[i]] > possibles[position]){
                    isright = true;
                }
            }
            if(isright){
                position++;
                continue;
            }

            for(int i = 0; i < ingredients; ++i){
                while(index[i] < packages && R[i][index[i]] < possibles[position]){
                    index[i]++;
                }
            }
            bool ok = true;
            for(int i = 0; i < ingredients; ++i){
                if(index[i] >= packages || L[i][index[i]] > possibles[position] || R[i][index[i]] < possibles[position]){
                    ok = false;
                }
            }
            if(ok){
                answer++;
                for(int i = 0; i < ingredients; ++i){
                    index[i]++;
                }
            }else{
                position++;
            }
    }
    printf("Case #%d: %d\n",numbercase , answer);

}


int main(){

    freopen("B-large.in","r",stdin);
    freopen("output.c","w",stdout);

    int tc;
    cin >> tc;
    for(int numbercase = 1; numbercase <= tc; numbercase++){
        Solve(numbercase);
    }



    return 0;
}
