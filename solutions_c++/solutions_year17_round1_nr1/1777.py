#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<pair<int,int> > vii;
typedef vector<vii> vvii;
typedef long long ll;
const int INF = 200000000;
const int MAX = 10005;

int main()
{
    int t,r,c,con=1,ini,fin;
    bool pinta,vis[27];
    char m[26][26];
    cin>>t;
    while(t--)
    {
        cin>>r>>c;
        for(int i=0;i<r;i++)
            for(int e=0;e<c;e++)
                cin>>m[i][e];
        cout<<"Case #"<<con++<<":\n";
  
        memset(vis,false,sizeof vis);
        for(int i=0;i<r;i++)
        {
            for(int e=0;e<c;e++)
                if(m[i][e]!='?' && !vis[m[i][e]-'A'])
                {
                    vis[m[i][e]-'A']=true;
                    ini=e;
                    for(int k=e-1;k>=0;k--)
                    {
                        if(k==0 && m[i][0]=='?')
                        {
                            ini=0;
                            m[i][0]=m[i][e];
                            break;
                        }
                        if(m[i][k]!='?')
                        {
                            ini=k+1;
                            break;
                        }
                        m[i][k]=m[i][e];
                    }
                    fin=e;    
                    for(int k=e+1;k<c;k++)
                    {
                        if(k==c-1 && m[i][c-1]=='?')
                        {
                            fin=c-1;
                            m[i][k]=m[i][e];
                            break;
                        }
                        if(m[i][k]!='?')
                        {
                            fin=k-1;
                            break;
                        }
                        m[i][k]=m[i][e];
                    }
                    for(int k=i-1;k>=0;k--)
                    {
                        pinta=true;
                        for(int z=ini;z<=fin;z++)
                        {
                            if(m[k][z]!='?')
                            {
                                pinta=false;
                                break;
                            }
                        }
                        if(!pinta)
                            break;
                        for(int z=ini;z<=fin;z++)
                            m[k][z]=m[i][e];
                    }
                    for(int k=i+1;k<r;k++)
                    {
                        pinta=true;
                        for(int z=ini;z<=fin;z++)
                        {
                            if(m[k][z]!='?')
                            {
                                pinta=false;
                                break;
                            }
                        }
                        if(!pinta)
                            break;
                        for(int z=ini;z<=fin;z++)
                            m[k][z]=m[i][e];
                    }
                    //cout<<m[i][e]<<" "<<ini<<" "<<fin<<endl;
                }
        }
        for(int i=0;i<r;i++)
        {
            for(int e=0;e<c;e++)
                cout<<m[i][e];
            cout<<"\n";
        }
            
    }
    return 0;
}