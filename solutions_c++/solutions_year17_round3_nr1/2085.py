#include <stdio.h>
#include <algorithm>
#include <math.h>


using namespace std;


bool g(pair<int,int> a, pair<int,int> b)
{
    return a.first > b.first;
}

int T, K,N;

pair<int,int> arr[1010];

double dmax(double a, double b)
{
    if( a > b)return a;
    return b;
}

double nSize(double cur, int index)
{
    double radius, height;
    radius = arr[index].first;
    height = arr[index].second;

    if(cur == 0)
    {
        cur+= (radius*radius*M_PI);
    }

    double result = (cur+=(2*M_PI*radius*height));


    return(double) result;
}

double f(int index, int stacksize, double cur)
{
    //end
    if(index == N)
    {
        if(stacksize < K)
        {
            return 0;
        }else
        {
            return cur;
        }
    }

    if(stacksize == K)return cur;

    double a = f(index+1, stacksize+1, nSize(cur,index));
    double b = f(index+1, stacksize, cur);


    return dmax(a,b);
}


int main()
{
    scanf("%d",&T);
    int q,i;
    int r,h;
    for(q = 1; q<=T; q++) //TODO: Undo later
    {
        scanf("%d %d",&N,&K);
        for(i = 0; i < N; i++)
        {
            scanf("%d %d",&r,&h);
            arr[i] = make_pair(r,h);
        }
        
        sort(arr, arr+N,g);


        printf("Case #%d: %.9lf\n",q, f(0,0,0));
    }

    return 0;
}