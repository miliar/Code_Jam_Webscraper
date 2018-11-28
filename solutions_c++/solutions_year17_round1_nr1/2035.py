#include<bits/stdc++.h>
using namespace std;
string mat[60];
string ans[60];
int r,c;

int fn(int topx,int topy,int botx,int boty)
{
      if(topx>=0 && topx<r && topy>=0 && topy<c && botx>=0 && botx<r && boty>=0 && boty<c);
    else
        return 0;

    int prev = topx-1;

    for(int i=topx;i<=botx;i++)
        {
            for(int j=topy;j<=boty;j++)
            {
                if(ans[i][j]!='?')
                {

                    //found one

                    for(int k=i;k>prev;k--)
                    {
                        for(int l=j;l>=topy;l--)
                        {
                            if(ans[k][l]=='?')
                            {
                                ans[k][l]=ans[i][j];
                            }
                        }
                    }

                    fn(prev+1,j+1,i,boty);
                    prev=i;
                    break;
                }
            }
        }

    return prev;

}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);


	int t;
	cin>>t;




	for(int trm=1;trm<=t;trm++)
	{
		cout<<"Case #"<<trm<<":"<<endl;
        cin>>r>>c;

        for(int i=0;i<r;i++)
        {
            cin>>mat[i];
            ans[i]=mat[i];
        }

        int pp = fn(0,0,r-1,c-1);


        for(int i=0;i<=pp;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(ans[i][j]=='?')
                {
                    ans[i][j]=ans[i][j-1];
                }
            }
        }

        //finally fill last rows

        for(int i=pp+1;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(ans[i][j]=='?')
                {
                    ans[i][j]=ans[i-1][j];
                }
            }
        }

        for(int i=0;i<r;i++)
        {
            cout<<ans[i]<<endl;
        }


	}
}
