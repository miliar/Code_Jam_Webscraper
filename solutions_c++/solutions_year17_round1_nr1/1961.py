#include<bits\stdc++.h>
using namespace std;
int R,C;
char cake[30][30];
bool filled[30];
void fill_cake(int i,int refR){
    if(i<0||i>=R||filled[i])
        return;
    char ans='?';
    for(int j=0;j<C;j++)
    {
        if(cake[i][j]!='?'){
            ans=cake[i][j];
            break;
        }
    }
    if(ans=='?')
    {
        if(refR!=-1)
        {
            for(int j=0;j<C;j++)
                cake[i][j]=cake[refR][j];
            filled[i]=true;
            fill_cake(i-1,i);
            fill_cake(i+1,i);
        }
        else{
            fill_cake(i+1,-1);
            fill_cake(i-1,-1);
            fill_cake(i,-1);
        }
    }else{
        //cout<<"\n**"<<i<<endl;
        //cout<<"Ans:"<<ans<<endl;
        int j;
        for(j=0;j<C;j++)
            if(cake[i][j]!=ans)
                cake[i][j]=ans;
            else
                break;
        while(j+1<C){
            int k=j+1;
            for(j++;j<C;j++)
                if(cake[i][j]!='?')
            {
                ans=cake[i][j];
                break;
            }
            //cout<<"New Ans:"<<ans<<endl;
            for(;k<C;k++)
                if(cake[i][k]!=ans)
                    cake[i][k]=ans;
                else
                    break;
        }
        filled[i]=true;

//        for(int j=0;j<C;j++)
//            cout<<cake[i][j];
//        cout<<endl<<"**\n";
        fill_cake(i-1,i);
        fill_cake(i+1,i);
    }
}
void _main(int t){
    cin>>R>>C;
    for(int i=0;i<R;i++)
        cin>>cake[i];
    for(int i=0;i<R;i++)
        filled[i]=false;
    fill_cake(0,-1);
    for(int i=0;i<R;i++)
        cout<<cake[i]<<endl;
}
int main()
{
    int test;
    cin>>test;
    for(int t=1;t<=test;t++){
        cout<<"Case #"<<t<<":\n";
        _main(t);
    }
    return 0;
}
