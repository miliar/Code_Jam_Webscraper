#include <bits/stdc++.h>
using namespace std;

ifstream fin("A-small-attempt2.in");
ofstream fout("A-small-attempt2.out");

int r,c,f,t;

char ch[26][26];

vector<int>x[26];
vector<int>y[26];

int A[26][4];

void expand(int n)
{
    int i;
    if(f==1)return;
    if(A[n][0]>0)
    {
        for(i=A[n][1];i<=A[n][3];i++)
        {
            if(ch[A[n][0]-1][i]!='?')break;
        }
        if(i>A[n][3])
        {
            for(i=A[n][1];i<=A[n][3];i++)ch[A[n][0]-1][i]=char('A'+n);
            A[n][0]--;
            expand(n);
        }
    }
    if(A[n][2]<r-1)
    {
        for(i=A[n][1];i<=A[n][3];i++)
        {
            if(ch[A[n][2]+1][i]!='?')break;
        }
        if(i>A[n][3])
        {
            for(i=A[n][1];i<=A[n][3];i++)ch[A[n][2]+1][i]=char('A'+n);
            A[n][2]++;
            expand(n);
        }
    }
    if(A[n][1]>0)
    {
        for(i=A[n][0];i<=A[n][2];i++)
        {
            if(ch[i][A[n][1]-1]!='?')break;
        }
        if(i>A[n][2])
        {
            for(i=A[n][0];i<=A[n][2];i++)ch[i][A[n][1]-1]=char('A'+n);
            A[n][1]--;
            expand(n);
        }
    }
    if(A[n][3]<c-1)
    {
        for(i=A[n][0];i<=A[n][2];i++)
        {
            if(ch[i][A[n][3]+1]!='?')break;
        }
        if(i>A[n][2])
        {
            for(i=A[n][0];i<=A[n][2];i++)ch[i][A[n][3]+1]=char('A'+n);
            A[n][3]++;
            expand(n);
        }
    }
    f=1;
    return ;
}

int main()
{
    fin>>t;
    for(int i=0;i<t;i++)
    {
        fin>>r>>c;
        for(int j=0;j<26;j++)
        {
            x[j].clear();
            y[j].clear();
        }
        for(int j=0;j<r;j++)
        {
            for(int k=0;k<c;k++)
            {
                fin>>ch[j][k];
                if(ch[j][k]!='?')
                {
                    x[ch[j][k]-'A'].push_back(j);
                    y[ch[j][k]-'A'].push_back(k);
                }
            }
        }
        for(int j=0;j<26;j++)
        {
            sort(x[j].begin(),x[j].end());
            sort(y[j].begin(),y[j].end());
            if(x[j].size()>0)
            {
                for(int k=x[j][0];k<=x[j][x[j].size()-1];k++)
                {
                    for(int l=y[j][0];l<=y[j][y[j].size()-1];l++)ch[k][l]=char('A'+j);
                }
            }
        }
        for(int j=0;j<26;j++)
        {
            if(x[j].size()>0)
            {
                f=0;
                A[j][0]=x[j][0];
                A[j][1]=y[j][0];
                A[j][2]=x[j][x[j].size()-1];
                A[j][3]=y[j][y[j].size()-1];
                expand(j);
            }
        }
        fout<<"Case #"<<i+1<<":\n";
        for(int j=0;j<r;j++)
        {
            for(int k=0;k<c;k++)
            {
                fout<<ch[j][k];
            }
            fout<<endl;
        }
    }
    return 0;
}
/*
3 4
?B?A
DCE?
????
*/
