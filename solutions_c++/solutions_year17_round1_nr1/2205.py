#include<bits/stdc++.h>
using namespace std;
char s[26][26];
int h[27];
vector<char>v[28];
int main()
{
    int t,e;
  //  ofstream outFile;

//outFile.open("output23.txt");
    scanf("%d",&t);
    for(e=1;e<=t;e++)
    {
        int r,c;
        scanf("%d%d",&r,&c);
        int i,j;
        for(i=1;i<=r;i++)
        {
            scanf("%s",s[i]);
        }
        for(i=1;i<=r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(s[i][j]=='?')
                    continue;
                    v[i].push_back(s[i][j]);
            }
        }
      //  printf("dd");
       // for(i=1;i<=r;i++)
        //rintf("ff%d\n",v[i].size());
        int p=0,z;
char d;
        for(i=1;i<=r;i++)
        {
            if(v[i].size()!=0)
            d=v[i][p++];
            for(j=0;j<c;j++)
            {
               // printf("j=%d\n",j);
                if(i==1&&v[i].size()==0)
                {
                   break;
                }
                if(i!=1&&v[i].size()==0&&h[i-1]==1)
                {
                    for(z=0;z<c;z++)
                    {
                        s[i][z]=s[i-1][z];
                    }
                    h[i]=1;
                    break;
                }
                if(i!=1&&v[i].size()==0&&h[i-1]==0)
                    break;
               if(s[i][j]=='?')
               {
                h[i]=1;
                s[i][j]=d;
               }
               else
               {
                d=s[i][j];
                h[i]=1;
               }
               //printf("%d  %d  %c\n",i,j,s[i][j]);
            }
            p=0;
        }
     //   for(i=1;i<=r;i++)
       //     printf("FR%d\n",h[i]);
        for(i=(r-1);i>=1;i--)
        {
            if(h[i]!=1)
            {
              for(z=0;z<c;z++)
                    s[i][z]=s[i+1][z];
            }
        h[i]=1;
        }
         printf("Case #%d:\n",e);
        //outFile<<"Case #"<<e<<":\n";
         for(i=1;i<=r;i++)
        {
            printf("%s\n",s[i]);
          //  outFile<<s[i]<<"\n";
        }

for(i=0;i<=26;i++)
    v[i].clear();
memset(h,0,sizeof(h));
    }
    return(0);
}
