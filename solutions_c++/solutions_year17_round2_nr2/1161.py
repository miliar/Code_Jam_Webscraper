#include <iostream>
#include <queue>
using namespace std;

int n;
int col[6];
struct Color
{
    char color;
    int count;
};

int main()
{
    int tc,tci=0;
    cin>>tc;
    while(tc--)
    {
        //cout<<tc<<endl;
        tci++;
        int i;
        cin>>n;
        for(i=0;i<6;i++)
        {
            cin>>col[i];

        }
        cout<<"Case #"<<tci<<": ";
        if(col[0]>col[2]+col[4]||col[2]>col[0]+col[4]||col[4]>col[0]+col[2])
        {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
        char last=0;
        int first;
        char tre[3]={'R','Y','B'};
        while(1)
        {
            //cout<<col[0]<<" "<<col[2]<<" "<<col[4]<<endl;
            if(col[0]==0&&col[2]==0&&col[4]==0)break;
            if(last==0)
            {
                int ma=max(col[0],max(col[2],col[4]));
                for(i=0;i<3;i++)if(col[2*i]==ma)
                {
                    cout<<tre[i];last=tre[i];first=2*i;col[2*i]--;break;
                }
                continue;
            }
            if(last=='R')
            {
                if(col[2]>col[4]||col[2]==col[4]&&first==2)
                {
                    cout<<tre[1];
                    last=tre[1];
                    col[2]--;
                }
                else
                {
                    cout<<tre[2];
                    last=tre[2];
                    col[4]--;
                }
                continue;
            }
            if(last=='Y')
            {
                if(col[0]>col[4]||col[0]==col[4]&&first==0)
                {
                    cout<<tre[0];
                    last=tre[0];
                    col[0]--;
                }
                else
                {
                    cout<<tre[2];
                    last=tre[2];
                    col[4]--;
                }
                continue;
            }
            if(last=='B')
            {
                if(col[2]>col[0]||col[2]==col[0]&&first==2)
                {
                    cout<<tre[1];
                    last=tre[1];
                    col[2]--;
                }
                else
                {
                    cout<<tre[0];
                    last=tre[0];
                    col[0]--;
                }
                continue;
            }
        }
        cout<<endl;
    }
    return 0;
}
