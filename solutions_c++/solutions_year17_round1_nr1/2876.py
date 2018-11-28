#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int t;

char a[25][25];
char tmp[25][25];
int r, c;

vector<pair<int,int> > letters;

bool ok(int i, int j)
{
    if( 0 <= i && i < r && 0 <= j && j < c && a[i][j] == '?')
        return true;
    return false;
}

void fll(int x, int y)
{
    vector<pair<int,int> > lastl;
    vector<pair<int,int> > lastr;

    lastl.push_back(make_pair(x,y));
    lastr.push_back(make_pair(x,y));

    int i = x+1;
    int j = y;

    while(ok(i,j))
    {
        lastl.push_back(make_pair(i,j));
        lastr.push_back(make_pair(i,j));
        i++;
    }
    i = x-1;
    j = y;
    while(ok(i,j))
    {
        lastl.push_back(make_pair(i,j));
        lastr.push_back(make_pair(i,j));
        i--;
    }

    bool b = true;
    while(b == true)
    {
        for(int i = 0; i < lastl.size(); i++)
        {
            a[lastl[i].first][lastl[i].second] = a[x][y];
            lastl[i].second++;
        }
        for(int i = 0; i < lastl.size(); i++)
            if(!ok(lastl[i].first, lastl[i].second))
                b = false;
    }

    b = true;
    while(b)
    {
        for(int i = 0; i < lastr.size(); i++)
        {
            a[lastr[i].first][lastr[i].second] = a[x][y];
            lastr[i].second--;
        }
        for(int i = 0; i < lastr.size(); i++)
            if(!ok(lastr[i].first, lastr[i].second))
                b = false;
    }


}

bool pr()
{
   for(int j = 0; j < r; j++)
        for(int l = 0; l < c; l++)
        {
            if(a[j][l] == '?')
                return false;
        }
    return true;
}

int main()
{
    cout << "Hello world!" << endl;

    ifstream f("date.in");
    ofstream g("date.out");

    f >> t;
    for(int i = 1; i <= t; i++)
    {
        f >> r >> c;
        letters.clear();

        for(int j = 0; j < r; j++)
            for(int l = 0; l < c; l++)
            {
                f >> a[j][l];
                if(a[j][l] != '?')
                    letters.push_back(make_pair(j,l));
            }
        memcpy(tmp,a,sizeof(a));


        for(int k = 0; k < letters.size(); k++)
            fll(letters[k].first, letters[k].second);

        while(!pr())
        {
            memcpy(a,tmp,sizeof(a));
            next_permutation(letters.begin(),letters.end());
            for(int k = 0; k < letters.size(); k++)
                fll(letters[k].first, letters[k].second);
        }

        g << "Case #" << i << ": " << '\n';
        for(int j = 0; j < r; j++)
        {
            for(int l = 0; l < c; l++)
            {
                g << a[j][l];
            }
            g << '\n';
        }
    }


    return 0;
}
