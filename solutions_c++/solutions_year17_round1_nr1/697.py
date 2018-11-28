#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <fstream>
#include <map>
using namespace std;
const int N = 2120;

struct Node
{
    int x;
    int y;
    int len;
    Node(int a=0, int b=0, int c=0)
    {
        x = a;
        y = b;
        len = c;
    }
    friend bool operator < (const Node& A, const Node& B)
    {
        if(A.len<B.len) return true;
        if(A.len == B.len && A.x > B.x) return true;
        return false;
    }
};




char str[30][30];
int main()
{

    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int test;
    scanf("%d", &test);

    for(int t=1; t<=test; t++)
    {
        int r,c;
        scanf("%d%d",&r,&c);
        for(int i=0; i<r; i++)
        {
            scanf("%s",str[i]);
        }
        for(int i=0; i<r; i++)
        {
            for(int j=0; j<c; j++)
            {
                if(str[i][j]!='?')
                {
                    for(int k=j+1; k<c; k++)
                    {
                        if(str[i][k]=='?')
                        {
                            str[i][k]=str[i][j];
                        }

                        else break;
                    }
                    for(int k=j-1; k>=0; k--)
                    {
                        if(str[i][k]=='?')
                        {
                            str[i][k]=str[i][j];
                        }
                        else break;
                    }
                }
            }
        }
        for(int i=0; i<r; i++)
        {
            if(str[i][0]!='?')
            {
                for(int k=i-1; k>=0; k--)
                {
                    if(str[k][0]=='?')
                    {
                        for(int j=0; j<c; j++)
                        {
                            str[k][j]=str[i][j];
                        }
                    }
                    else break;
                }
                for(int k=i+1; k<r; k++)
                {
                    if(str[k][0]=='?')
                    {
                        for(int j=0; j<c; j++)
                        {
                            str[k][j]=str[i][j];
                        }
                    }
                    else break;
                }
            }
        }
        printf("Case #%d:\n",t);
        for(int i=0; i<r; i++)
        {
            printf("%s\n",str[i]);
        }
    }
    return 0;
}
