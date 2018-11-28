#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../../output.txt");
ifstream fin("../../../input.txt");

char grid[50][50];

bool graph[200][200];
int sats[50][50][2];
int satcount[50][50];

bool ansv[100];

int locs[100][2];
int loccount = 0;

int r,c;

bool cango(int sx, int sy, int dx, int dy)
{
    bool ret = true;
    int currx=sx;
    int curry=sy;
    
    currx+=dx;
    curry+=dy;
    
    while(true)
    {
        //cout << sx << " " << sy << " " << dx << " " << dy << " " << currx << " " << curry << endl;
        if(currx>=r || currx<0 || curry>=c || curry<0)
            return true;
        if(grid[currx][curry]=='#')
            return true;
        if(grid[currx][curry]=='-')
            return false;
        if(grid[currx][curry]=='\\')
           {
               int newx=dy;
               int newy=dx;
               dx=newx;
               dy=newy;
           }
        if(grid[currx][curry]=='/')
        {
            int newx=-dy;
            int newy=-dx;
            dx=newx;
            dy=newy;
        }
        currx+=dx;
        curry+=dy;
    }
    
    
    
    return ret;
}

void runadd(int sx, int sy, int dx, int dy, int seed)
{
 
    
    int currx=sx;
    int curry=sy;
    
    currx+=dx;
    curry+=dy;
    
    while(true)
    {
        if(currx>=r || currx<0 || curry>=c || curry<0)
            return;
        if(grid[currx][curry]=='#')
            return;
        if(grid[currx][curry]=='-')
            return;
        if(grid[currx][curry]=='\\')
        {
            int newx=dy;
            int newy=dx;
            dx=newx;
            dy=newy;
        }
        if(grid[currx][curry]=='/')
        {
            int newx=-dy;
            int newy=-dx;
            currx=dx;
            curry=dy;
        }
        if(grid[currx][curry]=='.')
        {
            sats[currx][curry][satcount[currx][curry]]=seed;
            satcount[currx][curry]++;
        }
        currx+=dx;
        curry+=dy;
    }

}

int mynot(int x)
{
    if(x%2==0)
        return x+1;
    return x-1;
}

int main(void)
{
    int ttt=0;
    fin >> ttt;
    int ct = 0;
    string s;
    
    cout.precision(9);
    fout.precision(9);
    
    cout << "HELLO" <<  " " << ttt << endl;
    
    
    
    while(ttt>0)
    {
        ct++;
        ttt--;
        
        double ans=0.0;
        int i,j,k;
        
        fin >> r >> c;
        loccount=0;
        
        for(i=0; i<r; i++)
        {
            for(j=0; j<c; j++)
            {
                fin >> grid[i][j];
                if(grid[i][j]=='|')
                    grid[i][j]='-';
                if(grid[i][j]=='-')
                {
                    locs[loccount][0]=i;
                    locs[loccount][1]=j;
                    loccount++;
                }
            }
        }
        memset(graph,0,sizeof(graph));
        memset(satcount,0,sizeof(satcount));
        
        for(k=0; k<loccount; k++)
        {
            int cx = locs[k][0];
            int cy = locs[k][1];
            if(cango(cx,cy,0,1) && cango(cx,cy,0,-1))
            {
                // minus sign
                runadd(cx,cy,0,1,2*k);
                runadd(cx,cy,0,-1,2*k);
            }
            else
            {
                //not possible, so implies its negative
                graph[2*k][2*k+1]=true;
            }
            if(cango(cx,cy,1,0)&&cango(cx,cy,-1,0))
            {
                runadd(cx,cy,1,0,2*k+1);
                runadd(cx,cy,-1,0,2*k+1);
            }
            else{
                graph[2*k+1][2*k]=true;
            }
            //cout << k << " " << graph[2*k][2*k+1] << " " << graph[2*k+1][2*k] << endl;
        }
        
        bool isok = true;
        
        for(i=0; i<r; i++)
        {
            for(j=0; j<c; j++)
            {
                if(grid[i][j]!='.')
                    continue;
                if(satcount[i][j]==0)
                    isok=false;
                else if(satcount[i][j]==1)
                {
                    int x = sats[i][j][0];
                    int y = mynot(x);
                    graph[y][x]=true;
                }
                else{
                    int x = sats[i][j][0];
                    int y = sats[i][j][1];
                    graph[mynot(x)][y]=true;
                    graph[mynot(y)][x]=true;
                }
            }
        }
        
        for(k=0; k<2*loccount; k++)
        {
            for(i=0; i<2*loccount; i++)
            {
                for(j=0; j<2*loccount; j++)
                {
                    if(graph[i][k]&& graph[k][j])
                        graph[i][j]=true;
                }
            }
        }
        
        for(k=0; k<2*loccount; k+=2)
        {
            if(graph[k][k+1] && graph[k+1][k])
                isok=false;
        }
        
        
        
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        
        if(!isok)
        {
            cout << "IMPOSSIBLE" << endl;
            fout << "IMPOSSIBLE" << endl;
        }
        else{
            cout << "POSSIBLE" << endl;
            fout << "POSSIBLE" << endl;
            int curr = 0;
            for(i=0; i<r; i++)
            {
                for(j=0; j<c; j++)
                {
                    if(grid[i][j]!='-')
                    {
                        cout << grid[i][j];
                        fout << grid[i][j];
                    }
                    else{
                        char cc = '-';
                        if(graph[2*curr][2*curr+1])
                        {
                            cc='|';
                        }
                        cout << cc;
                        fout << cc;
                        curr++;
                    }
                }
                fout << endl;
                cout << endl;
            }
        }
        
        
    }
    
    
    return 0;
}

