#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define sf_d(var) scanf("%d",&var)
#define sf_2d(var1,var2) scanf("%d %d",&var1,&var2)
#define vi vector<int>
#define vvi vector< vector<int> >
#define pb push_back
#define v_iter vector<int>::iterator
#define v_riter vector<int>::reverse_iterator
#define fr_z(start,end) for(int z=start;z<end;z++)
#define fr_o(start,end) for(int o=start;o<end;o++)
#define w while
#define mod 1000000007
#define srt(cont) sort(cont.begin(),cont.end())
#define all(m) m.begin(),m.end()
#define mp make_pair
#define fa_io std::ios::sync_with_stdio(false)

int main()
{
    fa_io;
    cin.tie(NULL);
    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int t,n,r,c;
    cin>>t;
    for(int q=1;q<=t;q++)
    {
        cout<<"Case #"<<q<<":\n";
        cin>>r>>c;
        char ch;
        char grid[r][c];
        fr_z(0,r)
            fr_o(0,c)
            {
                cin>>ch;
                grid[z][o]=ch;
            }
        vi v;
        fr_z(0,r)
        {
            int a=0,b,h;
            bool j=true,k;
            while(a<=c-1)
            {
                k=false;
                while(grid[z][a]=='?' && a<=c-1)
                {
                    k=true;
                    a++;
                }
                b=a-1;h=a+1;
                while(grid[z][b]=='?' && b>=0 && a<=c-1)
                {
                    grid[z][b]=grid[z][a];
                    b--;
                    j=false;
                }
                while(grid[z][h]=='?' && h<=c-1 && a<=c-1)
                {
                    grid[z][h]=grid[z][a];
                    h++;
                    j=false;
                }
                if(k)
                    a=h;
                else
                    a++;
            }
            if(j)
                v.pb(z);
        }
        /*for(auto it:v)
            cout<<it<<'\n';*/
            for(int a=0;a<r;a++)
            {
                //cout<<a<<'\n';
                while(grid[a][0]=='?')
                    a++;
                int b=a-1;
                while(b>=0 && a<=r-1 && grid[b][0]=='?')
                {
                    fr_z(0,c)
                        grid[b][z]=grid[a][z];
                    b--;
                }
            }
        if(grid[r-1][0]=='?')
        {
            int a=r-1,b;
            while(grid[a][0]=='?')
                a--;
            b=a+1;
            while(b<=r-1 && grid[b][0]=='?')
            {
                fr_z(0,c)
                    grid[b][z]=grid[a][z];
                b++;
            }
        }
        fr_z(0,r)
        {
            fr_o(0,c)
                cout<<grid[z][o];
            cout<<'\n';
        }
    }

    return 0;
}
