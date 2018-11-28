#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <cassert>
#define pb push_back
#define mk make_pair
#define F first
#define S second
#define pi 3.1415926535

#define MOD (1000000007)
using namespace std;
int p,b;
int cs[2][2];
vector <int> tmp[2];
int done[1000][2];
int pairs()
{
    sort(tmp[0].begin(),tmp[0].end());
    sort(tmp[1].begin(),tmp[1].end());
    memset(done,0,sizeof done);
    int i=0,j=0,pr=0;;
    while(i<tmp[0].size() && j<tmp[1].size())
    {
        if(tmp[0][i]<tmp[1][j])
        {  pr++; done[0][i]=1; done[1][j]=1;i++;j++;}
        else
            j++;
    }
    i=0;j=0;
    while(i<tmp[0].size() && j<tmp[1].size())
    {
        if(done[1][j]==1)
        { j++; continue;}
        if(done[0][i]==1)
        {
            i++; continue;
        }
        if(tmp[1][j]<tmp[0][i])
        { pr++; done[0][i]=1; done[0][j]=1; i++;j++;}
        else
            i++;
    }
    cout<<cs[0][0]<<" "<<cs[1][0]<<endl;
    for(int i=0;i<tmp[0].size();i++)
        printf("%d ",tmp[0][i]);
    printf("\n");
    for(int i=0;i<tmp[1].size();i++)
        printf("%d ",tmp[1][i]);
    printf("\n");
    return pr;
}
int main(void)
{
    ifstream infile;
    infile.open("in.txt");
    
    ofstream outfile;
    outfile.open("out.txt");
    int t,n,c,m,y,z,cc=1;
    infile>>t;
    int pos;
    while(t--)
    {
        infile>>n>>c>>m;
        printf("%d %d %d\n",n,c,m);
        assert(c==2);
        tmp[0].clear();
        tmp[1].clear();
        memset(cs,0,sizeof cs);
        for(int i=0;i<m;i++)
        { infile>>p>>b;
            pos=(p==1?0:1);
            cs[b-1][pos]++;
            if(p!=1)
            tmp[b-1].pb(p);
        }
        if(n==1)
          {y=m;z=0;}
        else
        {
            y=cs[0][0]+cs[1][0];
            z=0;
            cs[1][1]-=cs[0][0];
            cs[0][1]-=cs[1][0];
            cs[1][1]=max(cs[1][1],0);
            cs[0][1]=max(cs[0][1],0);
            if(cs[1][1]==0)
                y+=cs[0][1];
            else if(cs[0][1]==0)
                y+=cs[1][1];
            else//none are zero
            {
                int pr=pairs();
                if(pr>=cs[0][1] || pr>=cs[1][1])
                    y+=max(cs[0][1],cs[1][1]);// done
                else
                {
                    z=min(cs[0][1],cs[1][1])-pr;
                    y+=max(cs[0][1],cs[1][1]);
                }
            }
        }
        printf("Case #%d: %d %d\n",cc,y,z);
        outfile<<"Case #"<<cc++<<": "<<y<<" "<<z<<endl;
        continue;
       
    }
    outfile.close();
    infile.close();
    return 0;
}
