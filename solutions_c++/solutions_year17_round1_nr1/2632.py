#include <bits/stdc++.h>
#define us unordered_set
#define os ordered_set
#define om ordered_map
#define um unordered_map
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define rmod 1000000
using namespace std;
char str[30][30];
int che[10000];
set<char> check;
int t,n,m;
bool gfd(int l,int r,int row)
{int i;
    for(i=l;i<=r;i++)
        if(str[row][i]=='?')
        continue;
    else break;
    if(i>r)
        return true;
    else return false;
}
void expand(char c)
{bool flag=false;
int posx,posy;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        if(str[i][j]==c)
        {posx=i;
        posy=j;
        flag=true;
        break;
        }

      if(flag) break;  }

int lb,rb;
rb=posy;
lb=posy;
for(int j=posy+1;j<m;j++)
{

if(str[posx][j]=='?')
{
 rb++;
 str[posx][j]=c;
}
else break;
}
for(int j=posy-1;j>=0;j--)
{
    if(str[posx][j]=='?')
{
 lb--;
 str[posx][j]=c;
}
else break;
}

for(int i=posx-1;i>=0;i--)
{
    if(!gfd(lb,rb,i))break;
    for(int j=lb;j<=rb;j++)
    str[i][j]=c;


}

for(int i=posx+1;i<n;i++)
{
    if(!gfd(lb,rb,i))break;
    for(int j=lb;j<=rb;j++)
    str[i][j]=c;


}






}
int main()
{
    freopen("INPUT.IN","r",stdin);
    freopen("CHOD.txt","w",stdout);

scanf("%d",&t);
int index=0;
while(t--)
{index++;
for(int i=0;i<1000;i++)che[i]=0;
    scanf("%d%d",&n,&m);
for(int i=0;i<n;i++)
    scanf("%s",str[i]);
   for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
        check.insert(str[i][j]);
for(int i=0;i<n;i++)
    for(int j=0;j<m;j++)
    if(che[str[i][j]])continue;
    else {expand(str[i][j]);
    che[str[i][j]]++;}

printf("Case #%d:\n",index);
for(int i=0;i<n;i++)
puts(str[i]);

}




return 0;}
