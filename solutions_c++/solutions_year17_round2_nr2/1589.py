#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

FILE *in = fopen("input.txt","r");    
FILE *out= fopen("output.txt","w");


struct uni
{
int num;
char col;

};

uni u[3];

int primecolor (int r, int y, int b)
{
int i=0;


if ((r==y)&&(r==b))
    {

    
    for (i=0;i<r;i++)
        {
        fprintf(out, "%c%c%c", u[0].col, u[1].col, u[2].col);
        }
    return 0;
    } 


if ((r>=y)&&(y>=b))
    {
    fprintf(out, "%c%c", u[0].col, u[1].col);
    primecolor(r-1,y-1,b);
    return 0;

    }
if ((r>=b)&&(b>=y))
    {
    fprintf(out, "%c%c", u[0].col, u[2].col);
    primecolor(r-1,y,b-1);
    return 0;
    }
/*if ((y>=r)&&(r>=b))
    {
    fprintf(out, "yr");
    primecolor(r-1,y-1,b);
    return 0;
    }
if ((y>=b)&&(b>=r))
    {
    fprintf(out, "yb");
    primecolor(r,y-1,b-1);
    return 0;
    }
if ((b>=r)&&(r>=y))
    {
    fprintf(out, "br");
    primecolor(r-1,y,b-1);
    return 0;
    }
if ((b>=y)&&(y>=r))
    {
    fprintf(out, "by");
    primecolor(r,y-1,b-1);
    return 0;
    }*/
    return 0;




}



int main ()
{
int t,n,i,j,r,o,y,g,b,v,z;


fscanf(in, "%d", &t);

for (i=0;i<t; i++)
    {
    fscanf(in, "%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
    if ((r+y<b)||(r+b<y)||(y+b<r))
        {
        fprintf(out, "Case #%d: IMPOSSIBLE\n", i+1);
        }
    else
        {
        if ((r>=b)&&(r>=y))
            {
            u[0].col='r';
            u[0].num=r;
            if (b>=y)
                {
                u[1].col='b';
                u[1].num=b;
                u[2].col='y';
                u[2].num=y;
                }
                else
                {
                u[1].col='y';
                u[1].num=y;
                u[2].col='b';
                u[2].num=b;
                }
            }
        if ((b>=r)&&(b>=y))
            {
            u[0].col='b';
            u[0].num=b;
            if (r>=y)
                {
                u[1].col='r';
                u[1].num=r;
                u[2].col='y';
                u[2].num=y;
                }
                else
                {
                u[1].col='y';
                u[1].num=y;
                u[2].col='r';
                u[2].num=r;
                }
            }
        if ((y>=b)&&(y>=r))
            {
            u[0].col='y';
            u[0].num=y;
            if (b>=r)
                {
                u[1].col='b';
                u[1].num=b;
                u[2].col='r';
                u[2].num=r;
                }
                else
                {
                u[1].col='r';
                u[1].num=r;
                u[2].col='b';
                u[2].num=b;
                }
            }
            
            
        fprintf(out, "Case #%d: ", i+1);
        z=primecolor(u[0].num,u[1].num,u[2].num);
        fprintf(out,"\n");
        }


    }


return 0;    
    
}
