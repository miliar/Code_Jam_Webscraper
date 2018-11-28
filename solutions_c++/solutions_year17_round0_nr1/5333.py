#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string.h>
#include<math.h>
#include<queue>
using namespace std;
int pancake[1025];
main()
{
    int binary[100];
    for(int i=0;i<=100;i++)
    {
        binary[i]=pow(2.0,i);
    }
    FILE* FileRead = fopen("A-small-attempt0.in", "r");
    FILE* FileWrite = fopen("out.txt", "w");
    int n;
    fscanf(FileRead,"%d",&n);
    for(int i=1;i<=n;i++)
    {
        queue<int> q,q_ct;
        char input[1000];
        int K;
        fscanf(FileRead, "%s", input);
        fscanf(FileRead, "%d", &K);
        int m=strlen(input);
        int dest=0;
        int start=0;
        for(int j=0;j<m;j++)
        {
            dest+=pow(2.0,j);
            if(input[j]=='+')start+=pow(2.0,j);
        }
        if(dest==start)fprintf(FileWrite, "Case #%d: 0\n", i);
        else
        {
            //cout<<input<<endl;
            for(int j=0;j<=1024;j++)
            {
                pancake[j]=0;
            }
            q.push(start);
            q_ct.push(0);
            //cout<<"test case"<<i<<endl;
            while(!q.empty())
            {
                int curr_node=q.front();
                int ct=q_ct.front();
                //cout<<curr_node<<' '<<ct<<endl;
                q.pop();q_ct.pop();
                int next_node;
                for(int j=K-1;j<m;j++)
                {
                    int Xor=0;
                    for(int k=0;k<K;k++)Xor+=pow(2.0,j-k);
                    next_node=curr_node^Xor;
                    //cout<<next_node<<' ';
                    if(pancake[next_node]==0||pancake[next_node]>ct+1)
                    {
                        pancake[next_node]=ct+1;
                        q.push(next_node);
                        q_ct.push(ct+1);
                    }
                }
                //cout<<endl;
                if(pancake[dest]!=0)
                {
                    fprintf(FileWrite, "Case #%d: %d\n", i, pancake[dest]);
                    break;
                }
            }
            if(pancake[dest]==0)
                {
                    fprintf(FileWrite, "Case #%d: IMPOSSIBLE\n", i, pancake[dest]);
                }
        }
    }
}
