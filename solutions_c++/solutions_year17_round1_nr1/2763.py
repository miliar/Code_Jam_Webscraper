#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

ifstream fin("date.in");
ofstream fout("date.out");

int t, cas;
int n, m;
bool turn;

int i_o, j_o;

char v[32][32];

int di[] = {-1, 1, 0, 0};
int dj[] = {0, 0, -1, 1};

queue < pair < int, int > > Q;

bool walk(int i, int j, int l, int L)
{
    if (i < 0 || j < 0) return false;
    if (i + L > n) return false;
    if (j + l > m) return false;

    for (int i_n = 0; i_n < L; i_n ++)
        for (int j_n = 0; j_n < l; j_n ++)
            if (v[i + i_n][j + j_n] != v[i_o][j_o] && v[i + i_n][j + j_n] != '0')
            {
                return false;
            }
    return true;
}

void rez()
{
    fin >> n >> m;
    char temp;
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
        {
            fin >> temp;
            if (temp != '?')
            {
                v[i][j] = temp;
                Q.push(make_pair(i, j));
            }
            else
            {
                v[i][j] = '0';
            }
        }

    while (!Q.empty())
    {
        int i_c = Q.front().first;
        int j_c = Q.front().second;
        i_o = i_c;
        j_o = j_c;
        int l = 1, L = 1;
        Q.pop();
        turn = true;
        while(true)
        {
            //cout << "da " << i_c << " " << j_c << "\n";
           if (walk(i_c, j_c, l + 1, L))
            l ++;
            else if (walk(i_c, j_c, l, L + 1))
            L ++;
           else if (walk(i_c - 1, j_c, l , L + 1))
           {
            L ++;
            i_c --;
           }
           else if (walk(i_c, j_c - 1, l + 1, L))
           {
            l ++;
            j_c --;
           }
           else
            break;
        }
        temp = v[i_o][j_o];
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < m; j ++)
                if (v[i][j] == temp)
                    v[i][j] = '0';
        v[i_o][j_o] = temp;
        for (int i = 0; i < L; i ++)
            for (int j = 0; j < l; j ++)
                v[i + i_c][j + j_c] = v[i_o][j_o];
    }

    fout << "Case #" << cas << ":\n";
    for (int i = 0; i < n; i ++)
    {
        for (int j = 0; j < m; j ++)
            fout << v[i][j];
        fout << "\n";
    }
}

int main()
{
    fin >> t;
    for (int i = 0; i < t; i ++)
    {
        cas ++;
        rez();
    }
}
