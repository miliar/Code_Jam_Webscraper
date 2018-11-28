#include <iostream>
#include <set>
#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out", "w", stdout);


    int t;
    cin>>t;
    int count=1;
    while(t--)
    {
        char ch[20],ans[20];
        cin>>ch;
        ans[0]=ch[0];
        int i,j,m;
        for(i=1;ch[i]!='\0';i++)
        {
          //  cout<<"SDFDFG ";
            if(ch[i-1]>ch[i])
            {
                m=i;
            //    cout<<"SDFDFG ";
                ans[i-1]=ch[i-1]-1;
                for(j=i;ch[j]!='\0';j++,i++)
                    ans[j]='9';
                ans[j]='\0';

              //  cout<<ans;

                j=m-1;
                while(ans[j-1]>ans[j])
                {
                    //cout<<"SDFDFG ";
                    //if(ch[j-1]>ch[j])
                        ans[j-1]=ans[j-1]-1;
                        ans[j]='9';
                    //else
                      //  break;
                    //cout<<ans<<" ";
                    j--;
                }
                break;
            }
            else
                ans[i]=ch[i];
        }

        int w=0;
        for(i=0;ch[i]!='\0';i++)
            w++;

        ans[w]='\0';
        //111111111111111110
        //  111111111111111109
        //99999999999999999
        //99999999999999999
        for(i=0;ans[i]!='\0';i++)
                if(ans[i]!='0')
                    break;


        cout<<"Case #"<<count++<<": "<<&ans[i]<<endl;
    }


    return 0;
}
