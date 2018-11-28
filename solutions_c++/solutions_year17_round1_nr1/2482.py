#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
//#define MY_DEBUG
using namespace std;

char board[32][32];
int R,C;

void readProblem()
{
    scanf("%d %d ",&R,&C);
    for(int i=0;i<R;i++)
        scanf(" %s",board[i]);

    #ifdef MY_DEBUG
    printf("start of problem\n");
    for(int i=0; i<R; i++)
        puts(board[i]);
    #endif // MY_DEBUG
}

struct Rect
{
    int col;
    char a;
    Rect(int n, char c) {
        col=n;
        a=c;
    }
};
struct RowBarrier
{
    int rown;//start row
    vector<Rect> colBarrier;
    RowBarrier(int n) {
        rown=n;
    }
};

void solve()
{
    vector<RowBarrier> rowBar;
    //split by rows
    for(int i=0; i<R; i++)
        for(int j=0; j<C; j++)
            if(board[i][j]!='?') {
                rowBar.push_back(RowBarrier(i));
                break;
            }
    rowBar.push_back(RowBarrier(R));
    const int bn = rowBar.size()-1;
    for(int i=0; i<bn; i++) {
        //split by columes
        const int startW = rowBar[i].rown;
        const int endW = rowBar[i+1].rown;

        for(int k=0; k<C; k++)
            for(int j=startW; j<endW; j++)
                if(board[j][k]!='?')
                    rowBar[i].colBarrier.push_back(Rect(k,board[j][k]));
        rowBar[i].colBarrier.push_back(Rect(C,'?'));
    }
#ifdef MY_DEBUG
    for(int i=0; i<bn; i++) {
        const int startW = rowBar[i].rown;
        const int endW = rowBar[i+1].rown;
        printf("row bar %d\n",i);
        printf("\tstart %2d end %2d\n",startW,endW);
        printf("\tcolumn split:\n");
        int cbn = rowBar[i].colBarrier.size();
        for(int j=0;j<cbn; j++)
            printf("\t\t %c %2d\n",rowBar[i].colBarrier[j].a,rowBar[i].colBarrier[j].col);
        printf("\b");

    }
    system("pause");
#endif // MY_DEBUG
    for(int i=0; i<bn; i++) {
        RowBarrier &row = rowBar[i];
        const int startR = i==0?0:row.rown;
        const int endR = rowBar[i+1].rown;
        int cbn = row.colBarrier.size()-1;
        for(int j=0;j<cbn; j++)
        {
            //fill rectangles
            Rect &rect = row.colBarrier[j];
            const int startC = j==0?0:rect.col;
            const int endC = row.colBarrier[j+1].col;
            #ifdef MY_DEBUG
            printf("start %d end %d\n",startC,endC);
            system("pause");
            #endif // MY_DEBUG

            for(int r=startR;r<endR;r++)
                for(int c=startC;c<endC;c++)
                {
                    #ifdef MY_DEBUG
                    printf("fill %d %d\n",r,c);
                    #endif // MY_DEBUG
                    board[r][c] = rect.a;
                }

        }

    }
}

void printBoard()
{
    for(int r=0;r<R;r++)
        puts(board[r]);
}

int main()
{
    int T = 0;
    scanf("%d",&T);
    for(int i=0; i<T; i++) {
        R=C=0;
        readProblem();
        solve();
        printf("Case #%d:\n",i+1);
        printBoard();
    }

    return 0;
}
