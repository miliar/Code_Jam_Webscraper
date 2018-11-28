#include <bits/stdc++.h>
using namespace std;

int main() {
    int t,i,j,k,r,c;
    cin>>t;
    for(int q=1;q<=t;q++)
    {
        cin>>r>>c;
        char str[r][c+1];
        for(i=0;i<r;i++)
         cin>>str[i];
        for(i=0;i<r;i++)
        {for(j=0;j<c;j++)
         {
          if(str[i][j]!='?')
          {k=j-1;
            while(k>=0&&(str[i][k]=='?'))
            {str[i][k]=str[i][j];
             k--;
            }
            k=j+1;
            while(k<c&&(str[i][k]=='?'))
            {str[i][k]=str[i][j];
             k++;
            }
          }
         }
        }
        if(str[0][0]=='?')
        {
            for(i=1;i<r;i++)
             if(str[i][0]!='?')
             break;
            strcpy(str[0],str[i]);
        }
        for(i=1;i<r;i++)
        {
         if(str[i][0]=='?')
          strcpy(str[i],str[i-1]);
        }
        cout<<"Case #"<<q<<':'<<endl;
        for(i=0;i<r;i++)
        cout<<str[i]<<endl;
    }
    return 0;
}
