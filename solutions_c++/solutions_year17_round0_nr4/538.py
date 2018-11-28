#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <fstream>
using namespace std;
static const double EPS = 1e-9;
typedef long long ll;
typedef long long LL;
typedef pair<int,int>            PI;
typedef map<PI, int> MPI;
typedef vector<int>	VI;
typedef vector<LL>	VLL;
typedef set<int>	SI;
typedef set<LL>	SLL;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;
#define ALL(c) (c).begin(), (c).end()
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define PB push_back
#define MP make_pair

//#define DEBUG

#define MAXN 100
char Array[MAXN+1][MAXN+1];
int Size;
int ListSize;
char CList[(MAXN)*MAXN];
int RowList[(MAXN)*MAXN];
int ColList[(MAXN)*MAXN];

void ArrayInit(int n)
{
    for(int row = 1; row <= n;row++){
        for(int col = 1 ; col <= n ; col++){
            Array[row][col] = '.';
        }
    }
    Size = n;
    ListSize=0;
}
void ArrayInitAppend(char c, int row, int col)
{
    Array[row][col] = c;
}

char ArrayGet(int row, int col)
{
    return Array[row][col];
}

void ArrayListUpdate(char c, int row, int col)
{
    CList[ListSize] = c;
    RowList[ListSize] = row;
    ColList[ListSize] = col;
    ListSize++;
}
void ArrayUpdate(char c, int row, int col)
{
    Array[row][col] = c;
    ArrayListUpdate(c, row, col);
}
void ArrayCheckAndUpdate(char c, int row, int col)
{
    if(Array[row][col] == '.'){
        Array[row][col] = c;
        ArrayListUpdate(c, row, col);
    }
}
int ArrayGetScore(void)
{
    int n = Size;
    int score = 0;
    for(int row = 1; row <= n;row++){
        for(int col = 1 ; col <= n ; col++){
            char c = Array[row][col];
            if(c == '+' || c == 'x') score++;
            else if (c=='o')score+=2;
        }
    }
    return score;
}
void ArrayPrint(void)
{
    int n = Size;
    for(int row = 1; row <= n;row++){
        for(int col = 1 ; col <= n ; col++){
            cout<< Array[row][col];
        }
        cout<<endl;
    }
}
void ArrayPrintList(void)
{
    for(int i = 0 ; i < ListSize ; i++){
        cout<<CList[i]<<" "<<RowList[i]<<" "<<ColList[i]<<endl;
    }
}
int ArrayGetListSize(void)
{
    return ListSize;
}
void ArrayCheckSyntax(void)
{
    int n = Size;
    char c;
    // 1 horizontal
    for(int row = 1; row <= n;row++){
        int countxo = 0;
        for(int col = 1 ; col <= n ; col++){
            c = Array[row][col];
            if(c=='x' || c=='o')countxo++;
        }
        if(countxo>1){
            cout<<"Syntax error 1 horizontal "<< row<<endl;
        }
    }
    // 2 vertical
    for(int col = 1 ; col <= n ; col++){
        int countxo = 0;
        for(int row = 1; row <= n;row++){
            c = Array[row][col];
            if(c=='x' || c=='o')countxo++;
        }
        if(countxo>1){
            cout<<"Syntax error 2 col "<< col<<endl;
        }
    }
    // 3 diagonal 1
    for(int rc = 2 ; rc <= 2*n ; rc++){
        int countop = 0;
        for(int col = 1; col <=n;col++){
            int row = rc - col;
            if(row<=0 || row>n) continue;
            c = Array[row][col];
            if(c=='+' || c=='o')countop++;
        }
        if(countop>1){
            cout<<"Syntax error 3 diagonal 1 "<< rc<<endl;
        }
    }
    // 4 diagonal 2
    for(int rc = -n ; rc <= n ; rc++){
        int countop = 0;
        for(int col = 1; col <=n;col++){
            int row = rc + col;
            if(row<=0 || row>n) continue;
            c = Array[row][col];
            if(c=='+' || c=='o')countop++;
        }
        if(countop>1){
            cout<<"Syntax error 3 diagonal 1 "<< rc<<endl;
        }
    }
}
int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int N,M;
    cin>>N>>M;
    ArrayInit(N);
    int countx = 0;
    int counto = 0;
    int colx = 0;
    int colo = 0;
    for(int m = 0; m < M ; m++){
        char c;
        int row;
        int col;
        cin>>c>>row>>col;
        ArrayInitAppend(c, row, col);
        if(c=='o'){
            counto++;
            colo = col;
        }
        if(c=='x'){
            countx++;
            colx = col;
        }
    }
    // step 1: row 1
    if(countx != 0){
        ArrayUpdate('o', 1, colx);
        counto++;
        colo = colx;
    }
    if(counto == 0){
        ArrayUpdate('o', 1, N);
        counto = N;
    }
    for(int col = 1 ; col <= N ; col++){
        ArrayCheckAndUpdate('+', 1, col);
    }
    // step2 : put x diagonal line (2, n-1) ... (n, 1) or (2,2) ... (n,n)
    if(ArrayGet(1,1) == 'o'){
        // step2 : put x diagonal line (2, 2) ... (n, n)
        for(int row = 2 ; row <= N ; row++){
            int col = row;
            if(ArrayGet(1, col) != 'o'){
                ArrayCheckAndUpdate('x', row, col);
            }
        }
    }
    else{
        // step2 : put x diagonal line (2, n-1) ... (n, 1)
        for(int row = 2 ; row <= N ; row++){
            int col = N+1 - row;
            if(ArrayGet(1, col) != 'o'){
                ArrayCheckAndUpdate('x', row, col);
            } else{
                ArrayCheckAndUpdate('x', row, N);
            }
        }
    }
    // step 3: put + horizontal line (n, 2)..(n, n-1)
    for(int col = 2;col <= N-1 ; col++){
        ArrayCheckAndUpdate('+', N, col);
    }
    int score = ArrayGetScore();
    int listsize = ArrayGetListSize();
    cout<<"Case #"<<t<<": "<<score<<" "<<listsize<<endl;
    ArrayPrintList();
    //ArrayPrint();
    //ArrayCheckSyntax();
  }
  return 0;
}

