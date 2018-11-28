#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
#include <queue>
#include <unordered_map>

using namespace std;


unordered_map<int, int> dyn[1000];
int taille;

char res[10000];

char trucs[4];

int main()
{
    //ios::sync_with_stdio(false);
    //cin.tie(0);
    freopen("t.out", "w", stdout);
    freopen("t.in", "r", stdin);



    long long nbT;
    cin >> nbT;


    for (long long t = 1; t <= nbT; t++)
    {
        int r,o,y,g,b,v;
        cin >>taille>> r >> o >> y >> g >> b >> v;
        b-=o;
        r-=g;
        y-=v;
        bool isOk=  false;
        for (int i = 0; i < 1000; i++)
            dyn[i].clear();

        if (b >= 0 && r >= 0 && y >= 0)//TODO
        {
            isOk = true;

            int nb1, nb2, nb3;
            if (b >= r && b >= y)
            {
                nb1 = b;
                trucs[1] = 'B';
                if (r >= y)
                {
                    nb2 = r;
                    nb3 = y;
                    trucs[2] = 'R';
                    trucs[3] = 'Y';
                }
                else
                {
                    nb2 = y;
                    nb3 = r;
                    trucs[2] = 'Y';
                    trucs[3] = 'R';
                }
            }

            else if (r >= y && r >= b)
            {
                nb1 = r;
                trucs[1] = 'R';
                if (b >= y)
                {
                    nb2 = b;
                    nb3 = y;
                    trucs[2] = 'B';
                    trucs[3] = 'Y';
                }
                else
                {
                    nb2 = y;
                    nb3 = b;
                    trucs[2] = 'Y';
                    trucs[3] = 'B';
                }
            }

            else
            {
                nb1 = y;
                trucs[1] = 'Y';
                if (b >= r)
                {
                    nb2 = b;
                    nb3 = r;
                    trucs[2] = 'B';
                    trucs[3] = 'R';
                }
                else
                {
                    nb2 = r;
                    nb3 = b;
                    trucs[2] = 'R';
                    trucs[3] = 'B';
                }
            }
            //cout << "mais" << &trucs[1] << endl;


            //isOk = isValid(0, nb1-1, nb2, nb3);
            int pos = 0;
            int nbs[4] = {-1, nb1, nb2, nb3};

            while (nbs[1] > 0 || nbs[2] > 0 || nbs[3] > 0)
            {
               // std::cout << nbs[1] << "a" << nbs[2] << "b" << nbs[3] << "uuuuuuuuuu" << pos << endl;
                int iMax = 1;
                if (nbs[2] > nbs[1])
                    iMax = 2;
                if (nbs[3] > nbs[iMax])
                    iMax = 3;
                int i2Max = iMax==1?2:1;
                for (int i = 1; i < 4; i++)
                    if (i != iMax && nbs[i] > nbs[i2Max])
                        i2Max = i;
                //cout << iMax << "vs" << i2Max << endl;

                int ratio = 0;
                while (ratio*nbs[iMax] <= nbs[1]+nbs[2]+nbs[3])
                {

                        ratio++;
                }
                    ratio--;
                //cout << "ratio = " << ratio << res <<endl;

                if (ratio < 2)
                {
                    //cout << "haha" << endl;
                    isOk = false;
                    break;
                }

                res[pos] = trucs[iMax];
                res[pos+1] = trucs[i2Max];
                nbs[iMax]--;
                nbs[i2Max]--;
                if (ratio ==3)
                {
                    //cout << "lol" << pos+2 <<"\n";
                    if (1 != iMax && 1 != i2Max)
                    {

                        nbs[1]--;
                        res[pos+2] = trucs[1];
                    }
                    else if (2 != iMax && 2 != i2Max)
                    {

                        nbs[2]--;
                        res[pos+2] = trucs[2];
                    }
                    else
                    {

                        nbs[3]--;
                        res[pos+2] = trucs[3];
                    }
                }
                pos+= ratio;



            }

        }


        //cout << "rrrr" << taille << endl;
        std::cout << "Case #" << t << ": ";
        if (!isOk)
            std::cout << "IMPOSSIBLE\n";
        else
        {
            for (int i = 0; i < taille; i++)
                cout << res[i];
            cout << '\n';
        }


    }

    return 0;
}


bool isValid(int pos, int nb1, int nb2, int nb3)
{
    if (pos >= taille)
        return false;

    if (dyn[pos].find(nb1+1000*nb2+1000000*nb3) != dyn[pos].end())
    {
        return dyn[pos][nb1+1000*nb2+1000000*nb3];
    }
    if (nb1 == 0)
    {
        if (max(nb2,nb3)-min(nb2,nb3) > 1)
        {
            dyn[pos][nb1+1000*nb2+1000000*nb3] = false;
            return false;
        }

        if (nb2 > nb3)
        {
//            std::cout << "bbb\n";
            for (int i = pos+1; i < taille; i+=2)
                res[i] = trucs[2];
            for (int i = pos+2; i < taille; i+=2)
                res[i] = trucs[3];
        }
        else
        {
//            std::cout << "cccc" << nb2 << "lol" << nb3 << "\n";
            for (int i = pos+1; i < taille; i+=2)
                res[i] = trucs[3];
            for (int i = pos+2; i < taille; i+=2)
                res[i] = trucs[2];
        }

        dyn[pos][nb1+1000*nb2+1000000*nb3] = true;

        return true;
    }
    if (pos +2 < taille-1)
    {
        bool ok = isValid(pos+2, nb1-1, nb2-1, nb3);
        if (ok)
        {
//            cout << "hhhhhh\n";
            res[pos+2] = trucs[1];
            res[pos+1] = trucs[2];
            return true;
        }
        else
        {
            ok = isValid(pos+2, nb1-1, nb2, nb3-1);
            if (ok)
            {
//                cout << "iiiii\n";

                res[pos+2] = trucs[1];
                res[pos+1] = trucs[3];

                return true;//TODO dyn...
            }
        }
    }

    if (pos+3 < taille-1)
    {
        if (isValid(pos+3, nb1-1, nb2-1, nb3-1))
        {
            res[pos+3] = trucs[1];
            res[pos+1] = trucs[2];
            res[pos+2] = trucs[3];
            return true;
        }
    }

    if (pos+4 < taille-1)
    {
        bool ok = isValid(pos+4, nb1-1, nb2-2, nb3-1);
        if (ok)
        {
            res[pos+4] = trucs[1];
            res[pos+1] = trucs[2];
            res[pos+3] = trucs[2];
            res[pos+2] = trucs[3];
            return true;
        }
        else
        {
            ok = isValid(pos+4, nb1-1, nb2-1, nb3-2);
            if (ok)
            {

                res[pos+4] = trucs[1];
                res[pos+1] = trucs[3];
                res[pos+3] = trucs[3];
                res[pos+2] = trucs[2];
                return true;
            }
        }
    }

    if (pos+5 < taille-1)
    {
        bool ok = isValid(pos+5, nb1-1, nb2-2, nb3-3);
        if (ok)
        {
            res[pos+5] = trucs[1];
            res[pos+1] = trucs[2];
            res[pos+3] = trucs[2];
            res[pos+2] = trucs[3];
            res[pos+4] = trucs[3];
            return true;
        }
    }

    dyn[pos][nb1+1000*nb2+1000000*nb3] = false;
    return false;
}

