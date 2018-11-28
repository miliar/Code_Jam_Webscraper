#include<bits/stdc++.h>
using namespace std;


int r,c;
char matrix[50][50];
int visit[50][50];

bool check(int i, int j)
{
    if(i>=0 && i<r && j>=0 && j <c) return true;
    return false;
}

void dfs(int i,int j,char ch)
{
   // cout << i <<" =  " << j <<" = " << ch <<endl;
   if(visit[i][j] == 1) return;
    if(matrix[i][j] == '?')
    {
        matrix[i][j] = ch;
        visit[i][j] = 1;
        bool ok = check(i,j-1);
        if(ok==true && matrix[i][j-1] == '?')
        {
            dfs(i,j-1,ch);
        }
        ok = check(i,j+1);
        if(ok==true && matrix[i][j+1] == '?')
        {
            dfs(i,j+1,ch);
        }
    }
    else if(matrix[i][j] != '?')
    {
        if(matrix[i][j] == ch)
        {
            visit[i][j] = 1;
            bool ok = check(i,j-1);
            if(ok==true && matrix[i][j-1] == '?')
            {
                dfs(i,j-1,ch);
            }
            ok = check(i,j+1);
            if(ok==true && matrix[i][j+1] == '?')
            {
                dfs(i,j+1,ch);
            }
        }
    }

}


int main()
{
    int T,t;
    freopen("A-large (1).in","r",stdin);
    freopen("A-large (1).out","w",stdout);
    scanf("%d",&T);
    for(t = 1; t <= T; t++)
    {

        scanf("%d %d",&r,&c);


        for(int i=0; i<r; i++)
        {
            scanf("%s",matrix[i]);

        }
        memset(visit,0,sizeof(visit));

        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(matrix[i][j] != '?')
                {
                    //printf("pass \n");
                    dfs(i,j,matrix[i][j]);
                   // cout<<matrix[i]<<endl;

                }
            }
        }
       /* for(int i=0;i<r;i++)
        {
            printf("%s\n",matrix[i]);
        }*/
        for(int i=0;i<r;i++)
        {
            bool all=false;
            for(int j=0;j<c;j++)
            {
                if(matrix[i][j] == '?') continue;
                else all = true;
            }
            if(!all)
            {
                //cout<<" i = " << i << endl;
                bool hoi=false;
                int save = -1;
                for(int j=i;j<r;j++)
                {
                    if(matrix[j][0] != '?')
                    {
                        hoi = true;
                        save = j;
                        break;
                    }
                }
                if(hoi)
                {
                   for(int j=0;j<c;j++)
                   {
                       if(matrix[i][j] == '?') matrix[i][j] = matrix[save][j];
                   }
                }
                else
                {
                    bool last = false;
                    //cout<<"ase " << endl;
                    for(int j=i; j>=0;j--)
                    {
                        if(matrix[j][0] != '?')
                        {
                            hoi = true;
                            save = j;
                            break;
                        }
                    }
                    if(hoi)

                    {
                        //cout<<"mu "<<save << endl;
                        //for(int k=0;k<r;k++) cout<<matrix[k]<<endl;
                        for(int j=0;j<c;j++)
                        {
                           if(matrix[i][j] == '?') matrix[i][j] = matrix[save][j];
                        }
                    }
                }
            }
        }
        printf("Case #%d:\n",t);
        for(int i=0;i<r;i++)
        {

            printf("%s\n",matrix[i]);
        }

    }

    return 0;
}
