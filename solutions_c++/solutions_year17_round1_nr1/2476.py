#include<iostream>
#include<cstdio>

using namespace std;
char s[27][27];
int r, c;
void dorow(int i)
{
    if(s[i][0]=='?')
    {
        int k=1;
        char ans ='?';
       while(k<c)
       {
           if(s[i][k]!= '?')
           {
               ans =s[i][k];
               break;
           }
           k++;
       }
       if(ans == '?')
        return;
        else
            s[i][0]=ans;
    }

    for(int j=1;j<c;j++)
    {
        if(s[i][j]=='?')
            s[i][j]=s[i][j-1];
    }

}
 void dorowcopy(int i)
{
    for(int j=0;j<c;j++)
        {
            s[i][j]=s[i-1][j];
        }
}

int main()
{
    freopen("C:\\Users\\apachoud.ORADEV\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\apachoud.ORADEV\\Desktop\\output.txt","w",stdout);
    int t;
    cin>>t;
    int i,j;
    int te=1;
    while(te<=t)
    {



    cin>>r>>c;
    //cout<<r<<c<<endl;

    for(i=0;i<r;i++)
    {
        cin>>s[i];
        //printf("%s\n",s[i]);
    }
    //cout<<"started";
    for(i=0;i<r;i++)
    {
        dorow(i);
    }
    if(s[0][0]=='?')
    {
        int row=1;
        while(row<r)
        {
            if(s[row][0]!='?')
            {
                break;
            }
            row++;
        }
        for(i=0;i<c;i++)
        {
            s[0][i]=s[row][i];
        }
    }
    for(i=1;i<r;i++)
    {
        if(s[i][0]=='?')
        {
            dorowcopy(i);
        }

    }

    cout<<"Case #"<<te<<":"<<endl;
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            cout<<s[i][j];
        }
        cout<<endl;
    }
    te++;
    }


}

