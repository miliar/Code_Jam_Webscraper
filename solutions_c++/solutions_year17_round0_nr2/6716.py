#include<iostream>
using namespace std;
int main()
{

    int t,i,pos,k=1,temp,f;
    cin>>t;
    char n[20];
    while(t--)
    {
        f=0;
        pos=20;
        cin>>n;
       // cout<<n<<"      ";
        if(n[1]=='\0')
        {
            cout<<"Case #"<<k<<": "<<n[0];
        }
        else{
        i=1;
        while(n[i]!='\0')
        {
            if(n[i]<n[i-1]&&f==0)
            {
                f=1;
               // cout<<i<<endl;
               // cout<<"Chota hai"<<endl;
                pos=i;
                n[i-1]--;
          //      cout<<n[i-1]<<endl;
            if(n[i-2]>n[i-1]&&n[i-1]>'0'&&(i-2)>=0)
            {
               // cout<<"FIRST"<<endl;
                temp=pos;
                temp--;
                pos--;
                while(n[temp-1]>n[temp] && temp-1>0)
                {
                    pos--;
                    n[temp-1]=n[temp];
                    temp--;
                }
                if(n[0]>n[1]&&n[1]!='0')
                    n[0]=n[1];

            }
            else if((n[i-1]<'1')&&(i-1)>0)
                {
                   // cout<<"SECOND"<<endl;
                    pos--;
                  //  cout<<pos<<" "<<n[pos]<<endl;
                    //cout<<n[pos-1]<<endl;
                    while( ( --n[pos-1] <'1')&&(pos-1)>0)
                    {
                    //    cout<<"Ghussa"<<endl;
                        pos--;
                    }
                }
        }
            i++;
        }
      //  cout<<pos<<endl;
        cout<<"Case #"<<k<<": ";
        i--;
               // n[0]--;
        for(int j=0;j<=i;j++)
        {
            if(j>=pos)
              cout<<"9";
            else
            {
                if(n[j]>'0')
                    cout<<n[j];
            }
        }

        }
       // cout<<"    "<<n;
        cout<<endl;
        k++;
    }
    return 0;
}

