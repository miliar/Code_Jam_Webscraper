#include<bits/stdc++.h>
using namespace std;
char mp[30][30];
bool f[30];
int lft[30],rgt[30];
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;cin>>T;
	for(int ks=1;ks<=T;ks++)
    {
        int R,C;
        cin>>R>>C;
        memset(f,0,sizeof(f));
        memset(lft,0,sizeof(lft));
        fill_n(rgt,30,C-1);
        vector<pair<int,int> > pos;
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                cin>>mp[i][j];
                if(mp[i][j]!='?') pos.push_back({i,j});
            }
        }
        sort(pos.begin(),pos.end());
        int s=pos.size();
        for(int i=0;i<s;i++)
        {
            f[pos[i].first]=1;
            if(i>0&&pos[i].first==pos[i-1].first) rgt[i-1]=pos[i-1].second,lft[i]=rgt[i-1]+1;
        }
        for(int i=0;i<s;i++)
        {
            pair<int,int> P=pos[i];
            char cur=mp[P.first][P.second];
            for(int j=lft[i];j<=rgt[i];j++)
            {
                mp[P.first][j]=cur;
                for(int k=P.first+1;k<R;k++)
                {
                    if(f[k]) break;
                    mp[k][j]=cur;
                }
            }
        }
        for(int i=R-2;i>=0;i--)
        {
            for(int j=0;j<C;j++) if(mp[i][j]=='?') mp[i][j]=mp[i+1][j];
        }
        cout<<"Case #"<<ks<<":"<<endl;
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++) cout<<mp[i][j];
            cout<<endl;
        }
    }
	return 0;
}
