#include <iostream>
using namespace std;
const int MAXN=50;
char cake[MAXN][MAXN];
int main()
{
    freopen("/Users/nsbhasin/Desktop/Kickstart2017/AlphabetCake/A-large.in","r",stdin);
    freopen("/Users/nsbhasin/Desktop/Kickstart2017/AlphabetCake/output3.txt","w",stdout);
    int t,test=1;
    int R,C;
    cin>>t;
    while(t--)
    {
        cin>>R>>C;
        for(int i=0;i<R;i++)
            cin>>cake[i];
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                int row=i;
                if(cake[i][j]!='?')
                {
                    while(--row >= 0 && cake[row][j]=='?')
                        cake[row][j]=cake[i][j];
                    row=i;
                    while(++row<R && cake[row][j]=='?')
                        cake[row][j]=cake[i][j];
                }
            }
        }
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                int col=j;
                if(cake[i][j]!='?')
                {
                    while(--col >= 0 && cake[i][col]=='?')
                        cake[i][col]=cake[i][j];
                    col=j;
                    while(++col < C && cake[i][col]=='?')
                        cake[i][col]=cake[i][j];
                }
            }
        }        cout<<"Case #"<<test++<<": "<<endl;
        for(int i=0;i<R;i++)
            cout<<cake[i]<<endl;
    }
    return 0;
}
