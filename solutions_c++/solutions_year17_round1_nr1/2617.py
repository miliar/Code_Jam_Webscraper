#include <iostream>
#include <fstream>
#include <list>
#include <cstdio>
#include <sstream>
#include <stdlib.h>
#include <time.h>

using namespace std;

void drawat(int R, int C, char **data, int &posx, int &posy)
{
    int hU = posy, hB = posy, vL = posx, vR = posx;
    while(vL > 0)
    {
        char charV = data[posy][vL-1];
        if(data[posy][vL-1])
            break;
        vL--;
    }
    while(vR < C-1)
    {
        char charV = data[posy][vR+1];
        if(data[posy][vR+1])
            break;
        vR++;
    }
    while(hU > 0)
    {
        char charV = data[hU-1][vL];
        if(data[hU-1][vL])
            break;
        hU--;
    }
    for(int i = hU; i < hB + 1; i++)
    {
        for(int j = vL; j < vR + 1; j++)
            data[i][j] = data[posy][posx];
    }

    posx = vR;
}

string fillset(int R, int C, char **data)
{
    for(int i = 0; i < R; i++)
        for(int j = 0; j < C; j++)
        {
            char charV = data[i][j];
            if(data[i][j])
                drawat(R, C, data, j, i);
        }
    string res;
    string lastline;
    for(int j = 0; j < C; j++)
        lastline += data[0][j];
    res += lastline;
    res += "\n";
    int i = 1;
    for(i = 1; i < R; i++)
    {
        if(!data[i][0])
            break;
        lastline = "";
        for(int j = 0; j < C; j++)
            lastline += data[i][j];
        res += lastline;
        if(i < R-1)
            res += "\n";
    }
    for(int j = i; j < R; j++)
    {
        res += lastline;
        if(j < R-1)
            res += "\n";
    }
    return res;
}

int main()
{
    string inname = "A-large.in";
    string outname = "A-large.out";
    ifstream infile(inname);
    ofstream outfile(outname);

    int T = 0;
    infile >> T;
    for(int k = 1; k <= T; k++)
    {
        int R = 0, C = 0;
        infile >> R >> C;
        char **data = new char*[R];
        for(int i = 0; i < R; i++)
            data[i] = new char[C];
        string tmp;
        for(int i = 0; i < R; i++)
        {
            infile >> tmp;
            for(int j = 0; j < C; j++)
            {
                if(tmp[j] == '?')
                    data[i][j] = 0;
                else
                    data[i][j] = tmp[j];
            }
        }
        string res = fillset(R,C,data);
        outfile << "Case #" << k << ":" << endl;
        outfile << res;
        if(k < T)
            outfile << endl;
    }

    infile.close();
    outfile.close();


    /*string inname = "B-large.in";
    string outname = "B-large.out";
    ifstream infile(inname);
    ofstream outfile(outname);

    int T;
    infile >> T;
    string number;
    string res;
    for(int i = 1; i <= T; i++){

        outfile << "Case #" << i <<": " << ;
        if(i < T)
            outfile << endl;
    }
    infile.close();
    outfile.close();*/
    return 0;
}
