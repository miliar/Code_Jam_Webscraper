#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <stdio.h>
#include <fstream>
using namespace std;
int bfs(string S, int K)
{
    std::map<string,int> pancake;
    queue< pair<string,int> > qup;
    qup.push(make_pair(S,0));
    pancake.insert( make_pair (S, 0) );
    int N = S.length();
    while (!qup.empty())
    {
         string tmpS = qup.front().first;
         int step = qup.front().second;
         string proS = "";
         int negative = 0;
         for (int i = 0; i < N; i ++)
         {
             if (tmpS[i] == '-') negative++;
         }
         if (negative == 0) return step;
         qup.pop();
         negative = 0;
         for (int i=0; i < K; i ++)
         {
             if (tmpS[i] == '-') negative++;
         }
         if (negative)
         {
             string NewS = tmpS;
             for (int i=0; i < K; i++)
             {
                 if (NewS[i] == '-') NewS[i] = '+';
                 else NewS[i] = '-';
             }
             if (pancake.find( NewS ) == pancake.end())
             {
                 pancake.insert( make_pair (NewS, step + 1) );
                 qup.push( make_pair (NewS, step + 1) );
             }
         }
         for (int i = K; i < N; i++ )
         {
             if (tmpS[i-K] == '-') negative--;
             if (tmpS[i] == '-') negative++;
             if (negative)
             {
                 string NewS = tmpS;
                 for (int j=i-K + 1; j < i+1; j++)
                 {
                     if (NewS[j] == '-') NewS[j] = '+';
                     else NewS[j] = '-';
                 }
                 if (pancake.find( NewS ) == pancake.end())
                 {
                     pancake.insert( make_pair (NewS, step + 1) );
                     qup.push( make_pair (NewS, step + 1) );
                 }
             }
         }
    }
    return -1;
}
int main(void)
{
    string S;
    int k;
    int test;
    std::ifstream infile("A-small-attempt2.in");
    infile >> test;
    FILE * pFile;
    pFile = fopen ("output.txt","w");
    for (int i = 0; i < test; i++)
    {
        infile >> S >> k;
        int res = bfs(S,k);
        if (res == -1 ) fprintf (pFile, "Case #%d: IMPOSSIBLE\n",i+1);
        else fprintf (pFile, "Case #%d: %d\n",i+1,res);
    }
    fclose (pFile);
}
