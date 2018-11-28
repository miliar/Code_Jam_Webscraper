#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../../output.txt");
ifstream fin("../../../input.txt");

int dp[101][101][101];

int main(void)
{
    int ttt=0;
    fin >> ttt;
    int ct = 0;
    string s;
    
    cout.precision(9);
    fout.precision(9);
    
    cout << "HELLO" <<  " " << ttt << endl;
    
    
    
    while(ttt>0)
    {
        ct++;
        ttt--;
        
        double ans=0.0;
        int i,j,k;
        
        int a,b,c;
        
        int ret = 0;
        
        int n,p;
        
        fin >> n >> p;
        
        a=b=c=0;
        
        for(i=0; i<n; i++)
        {
            fin >> j;
            if(j%p==0)
                ret++;
            else if(j%p==1)
                a++;
            else if(j%p==2)
                b++;
            else
                c++;
        }
        
        memset(dp,0,sizeof(dp));
        
        for(i=a; i>=0; i--)
        {
            for(j=b; j>=0; j--)
            {
                for(k=c; k>=0; k--)
                {
                    if(i==a && b==j && c==k)
                        continue;
                    if(i<a && dp[i+1][j][k]>dp[i][j][k])
                        dp[i][j][k]=dp[i+1][j][k];
                    if(j<b && dp[i][j+1][k]>dp[i][j][k])
                        dp[i][j][k]=dp[i][j+1][k];
                    if(k<c && dp[i][j][k+1]>dp[i][j][k])
                        dp[i][j][k]=dp[i][j][k+1];
                    if((i+2*j+3*k)%p==0)
                        dp[i][j][k]++;
                }
            }
        }
        ret+=dp[0][0][0];
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        
        cout << ret;
        fout << ret;
        
        
        
        
        
        fout << endl;
        cout << endl;
        
    }
    
    
    return 0;
}

