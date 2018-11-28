#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int> ii;
typedef long long ll;

int main()
{
    //freopen("#input.in","r",stdin);
    //freopen("#output.in","w",stdout);

    int i,j,k,l,t,r,c;
    string str[26];

    cin>>t;

    for(i=1; i<=t; i++)
    {
        cin>>r>>c;

        for(j=0; j<r; j++)
            cin>>str[j];

        for(j=0; j<r; j++)
        {
            for(k=0; k<c; k++)
            {
                if(str[j][k]!='?')
                {
                    for(l=k-1; l>=0; l--)
                    {
                        if(str[j][l]=='?')
                            str[j][l]=str[j][k];
                        else
                            break;
                    }
                    for(l=k+1; l<c; l++)
                    {
                        if(str[j][l]=='?')
                            str[j][l]=str[j][k];
                        else
                        {
                            k = l-1;
                            break;
                        }
                    }
                }
            }
        }
        for(j=0; j<r; j++)
        {
            if(str[j][0]!='?')
            {
                for(k=j-1; k>=0; k--)
                {
                    if(str[k][0]=='?')
                        str[k]=str[j];
                    else
                        break;
                }
                for(k=j+1; k<r; k++)
                {
                    if(str[k][0]=='?')
                        str[k]=str[j];
                    else
                    {
                        j = k-1;
                        break;
                    }
                }
            }
        }

        cout<<"Case #"<<i<<":\n";
        for(j=0; j<r; j++)
            if(j!=(r-1))
                cout<<str[j]<<endl;
            else
                cout<<str[j];
        cout<<endl;
    }
    return 0;
}

