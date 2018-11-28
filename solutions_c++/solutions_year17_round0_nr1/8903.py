#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
   /* string a;
    cin>>a;
    if(a[2]=='r')
    {
a[2]='t';

    }*/
 /*   ifstream ifi;
    ifi.open("a.txt");
    ofstream out;
    out.open("ans.txt");*/

    int times;
   cin>>times;
 //  ifi>>times;


    for(int t=1;t<=times;t++)
    {
        string pan;
        int k;
        cin>>pan;
        cin>>k;
     // ifi>>pan;
     // ifi>>k;
     // cout<<pan<<" "<<k<<" ";
        int len=0;
        for(int y=0;pan[y]!='\0';y++)
        {
            len++;
        }
       // cout<<"Length : "<<len<<endl;
         int ans=0;
         int flag=0;
        for(int i=0;i<len;i++)
        {
            if(pan[i]=='-' && (len-i)>=k)
            {
                //flip
                for(int j=i;j<i+k;j++)
                {
                    if(pan[j]=='-')
                    {
                        pan[j]='+';
                    }
                    else
                    {
                        pan[j]='-';
                    }
                }

                ans++;
            }
            else if(pan[i]=='-' && (len-i)<k)
            {
                flag=1;
                break;

            }
        //    cout<<endl<<pan;

        }

        if(flag==0)
        {
            cout<<"Case #"<<t<<": "<<ans;
          //  out<<"Case #"<<t<<": "<<ans<<endl;
           // cout<<endl<<pan;
        }
        else
        {
            cout<<"Case #"<<t<<": "<<"IMPOSSIBLE";
           // out<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
           // cout<<endl<<pan;
        }
        cout<<endl;
    }


  //  cout<<a;
   // cout << "Hello world!" << endl;
    return 0;
}
