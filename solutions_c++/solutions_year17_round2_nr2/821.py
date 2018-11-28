
/*
Contest: Google Code Jam 2017 [Round 1B]
*/


#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;

int n;
int r,o,y,g,b,v;

vector<char> current;

char color[12] = "XRYOBVGX";
int cnt[12];

bool mycmp(const int &ls,const int &rs)
{
    return cnt[ls]>cnt[rs];
}

void noGroupSolver()
{
    char test[1010]; test[n] = '\0';
    int tmp[4] = {1,2,4,99}; sort(tmp,tmp+3,mycmp);
    if(cnt[tmp[0]]>n/2) {printf("IMPOSSIBLE\n"); return;} //Fail
    int high = cnt[tmp[0]];
    int lastCell = 2*high-1;
    int spaceLeft = n-lastCell;
    int det = spaceLeft/2;
    int low = cnt[tmp[2]]; if(low<det) {printf("IMPOSSIBLE\n"); return;} //Fail
    for(int i=0;i<high;i++) test[2*i] = color[tmp[0]];
    //Big Gap Solver
    for(int i=2*(high-1)+1;i<n;i++)
    {
        //printf("FINDING: %d\n",i);
        if(i%2==1) {test[i] = color[tmp[1]];}
        else {test[i] = color[tmp[2]]; low--;}
    }
    //Space
    for(int i=1;i<high;i++)
    {
        if(low>0) {test[2*i-1] = color[tmp[2]]; low--;}
        else test[2*i-1] = color[tmp[1]];
    }
    printf("%s\n",test);
}


void generalSolver()
{
    //printf("GENERALSOLVER\n");
    n = cnt[1]+cnt[2]+cnt[4];
    char test[1010]; test[n] = '\0';
    int tmp[4] = {1,2,4,99}; sort(tmp,tmp+3,mycmp);
    if(cnt[tmp[0]]>n/2) {printf("IMPOSSIBLE\n"); return;} //Fail
    int high = cnt[tmp[0]];
    int lastCell = 2*high-1;
    int spaceLeft = n-lastCell;
    int det = spaceLeft/2;
    int low = cnt[tmp[2]]; if(low<det) {printf("IMPOSSIBLE\n"); return;} //Fail
    for(int i=0;i<high;i++) test[2*i] = color[tmp[0]];
    //Big Gap Solver
    for(int i=2*(high-1)+1;i<n;i++)
    {
        //printf("FINDING: %d\n",i);
        if(i%2==1) {test[i] = color[tmp[1]];}
        else {test[i] = color[tmp[2]]; low--;}
    }
    //Space
    for(int i=1;i<high;i++)
    {
        if(low>0) {test[2*i-1] = color[tmp[2]]; low--;}
        else test[2*i-1] = color[tmp[1]];
    }


    //FINAL PRINT!
    for(int i=0;i<n;i++)
    {
        switch(test[i])
        {
        case 'R':
            if(g<=0) printf("R"); else {for(int i=0;i<g;i++) printf("RG"); printf("R"); g = 0;} break;
        case 'B':
            if(o<=0) printf("B"); else {for(int i=0;i<o;i++) printf("BO"); printf("B"); o = 0;} break;
        case 'Y':
            if(v<=0) printf("Y"); else {for(int i=0;i<v;i++) printf("YV"); printf("Y"); v = 0;} break;
        }
    }
    printf("\n");
}

bool oneGroupSolver(int id)
{
    //printf("ONE SOLVER\n");
    int blocker = 7-id;
    if(cnt[blocker]<cnt[id]) {printf("IMPOSSIBLE\n"); return true;} //Fail
    //Check if there aren't any color
    if(cnt[blocker]==cnt[id]&&cnt[blocker]+cnt[id]==n)
    {
        for(int i=0;i<cnt[blocker];i++) printf("%c%c",color[id],color[blocker]);
        printf("\n"); return true;
    }

    //We need to close a loop!

    return false;

    int blockerCount = cnt[blocker]-(cnt[id]+1);
    if(blockerCount<0) {printf("IMPOSSIBLE\n"); return true;} //Fail
    //Loop Closed
    return false;
}


void each()
{
    scanf("%d",&n);
    scanf("%d%d%d%d%d%d",&r,&o,&y,&g,&b,&v);
    cnt[1] = r; cnt[2] = y; cnt[3] = o;
    cnt[4] = b; cnt[5] = v; cnt[6] = g;
    int special = o+v+g;
    //printf("Special Count: %d\n",special);
    if(special>n/2) {printf("IMPOSSIBLE\n"); return;} //Fail
    if(special==0) {noGroupSolver(); return;}
    //SMALL INPUT HAS NO MULTI COLOR!
    if(o==special) {bool vd = oneGroupSolver(3); if(vd)return;}
    if(v==special) {bool vd = oneGroupSolver(5); if(vd)return;}
    if(g==special) {bool vd = oneGroupSolver(6); if(vd)return;}

    //Let's Close a loop and continue!
    int prime[3] = {1,2,4};
    for(int q=0;q<3;q++)
    {
        int primary = prime[q];
        int trouble = 7-primary;
        if(cnt[trouble]<=0) continue;   //Nothing to Merge!
        cnt[primary]-= (cnt[trouble]+1);
        if(cnt[primary]<0) {printf("IMPOSSIBLE\n",primary); return;} //Fail
        cnt[primary]++;
    }

    generalSolver();
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-Large.txt","w",stdout);
    int tc; scanf("%d",&tc);
    for(int t=1;t<=tc;t++)
    {
        printf("Case #%d: ",t);
        each();
    }
    return 0;
}

