#include<cstdio>
#include<cstring>
using namespace std;

const int MAX = 100 + 10;
char arr[MAX][MAX];
bool fixed[MAX][MAX];
int n, m;

int lfind(int i, int j) {
    int l = j-1;
    while(l >= 0) {
        if(arr[i][l] == '#') break;
        if(arr[i][l] == '-' || arr[i][l] == '|') {
            return l;
        }
        l--;
    }
    return -1;
}

int rfind(int i, int j) {
    int r = j+1;
    while(r < m) {
        if(arr[i][r] == '#') break;
        if(arr[i][r] == '-' || arr[i][r] == '|') {
            return r;
        }
        r++;
    }
    return -1;
}

int ufind(int i, int j) {
    int u = i-1;
    while(u >= 0) {
        if(arr[u][j] == '#') break;
        if(arr[u][j] == '-' || arr[u][j] == '|') {
            return u;
        }
        u--;
    }
    return -1;
}

int dfind(int i, int j) {
    int d = i+1;
    while(d < n) {
        if(arr[d][j] == '#') break;
        if(arr[d][j] == '-' || arr[d][j] == '|') {
            return d;
        }
        d++;
    }
    return -1;
}

bool ltd(int i, int j) {
    if(arr[i][j]!='.') return true;
    int ll = lfind(i,j);
    int rr = rfind(i,j);
    int uu = ufind(i,j);
    int dd = dfind(i,j);
    if(ll != -1 && arr[i][ll] == '-') return true;
    if(rr != -1 && arr[i][rr] == '-') return true;
    if(uu != -1 && arr[uu][j] == '|') return true;
    if(dd != -1 && arr[dd][j] == '|') return true;
    return false;
}

int main() {
    int TN;
    scanf("%d", &TN);
    for(int casen = 1 ; casen <= TN ; casen++) {
        memset(fixed, 0, sizeof(fixed));
        printf("Case #%d: ", casen);
        scanf("%d %d", &n, &m);
        for(int i = 0 ; i < n ; i++) {
            scanf("%s", arr[i]);
        }
        bool get = true;
        for(int i = 0 ; i < n ; i++) {
            for(int j = 0 ; j < m ; j++) {
                if(arr[i][j] == '-' || arr[i][j] == '|') {
                    int ll = lfind(i,j);
                    int rr = rfind(i,j);
                    int uu = ufind(i,j);
                    int dd = dfind(i,j);
                    if((ll != -1 || rr != -1)&&
                       (uu != -1 || dd != -1)){
                        get = false;
                        break;
                    }
                    arr[i][j] = '-';
                    if(ll != -1 || rr != -1) arr[i][j] = '|', fixed[i][j] = true;
                }
            }
            if(!get) break;
        }
        if(!get) puts("IMPOSSIBLE");
        else {
            while(1) {
                int x = -1, y = -1;
                for(int i = 0 ; i < n ; i++) {
                    for(int j = 0 ; j < m ; j++) {
                        if(!ltd(i,j)) {
                            x = i, y = j;
                            break;
                        }
                    }
                    if(x!=-1&&y!=-1) break;
                }
                if(x == -1 && y == -1) break;
                int uu = ufind(x,y);
                int dd = dfind(x,y);
                int tt = uu == -1 ? dd : uu;
                if(tt == -1) {
                    get = false;
                    break;
                }
                if(fixed[tt][y]) {
                    get = false;
                    break;
                }
                arr[tt][y] = '|';
                fixed[tt][y] = true;
            }
            if(!get) puts("IMPOSSIBLE");
            else {
                puts("POSSIBLE");
                for(int i = 0 ; i < n ; i++) {
                    puts(arr[i]);
                }
            }
        }
    }      
    return 0;
}
