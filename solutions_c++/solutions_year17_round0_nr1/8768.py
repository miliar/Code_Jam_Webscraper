#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
using namespace std;

int convert(char *S,int N)
{
    int sum=0;
    for (int i=0;i<N;i++){
        int d=(S[i]=='+')?1:0;
        sum+=d*(1<<i);
    }
    return sum;
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A_output_small.txt","w",stdout);
    int T;
    char S[110];
    int K;
    int step[1<<11];
    list<int> queue;
    scanf("%d",&T);
    for (int index=1;index<=T;index++){
        scanf("%s %d",S,&K);
        //printf("S=%s K=%d\n",S,K);
        int N=strlen(S);
        memset(step,0xff,sizeof(step));
        queue.clear();
        int tmp=convert(S,N);
        int end=(1<<N)-1;
        if (tmp==end){
            printf("Case #%d: 0\n",index);
            continue;
        }
        //printf("tmp=%d end=%d\n",tmp,end);
        step[tmp]=0;
        queue.push_back(tmp);
        while (!queue.empty()){
            int u=queue.front();
            queue.pop_front();
            for (int i=0;i<N;i++){
                int j=i+K-1;
                if (j>=N) break;
                int v=u;
                for (int p=i;p<=j;p++){
                    v=v^(1<<p);
                }
                if (step[v]<0 || step[v]>step[u]+1){
                    queue.push_back(v);
                    step[v]=step[u]+1;
                }
            }
        }
        if (step[end]<0){
            printf("Case #%d: IMPOSSIBLE\n",index);
        }else{
            printf("Case #%d: %d\n",index,step[end]);
        }
    }
    return 0;
}
