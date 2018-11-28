#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <list>
#include <string.h>
#include <map>

using namespace std;

typedef pair<int, int> coor;

void CleanFree(map<coor, bool>& Free, int r, int c, int n)
{
    for(int i=1; r-i>=0 && c-i>=0; ++i)
    {
        Free[coor(r-i, c-i)] = false;
    }
    for(int i=1; r-i>=0 && c+i<n; ++i)
    {
        Free[coor(r-i, c+i)] = false;
    }
    for(int i=1; r+i<n && c-i>=0; ++i)
    {
        Free[coor(r+i, c-i)] = false;
    }
    for(int i=1; r+i<n && c+i<n; ++i)
    {
        Free[coor(r+i, c+i)] = false;
    }
}

int main()
{
    FILE* in, *out;
    string filename = "D-large";
    string infilename = filename, outfilename = filename;
    infilename+=".in";
    outfilename+=".out";
    if((in=fopen(infilename.c_str(), "rt"))==NULL)
    {
        cout<<"Input file not found."<<endl;
        getchar();
        return 1;
    }
    if((out=fopen(outfilename.c_str(), "wt"))==NULL)
    {
        cout<<"Cannot create output file."<<endl;
        getchar();
        return 2;
    }

    int T;
    fscanf(in, "%d", &T);

    for(int t=0; t!=T; ++t)
    {
        int n, m;
        fscanf(in, "%d %d \n", &n, &m);
        vector<vector<int> > Cell(n, vector<int>(n, 0));
        vector<bool> colHasX(n, false), rowHasX(n, false);
        for(int i=0; i<m; ++i)
        {
            int r, c;
            char type;
            fscanf(in, "%1c %d %d \n", &type, &r, &c);
            --r; --c;
            if(type=='+')
            {
                Cell[r][c] = 1;
            }
            else if(type=='x')
            {
                Cell[r][c] = 2;
                rowHasX[r]=true;
                colHasX[c]=true;
            }
            else if(type=='o')
            {
                Cell[r][c] = 3;
                rowHasX[r]=true;
                colHasX[c]=true;
            }
            else
                cout<<"INPUT FORMAT ERROR"<<endl;

        }

        vector<vector<int> > Orig = Cell;

        for(int r=0, c=0; r<n && c<n; )
        {
            while(rowHasX[r])
                ++r;
            while(colHasX[c])
                ++c;

            if(r<n && c<n)
                Cell[r][c]+=2;

            ++r; ++c;
        }

        map<coor, bool> Free;
        for(int r=0; r<n; ++r)
        {
            for(int c=0; c<n; ++c)
                Free[coor(r, c)] = true;
        }
        for(int r=0; r<n; ++r)
        {
            for(int c=0; c<n; ++c)
            {
                if(Cell[r][c]==1 || Cell[r][c]==3)
                {
                    Free[coor(r, c)] = false;
                    CleanFree(Free, r, c, n);
                }
            }
        }
        for(int d=0; d<=n/2; ++d)
        {
            int r, c;
            for(c=d; c<=n-1-d; ++c)
            {
                r=d;
                if(Free[coor(r, c)])
                {
                    Cell[r][c]+=1;
                    Free[coor(r, c)] = false;
                    CleanFree(Free, r, c, n);
                }
                r=n-1-d;
                if(Free[coor(r, c)])
                {

                    Cell[r][c]+=1;
                    Free[coor(r, c)] = false;
                    CleanFree(Free, r, c, n);
                }
            }
            for(r=d; r<=n-1-d; ++r)
            {
                c=d;
                if(Free[coor(r, c)])
                {
                    Cell[r][c]+=1;
                    Free[coor(r, c)] = false;
                    CleanFree(Free, r, c, n);
                }
                c=n-1-d;
                if(Free[coor(r, c)])
                {
                    Cell[r][c]+=1;
                    Free[coor(r, c)] = false;
                    CleanFree(Free, r, c, n);
                }
            }
        }

        int Value = n;
        int Change = 0;
        for(int r=0; r<n; ++r)
        {
            for(int c=0; c<n; ++c)
            {
                if(Cell[r][c]!=Orig[r][c])
                    ++Change;
                if(Cell[r][c]%2==1)
                    ++Value;
            }
        }

        fprintf(out, "Case #%d: %d %d\n", t+1, Value, Change);

        for(int r=0; r<n; ++r)
        {
            for(int c=0; c<n; ++c)
            {
                if(Cell[r][c]!=Orig[r][c])
                {
                    if(Cell[r][c]==1)
                        fprintf(out, "+");
                    else if(Cell[r][c]==2)
                        fprintf(out, "x");
                    else if(Cell[r][c]==3)
                        fprintf(out, "o");
                    fprintf(out, " %d %d\n", r+1, c+1);
                }
            }
        }
    }

    fclose(in);
    fclose(out);
    return 0;
}
