#include <iostream>
#include <fstream>


using namespace std;

ifstream fin;
ofstream fout;
int T;
int n,m;
char data[30][30];

void init()
{

    fin.open("input.txt");
    fout.open("output.txt");
    fin>>T;
}

int main() {
    init();
    for (int t0=0;t0<T;t0++)
    {
        fin>>n>>m;
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
            fin>>data[i][j];
        int last;
        bool flag;
        for (int i=0;i<n;i++)
        {
            flag=false;
            for (int j=0;j<m;j++)
                if (data[i][j]!='?')
                {
                    flag=true;
                    last=j;
                    for (int k=j;k>=0;k--)
                        for (int ti=i;ti>=0;ti--)
                        if (data[ti][k]=='?')
                            data[ti][k]=data[i][j];
                }
            if (flag)
            {
                for (int k=last;k<m;k++)
                    for (int ti=i;ti>=0;ti--)
                        if (data[ti][k]=='?')
                            data[ti][k]=data[i][last];
            }
        }
        for (int j=1;j<m;j++)
            if (data[0][j]=='?')
                data[0][j]=data[0][j-1];
        for (int i=1;i<n;i++)
            for (int j=0;j<m;j++)
                if (data[i][j]=='?')
                    data[i][j]=data[i-1][j];
        fout<<"Case #"<<t0+1<<':'<<endl;
        for (int i=0;i<n;i++) {
            for (int j = 0; j < m; j++)
                fout<<data[i][j];
            fout<<endl;
        }
    }

    return 0;
}
