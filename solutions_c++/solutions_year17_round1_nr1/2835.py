#include <bits/stdc++.h>

using namespace std;

int R,C;
int limsz;
bool usedch[500],usedk[500];
int maxR[500],maxC[500],minR[500],minC[500];
char s[100][100];

void initialize(){
    memset(s,0,sizeof s);
    memset(usedk,0,sizeof usedk);
    memset(usedch,0,sizeof usedch);
    memset(maxR,0,sizeof maxR);
    memset(maxC,0,sizeof maxC);
    for (int i=0;i<300;i++)
        minR[i] = minC[i] = 1000;
}

void paint(int r,int c,char ch){
    for (int i=minR[ch];i<=maxR[ch];i++){
        for (int j=minC[ch];j<=maxC[ch];j++){
            s[i][j] = ch;
        }
    }
}

void addAC(char ch){
    maxC[ch]++;
    int nc = maxC[ch];
    for (int i=minR[ch];i<=maxR[ch];i++){
        s[i][nc] = ch;
    }
}

bool isACvalid(char ch){
    if (maxC[ch]+1>C) return false;
    int nc = maxC[ch]+1;
    for (int i=minR[ch];i<=maxR[ch];i++){
        if (s[i][nc] != '?')
            return false;
    }
    return true;
}

void addDR(char ch){
    maxR[ch]++;
    int nr = maxR[ch];
    for (int j=minC[ch];j<=maxC[ch];j++){
        s[nr][j] = ch;
    }
}

bool isDRvalid(char ch){
    if (maxR[ch]+1>R) return false;
    int nr = maxR[ch]+1;
    for (int j=minC[ch];j<=maxC[ch];j++){
        if (s[nr][j] != '?')
            return false;
    }
    return true;
}

void addDC(char ch){
    minC[ch]--;
    int nc = minC[ch];
    for (int i=minR[ch];i<=maxR[ch];i++){
        s[i][nc] = ch;
    }
}

bool isDCvalid(char ch){
    if (minC[ch]<=1) return false;
    int nc = minC[ch]-1;
    for (int i=minR[ch];i<=maxR[ch];i++){
        if (s[i][nc] != '?')
            return false;
    }
    return true;
}

void addUR(char ch){
    minR[ch]--;
    int nr = minR[ch];
    for (int j=minC[ch];j<=maxC[ch];j++){
        s[nr][j] = ch;
    }
}

bool isURvalid(char ch){
    if (minR[ch]-1<1) return false;
    int nr = minR[ch]-1;
    for (int j=minC[ch];j<=maxC[ch];j++){
        if (s[nr][j] != '?')
            return false;
    }
    return true;
}

void paintSes(){
    for (int i=1;i<=R;i++){
        for (int j=1;j<=C;j++){
            if (usedk[s[i][j]]) continue;
            usedk[s[i][j]] = true;
            while (isACvalid(s[i][j])) addAC(s[i][j]);
            while (isDRvalid(s[i][j])) addDR(s[i][j]);
            while (isDCvalid(s[i][j])) addDC(s[i][j]);
            while (isURvalid(s[i][j])) addUR(s[i][j]);
        }
    }
}

void paintrem(){
    for (int i=1;i<=R;i++){
        char tmp = '?';
        for (int j=1;j<=C;j++){
            if (s[i][j] != '?') tmp = s[i][j];
            s[i][j] = tmp;
        }
    }

    for (int j=1;j<=C;j++){
        char tmp = '?';
        for (int i=1;i<=R;i++){
            if (s[i][j] != '?') tmp = s[i][j];
            s[i][j] = tmp;
        }
    }

    for (int i=R;i>=1;i--){
        char tmp = '?';
        for (int j=C;j>=1;j--){
            if (s[i][j] != '?') tmp = s[i][j];
            s[i][j] = tmp;
        }
    }

    for (int j=C;j>=1;j--){
        char tmp = '?';
        for (int i=R;i>=1;i--){
            if (s[i][j] != '?') tmp = s[i][j];
            s[i][j] = tmp;
        }
    }
}

void show(){
    for (int i=1;i<=R;i++){
        for (int j=1;j<=C;j++){
            printf ("%c",s[i][j]);
        }
        printf ("\n");
    }
}

void solve(){
    scanf ("%d%d",&R,&C);
    limsz = min(R,C);
    for (int i=1;i<=R;i++){
        scanf ("%s",&s[i][1]);
    }
    for (int i=1;i<=R;i++){
        for (int j=1;j<=C;j++){
            minR[s[i][j]] = min(minR[s[i][j]],i);
            minC[s[i][j]] = min(minC[s[i][j]],j);
            maxR[s[i][j]] = max(maxR[s[i][j]],i);
            maxC[s[i][j]] = max(maxC[s[i][j]],j);
        }
    }
    for (int i=1;i<=R;i++){
        for (int j=1;j<=C;j++){
            if (s[i][j] != '?' && !usedch[s[i][j]]){
                usedch[s[i][j]] = true;
                //printf ("%c %d %d %d %d\n",s[i][j],minR[s[i][j]],minC[s[i][j]],maxR[s[i][j]],maxC[s[i][j]]);
                paint(i,j,s[i][j]);

            }
        }
    }

    paintSes();
    show();
}

int main(){
    freopen ("A-small-attempt1.in","r",stdin);
    freopen ("A.out","w",stdout);
    int TC;
    scanf ("%d",&TC);
    for (int tc=1;tc<=TC;tc++){
        printf ("Case #%d:\n",tc);
        initialize();
        solve();
    }

    return 0;
}
