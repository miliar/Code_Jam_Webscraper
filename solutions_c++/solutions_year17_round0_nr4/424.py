#include <cstdio>
#include <algorithm>
#include <cstdlib>
using namespace std;


char a[111][111];
char b[111][111];
int n,m;
bool checkp(int x,int y){
    int t = x + y;
    int p = max(0,t-n+1);
    int q;
    for(int i=p;i<n && t-i>=0;i++){
        if(b[i][t-i] == '+' || b[i][t-i] == 'o')return false;
    }

    t = x - y;

    p = max(0,t);
    q = p + (n-abs(t)); 
    for(int i=p;i<n && i-t<n;i++){
        if(b[i][i-t] == '+' || b[i][i-t] == 'o')return false;
    }
    return true;
}

bool checkx(int x,int y){
    for(int i=0;i<n;i++){
        if(b[i][y] == 'x' || b[i][y] == 'o' || b[x][i] == 'x' || b[x][i] == 'o')return false;
    }
    return true;
}

void setx(int x, int y){
    if(b[x][y] == '.')b[x][y] = 'x';
    else if(b[x][y] == '+')b[x][y] = 'o';
}
void setp(int x, int y){
    if(b[x][y] == '.')b[x][y] = '+';
    else if(b[x][y] == 'x')b[x][y] = 'o';
}

int main(){
    int tcn;
    scanf("%d",&tcn);
    for(int tc=1;tc<=tcn;tc++){
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++)a[i][j]='.';
            a[i][n]=0;
        }
        for(int i=0;i<m;i++){
            char c;
            int x,y;
            scanf("\n%c%d%d",&c,&x,&y);
            a[x-1][y-1] = c;
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<=n;j++){
                b[i][j] = a[i][j];
            }
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(checkx(i,j))setx(i,j);
            }
        }
        for(int i=0;i<n;i++){
            if(checkp(i,0))setp(i,0);
            if(checkp(i,n-1))setp(i,n-1);
            if(checkp(0,i))setp(0,i);
            if(checkp(n-1,i))setp(n-1,i);
        }
        int score = 0;
        int diff = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(b[i][j] == '+' || b[i][j] == 'x')score++;
                else if(b[i][j] == 'o')score+=2;
                if(b[i][j] != a[i][j])diff++;
            }
        }
            
        printf("Case #%d: ",tc);
        printf("%d %d\n",score,diff);
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(b[i][j]!=a[i][j]){
                    printf("%c %d %d\n",b[i][j],i+1,j+1);
                }
            }
        }
    }
}
