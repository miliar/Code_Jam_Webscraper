#include <bits/stdc++.h>

using namespace std;

const int nmax = 109;

ifstream fin("input");
ofstream fout("output");

int a[nmax][nmax] , b[nmax][nmax] , c[nmax][nmax] , forbid[nmax][nmax] , used[nmax] , perm[nmax];
int N , M , x , test , tests , y , i , j , answer , curr , answerForPlus , where , total , l , r;
vector < pair < int , pair < int , int > > > moves;
char ch;

void solve()
{
    fin >> N >> M;

    memset(a , 0 , sizeof(a));
    for (i = 1 ; i <= M ; ++i)
    {
        fin >> ch;
        fin >> x >> y;
        if (ch == '+') a[x][y] = 1;
        if (ch == 'x') a[x][y] = 2;
        if (ch == 'o') a[x][y] = 3;
    }

    memset(b , 0 , sizeof(b));
    memset(c , 0 , sizeof(c));

    // solve +
    memset(forbid , 0 , sizeof(forbid));

    for (i = 1 ; i <= N ; ++i)
    for (j = 1 ; j <= N ; ++j)
    if (a[i][j] & 1)
    {
        b[i][j] = 1;
        x = i , y = j;
        while (1 <= x && x <= N && 1 <= y && y <= N) forbid[x][y] = 1 , x-- , y--;
        x = i , y = j;
        while (1 <= x && x <= N && 1 <= y && y <= N) forbid[x][y] = 1 , x++ , y--;
        x = i , y = j;
        while (1 <= x && x <= N && 1 <= y && y <= N) forbid[x][y] = 1 , x-- , y++;
        x = i , y = j;
        while (1 <= x && x <= N && 1 <= y && y <= N) forbid[x][y] = 1 , x++ , y++;
    }

    /*
    cerr << "Forbid : " << '\n';
    for (i = 1 ; i <= N ; ++i , cerr << '\n')
    for (j = 1 ; j <= N ; ++j)
    cerr << forbid[i][j] << " ";
    */

    answerForPlus = 0; where = 1;
    // case 1
    l = N; r = N - 2;
    for (i = 1 ; i <= N ; ++i)
    if (forbid[i][1]) l--;
    for (i = 2 ; i <= N - 1 ; ++i)
    if (forbid[i][N]) r--;

    if (l + r > answerForPlus) answerForPlus = l + r , where = 1;

    //case 2
    l = N; r = N - 2;
    for (i = 1 ; i <= N ; ++i)
    if (forbid[1][i]) l--;
    for (i = 2 ; i <= N - 1 ; ++i)
    if (forbid[N][i]) r--;

    if (l + r > answerForPlus) answerForPlus = l + r , where = 2;

    //case 3
    l = N; r = N - 2;
    for (i = 1 ; i <= N ; ++i)
    if (forbid[i][N]) l--;
    for (i = 2 ; i <= N - 1 ; ++i)
    if (forbid[i][1]) r--;

    if (l + r > answerForPlus) answerForPlus = l + r , where = 3;

    //case 4
    l = N; r = N - 2;
    for (i = 1 ; i <= N ; ++i)
    if (forbid[N][i]) l--;
    for (i = 2 ; i <= N - 1 ; ++i)
    if (forbid[1][i]) r--;

    if (l + r > answerForPlus) answerForPlus = l + r , where = 4;

    if (where == 1)
    {
        for (i = 1 ; i <= N ; ++i)
        if (!forbid[i][1]) b[i][1] = 1;
        for (i = 2 ; i <= N - 1 ; ++i)
        if (!forbid[i][N]) b[i][N] = 1;
    }

    if (where == 2)
    {
        for (i = 1 ; i <= N ; ++i)
        if (!forbid[1][i]) b[1][i] = 1;
        for (i = 2 ; i <= N - 1 ; ++i)
        if (!forbid[N][i]) b[N][i] = 1;
    }

    if (where == 3)
    {
        for (i = 1 ; i <= N ; ++i)
        if (!forbid[i][N]) b[i][N] = 1;
        for (i = 2 ; i <= N - 1 ; ++i)
        if (!forbid[i][1]) b[i][1] = 1;
    }

    if (where == 4)
    {
        for (i = 1 ; i <= N ; ++i)
        if (!forbid[N][i]) b[N][i] = 1;
        for (i = 2 ; i <= N - 1 ; ++i)
        if (!forbid[1][i]) b[1][i] = 1;
    }

    total = 0;
    for (i = 1 ; i <= N ; ++i)
    for (j = 1 ; j <= N ; ++j)
    if (b[i][j]) total++;

    /*
    cerr << "xxxxx : " << '\n';
    for (i = 1 ; i <= N ; ++i , cerr << '\n')
    for (j = 1 ; j <= N ; ++j)
    cerr << b[i][j] << " ";

    cerr << '\n';
    */

    //solve x
    memset(perm , 0 , sizeof(perm));
    memset(used , 0 , sizeof(used));

    for (i = 1 ; i <= N ; ++i)
    for (j = 1 ; j <= N ; ++j)
    if (a[i][j] & 2)
    {
        c[i][j] = 2;
        perm[i] = j;
        used[j] = 1;
    }

    for (i = 1 ; i <= N ; ++i)
    if (!perm[i])
    {
        for (j = 1 ; j <= N ; ++j)
        if (!used[j]) break;

        perm[i] = j;
        used[j] = 1;
        c[i][perm[i]] = 2;
    }

    for (i = 1 ; i <= N ; ++i)
    for (j = 1 ; j <= N ; ++j)
    if (c[i][j]) total++;

    moves.clear();
    for (i = 1 ; i <= N ; ++i)
    for (j = 1 ; j <= N ; ++j)
    {
        int now = b[i][j] + c[i][j];
        if (a[i][j] != now) moves.push_back(make_pair(now , make_pair(i , j)));
    }

    fout << total << " " << moves.size() << '\n';
    for (i = 0 ; i < moves.size() ; ++i)
    {
        if (moves[i].first == 1) fout << "+ ";
        if (moves[i].first == 2) fout << "x ";
        if (moves[i].first == 3) fout << "o ";
        fout << moves[i].second.first << " " << moves[i].second.second << '\n';
    }

    /*
    cerr << "+++++ : " << '\n';
    for (i = 1 ; i <= N ; ++i , cerr << '\n')
    for (j = 1 ; j <= N ; ++j)
    cerr << c[i][j] << " ";
    cerr << '\n';
    */
}

int main()
{

fin >> tests;
for (test = 1 ; test <= tests ; ++test)
{
    fout << "Case #" << test << ": ";
    solve();
}

return 0;
}
