#include <bits/stdc++.h>

using namespace std;
int dp[102][102][102][102];
struct tt{
   int h1,a1,h2,a2;
   tt(){}
   tt(int a,int b,int c,int d):h1(a),a1(b),h2(c),a2(d){}
};
void update(int a,int b,int c,int d,int pa,int pb,int pc,int pd,queue<tt> & q)
{
   a-=d;
   if(a<=0||pa<=0)return;
   if(dp[a][b][c][d]>dp[pa][pb][pc][pd]+1)
   {
      dp[a][b][c][d]=dp[pa][pb][pc][pd]+1;
      q.push(tt(a,b,c,d));
   }
}
int main()
{
	ios_base::sync_with_stdio(0);
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t;
	cin>>t;
	for(int o=1;o<=t;o++)
	{
      int h1,a1,h2,a2,b,d;
      cin>>h1>>a1>>h2>>a2>>b>>d;
      for(int i=0;i<102;i++)
      {
         for(int j=0;j<102;j++)
         {
            for(int k=0;k<102;k++)
            {
               for(int q=0;q<102;q++)
               {
                  dp[i][j][k][q]=1e9;
               }
            }
         }
      }
      dp[h1][a1][h2][a2]=0;
      queue<tt> q;
      q.push(tt(h1,a1,h2,a2));
      int ans=-1;
      while(!q.empty())
      {
         tt tmp=q.front();
         q.pop();
         if(tmp.a1>=tmp.h2)
         {
            ans=dp[tmp.h1][tmp.a1][tmp.h2][tmp.a2]+1;
            break;
         }
         update(h1,tmp.a1,tmp.h2,tmp.a2,                            tmp.h1,tmp.a1,tmp.h2,tmp.a2,q);///heal
         update(tmp.h1,tmp.a1,tmp.h2,max(tmp.a2-d,0),      tmp.h1,tmp.a1,tmp.h2,tmp.a2,q);///debuff
         update(tmp.h1,min(tmp.a1+b,100),tmp.h2,tmp.a2,             tmp.h1,tmp.a1,tmp.h2,tmp.a2,q);///buff
         update(tmp.h1,tmp.a1,tmp.h2-tmp.a1,tmp.a2,                     tmp.h1,tmp.a1,tmp.h2,tmp.a2,q);///attack
      }
      if(ans==-1)
      {
        cout<<"Case #"<<o<<": IMPOSSIBLE\n";
      }
      else
      {
         cout<<"Case #"<<o<<": "<<ans<<'\n';
      }

	}

}
