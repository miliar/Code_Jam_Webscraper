#include<iostream>
using namespace std;

int main()
{
    int tst1;
    cin>>tst1;
    for(int iz=1;iz<=tst1;iz++)
    {
        int i;
        string strng;
        cin>>strng;
        int alen=strng.length();
        int tmpy=0;
        for(i=alen-1;i>0;i--)
        {
            if(strng[i]<strng[i-1]&&strng[i]!=0&&strng[i-1]!=0)
                {
                    for(int a=i;a<alen;a++)
                        strng[a]='9';
                    strng[i-1]=strng[i-1]-1;
                    if(strng[i-1]=='0')
                        i++;
                }
            while(strng[i]=='0')
            {
                tmpy=1;
                i--;
            }
            if(tmpy)
            {
                strng[i]=strng[i]-1;
                for(int a=i+1;a<alen;a++)
                    strng[a]='9';
                if(strng[i]=='0')
                    i++;
                tmpy=0;
            }

        }
        cout<<"Case #"<<iz<<": ";
        int tmpy1=0;
        for(i=0;i<strng.length();i++)
         {
             if(strng[i]!='0')
             {
                 tmpy1=1;
             }
             if(tmpy1==1)
                cout<<strng[i];
         }
         cout<<endl;
    }
    return 0;
}
