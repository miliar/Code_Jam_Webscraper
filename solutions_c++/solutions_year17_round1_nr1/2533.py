#include<bits/stdc++.h>
using namespace std;

int main()
{
    int curr=1;

freopen("in.txt","r",stdin);
freopen("output.txt","w",stdout);
    int t;
   cin>>t;
    while(t--)
    {
        char c[50][50];
        int r,col;
        cin>>r>>col;

        for(int i=1;i<=r;i++)
        {
            int counti=0;
            for(int j=1;j<=col;j++)
                {
                    cin>>c[i][j];
                    if(c[i][j]!='?')
                        counti++;

        }
        if(counti!=0)
            c[i][0]='y';
            else if(counti==0)
            c[i][0]='n';
        }

        for(int i=1;i<=r;i++)
        {
            if(c[i][0]=='y')
            {
                int start=1;
                int temp;
            for(int j=1;j<=col;j++ )
                {

                    if(c[i][j]!='?')
                    {

                        temp=j-1;

                        while((temp>=start)&&(temp>0))
                        {
                         //if(c[i][temp]=='?')

                            c[i][temp]=c[i][j];
                            temp--;
                        }
                        start=j+1;
                    }
                }

                if((start<=col)&&(start!=1))
                {
                    int m=start-1;
                    while(start<=col)
                    {

                        c[i][start]=c[i][m];
                        start++;
                    }
                }
        }
    }
    int s;
    //int e=1;
   // for(int i=1;i<=r;i++)
     //   cout<<c[i][0];
    for(int i=1;i<=r;i++)
    {

        if(c[i][0]!='y')
        {
            //cout<<"**********";
            s=i+1;

            while((s<=r)&&(c[s][0]=='n'))
            s++;

            if(s>r)
            {
               // cout<<"**********";
                 s--;
                while(c[s][0]=='n')
                    s--;
                while(s<r)
                {

                    for(int j=1;j<=col;j++)
                        c[s+1][j]=c[s][j];
                    s++;
                   // cout<<"**********";
                }
            }
            else
            {


            while((s>1)&&(s>i))
            {

                for(int j=1;j<=col;j++)
                    c[s-1][j]=c[s][j];
                s--;
            }
            }
        }
    }
  cout<<"Case #"<<curr<<":"<<"\n";
    for(int i=1;i<=r;i++)
    {

        for(int j=1;j<=col;j++)
            cout<<c[i][j];
        cout<<"\n";
    }
    curr++;

   // if(s>)

}
}




