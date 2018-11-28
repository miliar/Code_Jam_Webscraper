#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <time.h>
#include <cmath>
#include <memory.h>
#include <string>
#include <vector>
using namespace std;

bool can_placed(int last, int next)
{
    /*
    0 - red
    1 - yellow
    2 - blue
    3 - orange
    4 - green
    5 - violet
    */
    if(last == next)
    {
        return false;
    }
    if(last == 0 && next == 3)return false;
    if(last == 3 && next == 0)return false;
    if(last == 1 && next == 3)return false;
    if(last == 3 && next == 1)return false;
    if(last == 1 && next == 4)return false;
    if(last == 4 && next == 1)return false;
    if(last == 2 && next == 4)return false;
    if(last == 4 && next == 2)return false;
    if(last == 0 && next == 5)return false;
    if(last == 5 && next == 0)return false;
    if(last == 2 && next == 5)return false;
    if(last == 5 && next == 2)return false;
    return true;
}

int pos[10000];

int max(int a, int b, int c)
{
    return max(max(a, b), c);
}

int main()
{
    string file_name = "B-large";
    ifstream f1((file_name+".in").c_str());
    ofstream f2((file_name+".out").c_str());
    int T;
    f1 >> T;
    for(int t = 0; t < T; ++t)
    {
        f2 << "Case #" << t+1 << ": ";
        int N, R, O, Y, G, B, V;
        memset(pos, 0, sizeof pos);
        f1 >> N >> R >> O >> Y >> G >> B >> V;
        R -= G;
        Y -= V;
        B -= O;

        if(R<0 || Y<0 || B<0)
        {
            f2 << "IMPOSSIBLE" << endl;
            continue;
        }

        if(R == 0 && N==2*G && G>0)
        {
            for(int i = 0; i < G; ++i)
                f2 << "RG";
            f2 <<endl;
            continue;
        }
        if(Y==0 && N==2*V && V>0)
        {
            for(int i = 0; i < V; ++i)
                f2 << "YV";
            f2 <<endl;
            continue;
        }
        if(B==0 && N==2*O && O>0)
        {
            for(int i = 0; i < O; ++i)
                f2 << "BO";
            f2 <<endl;
            continue;
        }

        if((R==0 && G>0 && N!=2*G) || (Y==0 && V>0 && N!=2*V || (B==0 && O>0 && N!=2*O)))
        {
            f2 << "IMPOSSIBLE" << endl;
            continue;
        }

        int max_c = -1,max_l;
        if(R > max_c){max_c=R;max_l=1;}
        if(Y > max_c){max_c=Y;max_l=2;}
        if(B > max_c){max_c=B;max_l=3;}

        int min_c=100500,min_l = -1;
        if(R < min_c && max_l != 1){min_c=R;min_l=1;}
        if(Y < min_c && max_l != 2){min_c=Y;min_l=2;}
        if(B < min_c && max_l != 3){min_c=B;min_l=3;}

        int mid_c, mid_l;
        if(max_l != 1 && min_l != 1){mid_c=R;mid_l=1;}
        if(max_l != 2 && min_l != 2){mid_c=Y;mid_l=2;}
        if(max_l != 3 && min_l != 3){mid_c=B;mid_l=3;}
        //cout << min_l << ' ' << mid_l << ' ' << max_l<<endl;

        if(2*max_c - R - Y - B > 0)
        {
            f2 << "IMPOSSIBLE" << endl;
            continue;
        }
        /* R - 1, Y - 2, B - 3*/
        for(int i = 0; i < max_c; ++i)
        {
            pos[i*3 + 0] = max_l;
        }
        for(int i = 0; i < mid_c; ++i)
        {
            pos[i*3 + 1] = mid_l;
        }
        for(int i = max_c-1; i >= max_c-min_c; --i)
        {
            pos[i*3 + 2] = min_l;
        }

        for(int i = 0; i < max_c * 3; ++i)
        {
            if(pos[i] == 0)continue;
            if(pos[i] == 1)
            {
                f2 << "R";
                if(G)
                {
                    for(int j = 0; j < G; ++j)
                        f2 <<"GR";
                    G=0;
                }
            }
            if(pos[i] == 2)
            {
                f2 << "Y";
                if(V)
                {
                    for(int j = 0; j < V; ++j)
                        f2 <<"VY";
                    V=0;
                }
            }
            if(pos[i] == 3)
            {
                f2 << "B";
                if(O)
                {
                    for(int j = 0; j < O; ++j)
                        f2 <<"OB";
                    O=0;
                }
            }
        }
        f2 << endl;
    }
    return 0;
}

