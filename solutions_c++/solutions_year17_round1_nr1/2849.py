#include<stdlib.h>
#include<iostream>

using namespace std;

int main()
{
    int t,i,j,k,curx,cury,ll,ul,leftl,rightl;
    cin>>t;

    for(i=1;i<=t;i++)
    {
        int r,c;
        cin>>r>>c;
        char mat[r][c];
        int let[26][2]={0};
        bool flg[26]={false};
        for(j=0;j<r;j++)
        {
            for(k=0;k<c;k++)
            {
                cin>>mat[j][k];
                if(mat[j][k]!='?')
                {
                    let[mat[j][k]-'A'][0]=j;
                    let[mat[j][k]-'A'][1]=k;
                    flg[mat[j][k]-'A']=true;
                }
            }
        }

        for(j=0;j<26;j++)
        {
            if(flg[j])
            {
                curx=let[j][0];
                cury=let[j][1];
                //cout<<"curx : "<<curx<<" cury : "<<cury<<" for "<<(char)(j+'A')<<endl;
                for(k=curx;k>=0;k--)
                {
                    if(mat[k][cury]!=j+'A' && mat[k][cury]!='?')
                        break;
                }
                ul=k+1;
                for(k=curx;k<r;k++)
                {
                    if(mat[k][cury]!=j+'A' && mat[k][cury]!='?')
                        break;
                }
                ll=k-1;
                for(k=cury;k>=0;k--)
                {
                    if(mat[curx][k]!=j+'A' && mat[curx][k]!='?')
                        break;
                }
                leftl=k+1;
                for(k=cury;k<c;k++)
                {
                    if(mat[curx][k]!=j+'A' && mat[curx][k]!='?')
                        break;
                }
                rightl=k-1;

                //cout<<"ul : "<<ul<<" ll : "<<ll<<" leftl : "<<leftl<<" rightl : "<<rightl<<" for "<<(char)(j+'A')<<endl;
                if(ll-ul>rightl-leftl)
                {
                    for(k=ul;k<=ll;k++)
                        mat[k][cury]=j+'A';
                }
                else
                {
                    for(k=leftl;k<=rightl;k++)
                        mat[curx][k]=j+'A';
                }
            }
        }

        cout<<"Case #"<<i<<":"<<endl;
        for(j=0;j<r;j++)
        {
            for(k=0;k<c;k++)
                cout<<mat[j][k];
            cout<<endl;
        }
    }
}
