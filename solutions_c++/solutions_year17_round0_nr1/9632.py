#include<bits/stdc++.h>
using namespace std;
#define MAX 1005

int BIT[MAX];

void update(int pos, int v)
{
    for(; pos<MAX; pos+=pos&(-pos))
        BIT[pos]+=v;
}

void update(int i, int j,int v)
{
    update(i,v);
    update(j+1,-v);
}

int query(int pos)
{
    int sum=0;
    for(; pos > 0; pos -= pos&(-pos))
        sum += BIT[pos];
    return sum;
}

int main()
{
    int n,d;
    string pancake;
    scanf("%d",&n);
    for(int k=1; k<=n; k++)
    {
        cin >> pancake >> d;

        for(int i=0;i<MAX;i++)
            BIT[i]=0;

        int answer=0;
        for(int i=0; i+d<=pancake.size(); i++)
        {
            if((query(i+1)%2==1 && pancake[i]=='+') || (query(i+1)%2==0 && pancake[i]=='-'))
            {
                answer++;
                update(i+1,i+d,1);
            }
        }

        for(int i=0; i<pancake.size(); i++)
        {
            if(query(i+1)%2==1)
            {
                if(pancake[i]=='-')
                    pancake[i]='+';
                else
                    pancake[i]='-';
            }
        }

        bool perdeuplayboy=false;
        for(int i=0; i<pancake.size(); i++)
            if(pancake[i]=='-')
                perdeuplayboy=true;
        printf("Case #%d: ",k);
        if(!perdeuplayboy)
            printf("%d\n",answer);
        else
            printf("IMPOSSIBLE\n");
    }
    return 0;
}
