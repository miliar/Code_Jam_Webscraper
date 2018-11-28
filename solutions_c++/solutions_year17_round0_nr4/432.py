#include <iostream>
#include <string>
using namespace std;
bool ldig[202], rdig[202],row[101],column[101];
char resm[101][101];
int T,N,M;

bool restmap[101][101],anstmap[101][101];
int anst,rest;
void countt()
{
    if(anst > rest)
    {
        rest = anst;
        for(int i = 1;i<=N;i++)
            for(int j = 1;j<=N;j++)
                restmap[i][j] = anstmap[i][j];
    }
}
void pluss(int cldig)//based on ldig
{
    if(cldig > 2*N-1)
        return countt();
    if(anst + 2*N-cldig + 2 < rest)
        return;
    pluss(cldig+1);
    if(!ldig[cldig]) {
        ldig[cldig] = true;
        int l, r;
        if (cldig <= N)
            l = N - cldig + 1, r = cldig + N - 1;
        else
            l = cldig - N + 1, r = 3 * N - cldig - 1;
        for (int j = l; j <= r; j += 2) {
            if (!rdig[j]) {
                rdig[j] = true;
                anst++;
                anstmap[(1+j+cldig-N)/2][(1+j+N-cldig)/2]=true;
                pluss(cldig + 1);
                anstmap[(1+j+cldig-N)/2][(1+j+N-cldig)/2]=false;
                anst--;
                rdig[j] = false;
            }
        }
        ldig[cldig] = false;
    }
}

bool resxmap[101][101],ansxmap[101][101];
int ansx,resx;
void countxcar()
{
    if(ansx > resx)
    {
        resx = ansx;
        for(int i = 1;i<=N;i++)
            for(int j = 1;j<=N;j++)
                resxmap[i][j] = ansxmap[i][j];
    }
}
void xcar(int crow)//based on row
{
    if(crow > N){
        countxcar();
        return;
    }
    if(ansx + 1+ N-crow < resx)
        return;
    xcar(crow+1);
    if(!row[crow]) {
        row[crow] = true;
        for (int i = 1; i <= N; i++) {
            if (!column[i]) {
                column[i] = true;
                ansx++;
                ansxmap[crow][i]=true;
                xcar(crow + 1);
                ansxmap[crow][i]=false;
                ansx--;
                column[i] = false;
            }
        }
        row[crow] = false;
    }
}
void xcarn()
{
    for(int i = 1;i<=N;i++)
    {
        if(!row[i])
            for(int j = 1;j<=N;j++)
            {
                if(!column[j])
                {
                    row[i]=column[j]=true;
                    resxmap[i][j]=true;
                    resx++;
                    break;
                }
            }
    }
}
void tcarn()
{
    for(int i = 1;i<=2*N-1;i++)
    {
        if(!ldig[i]) {
            int l, r;
            if (i <= N)
                l = N - i + 1, r = i + N - 1;
            else
                l = i - N + 1, r = 3 * N - i - 1;
            for (int j = l; j <= r; j = r)
            {
                if(!rdig[j])
                {
                    ldig[i]=rdig[j]=true;
                    restmap[(1+j+i-N)/2][(1+j+N-i)/2]=true;
                    rest++;
                    break;
                }
                if(j==r)
                    break;
            }
        }
    }
}
char deal(bool x,bool t)
{
    if(x&&t)
        return 'o';
    if(x)
        return 'x';
    if(t)
        return '+';
    return 0;
}
int main()
{
    string model;
    cin >>T;
    for(int i = 1;i<=T;i++) {
        cin >> N >> M;

        int mrow, mcolumn;
        ansx = resx = anst = rest = 0;
        for(int k = 1;k<=N;k++)
        {
            row[k]=column[k]=rdig[k]=rdig[k+N]=ldig[k]=ldig[k+N]=0;
            for(int j = 1;j<=N;j++)
                ansxmap[k][j]=resxmap[k][j]=anstmap[k][j]=restmap[k][j]=resm[k][j]=0;
        }

        for(int j = 1;j<=M;j++)
        {
            cin>>model>>mrow>>mcolumn;
            if(model[0] == 'x' || model[0] == 'o')
            {
                row[mrow] = true;
                column[mcolumn] = true;
                resxmap[mrow][mcolumn] = ansxmap[mrow][mcolumn]=true;
                resx++;
            }
            if(model[0] == '+' || model[0] == 'o')
            {
                ldig[mrow - mcolumn + N] = true;
                rdig[mrow + mcolumn - 1] = true;
                restmap[mrow][mcolumn] = anstmap[mrow][mcolumn]=true;
                rest++;
            }
        }
        //xcar(1);
        //pluss(1);
        xcarn();
        tcarn();
        int count = 0;
        for(int i = 1;i<=N;i++)
            for(int j = 1;j<=N;j++)
            {
                resm[i][j] = deal(resxmap[i][j],restmap[i][j]);
                if(resm[i][j] && deal(ansxmap[i][j],anstmap[i][j])!=resm[i][j])
                    count++;
            }
        cout << "Case #" << i << ": ";
        cout<<resx+rest<<" "<<count<<endl;
        for(int i = 1;i<=N;i++)
            for(int j = 1;j<=N;j++)
                if(resm[i][j] && deal(ansxmap[i][j],anstmap[i][j])!=resm[i][j])
                    cout<<resm[i][j]<<" "<<i<<" "<<j<<endl;
    }
}