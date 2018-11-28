#include <iostream>

const int MAX = 30;

char tab[MAX][MAX];
int R,C;

void ExplodeCol(int c)
{
    char last = '?';
    for (int r=0;r<R;++r)
    {
        if (tab[r][c] == '?')
            tab[r][c] = last;
        last = tab[r][c];
    }
    last = '?';
    for (int r=R-1;r>=0;--r)
    {
        if (tab[r][c] == '?')
            tab[r][c] = last;
        last = tab[r][c];
    }
}

void ExplodeRow(int r)
{
    char last = '?';
    for (int c=0;c<C;++c)
    {
        if (tab[r][c] == '?')
            tab[r][c] = last;
        last = tab[r][c];
    }
    last = '?';
    for (int c=C-1;c>=0;--c)
    {
        if (tab[r][c] == '?')
            tab[r][c] = last;
        last = tab[r][c];
    }
}
void Solve(int T)
{
    std::cin >> R >> C;
    for (int r=0;r<R;++r)
        for (int c=0;c<C;++c)
            std::cin >> tab[r][c];

    for (int c=0;c<C;++c)
        ExplodeCol(c);
    for (int r=0;r<R;++r)
        ExplodeRow(r);

    std::cout << "Case #" << T << ":\n";

    for (int r=0;r<R;++r)
    {
        for (int c=0;c<C;++c)
            std::cout << tab[r][c];
        std::cout << "\n";
    }
}

int main()
{
    int T;
    std::cin >> T;
    for (int i=1;i<=T;++i)
        Solve(i);
    return 0;
}