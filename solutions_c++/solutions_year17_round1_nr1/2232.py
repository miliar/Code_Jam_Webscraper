#include<stdio.h>
#include<vector>
#include<string.h>

using namespace std;
int n,m;
char mat[30][30];
int di[] = {0,0,1,-1};
int dj[] = {1,-1,0,0};

bool existe(int i, int j){
    return i>=0 && j>=0 && i<n && j<m;
}

bool puede(int i, int j, int k, int cv[4]){
    int ni = i+(cv[k]+1)*di[k];
    int nj = j+(cv[k]+1)*dj[k];
    //printf("%d %d %d\n",k,ni,nj);
    if(!existe(ni,nj)) return false;
    bool ok = true;
    char a = mat[i][j];
    if(k==0 || k==1){
        for(int l=i-cv[3]; l<=i+cv[2]; l++){
            if(mat[l][nj]!=a  && mat[l][nj]!='?'){
                ok = false;
                break;
            }
        }
    }else{
        for(int l=j-cv[1]; l<=j+cv[0]; l++){
            if(mat[ni][l]!=a && mat[ni][l]!='?'){
                ok = false;
                break;
            }
        }
    }
    return ok;
}

void expandir(int i, int j, int k, int cv[4]){
    int ni = i+(cv[k]+1)*di[k];
    int nj = j+(cv[k]+1)*dj[k];
    char a = mat[i][j];
    if(k==0 || k==1){
        for(int l=i-cv[3]; l<=i+cv[2]; l++){
            mat[l][nj] = a;
        }
    }else{
        for(int l=j-cv[1]; l<=j+cv[0]; l++){
            mat[ni][l]= a;
        }
    }
}

void rellenar(int mi, int Mi, int mj, int Mj, char a){
    for(int i=mi; i<=Mi; i++){
        for(int j=mj; j<=Mj; j++){
            mat[i][j] = a;
        }
    }
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,mi,Mi,mj,Mj;
    scanf("%d",&t);
    getchar();
    for(int c=1; c<=t; c++){
        scanf("%d",&n);
        getchar();
        scanf("%d",&m);
        getchar();
        vector<int> let;
        bool check[26];
        memset(check, false, sizeof check);
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                mat[i][j] = getchar();
                if(mat[i][j]!='?'){
                    if(!check[mat[i][j]-'A']){
                        let.push_back(mat[i][j]);
                        check[mat[i][j]-'A'] = true;
                    }
                }
            }
            getchar();
        }
        int s = let.size();
        char a;
        for(int l = 0; l<s; l++){
            mi = 50;
            Mi = 0;
            mj = 50;
            Mj = 0;
            a = let[l];
            for(int i=0; i<n; i++){
                for(int j=0; j<m; j++){
                    if(mat[i][j]==a){
                        if(i<mi) mi = i;
                        if(i>Mi) Mi = i;
                        if(j<mi) mj = j;
                        if(j>Mj) Mj = j;
                    }
                }
            }
            rellenar(mi,Mi,mj,Mj,a);
        }
        memset(check, false, sizeof check);
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(mat[i][j]!='?'){
                    if(!check[mat[i][j]-'A']){
                        int cv[] = {0,0,0,0};
                        for(int k=0; k<4; k++){
                            while(puede(i,j,k,cv)){
                                //printf("bu");
                                expandir(i,j,k,cv);
                                cv[k]++;
                            }
                        }
                        check[mat[i][j]-'A'] = true;
                    }
                }
            }
        }
        printf("Case #%d:\n",c);
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                printf("%c",mat[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
