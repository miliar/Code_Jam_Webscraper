#include<stdio.h>
#include<math.h>
#include<malloc.h>

long powr(long base, long exp)
{
    long result = 1;
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}

long lastpow(long a)
{
    long c=0;
    while(a!=0)
    {
        a=a>>1;
        c++;
    }
    return c-1;
}


long isPower(long n)
{
    long c = powr(2,lastpow(n+1));
    if(c==n+1)
        return 1;
    return 0;
}


long count(long *a,long v,long n)
{
    long i,c=0;
    for(i=0; i<n; i++)
    {
        if(a[i]==v)
            c++;
    }
    return c;
}

void f1(long n,long k,long cae)
{
    long a1,m,i,c1,c2,j,res,h1,h = lastpow(n)+1;
    long **a,**r;
    a = (long**)malloc(h*sizeof(long*));
    for(i=0; i<h; i++)
    {
        j=powr(2,i);
        a[i] = (long*)malloc(sizeof(long)*j);
    }

    a[0][0]=n;
    for(i=1; i<h; i++)
    {
        m=powr(2,i);
        for(j=0; j<m; j+=2)
        {
            if(a[i-1][j/2]%2!=0)
            {
                a[i][j]=(a[i-1][j/2]/2);
                a[i][j+1]=(a[i-1][j/2]/2);
            }
            else
            {
                a[i][j]=((a[i-1][j/2]/2) - 1);
                a[i][j+1]=(a[i-1][j/2]/2);
            }
        }
    }
    h1= lastpow(k);
    i=k-powr(2,h1);
    res = a[h1][0];
    c1 = count(a[h1],res,powr(2,h1)+1);
    c2 = count(a[h1],res+1,powr(2,h1)+1);

    if(i<c2)
        res = res+1;
    if(res==0)
        printf("Case #%ld: 0 0\n",cae+1);
    else if(res%2==0)
        printf("Case #%ld: %ld %ld\n",cae+1,(res/2),(res/2)-1);
    else
        printf("Case #%ld: %ld %ld\n",cae+1,(res/2),res/2);
}

int main()
{
    long t,a1,n,k,j,r;
    scanf("%ld",&t);
    for(a1=0; a1<t; a1++)
    {
        scanf("%ld %ld",&n,&k);
        if(isPower(n))
        {
            j = lastpow(k);
            r = (n)/(powr(2,j+1));
            printf("Case #%ld: %ld %ld\n",a1+1,r,r);
        }
        else if(n>k)
            f1(n,k,a1);
        else
            printf("Case #%ld: 0 0\n",a1+1);
    }
    return 0;
}
