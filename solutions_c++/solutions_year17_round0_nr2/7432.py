#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {

        char a[19];
        cin>>a;

        cout<<"Case #"<<j<<": ";
        int n=strlen(a);

        if(n==1)
            cout<<a;
        else{
            bool istidy=true;
            for(int i=0;i<n-1;i++)
            {
                if(a[i]>a[i+1]){
                    istidy=false;
                    break;
                }
            }
            if(istidy==false)
            {



            bool flag=false;


            for(int i=0;i<n-1;i++)
            {



                if(a[i]>=a[i+1]&&flag==false)
                {
                    a[i]--;
                    flag=true;


                }
                else if(flag==true)
                {
                    a[i]='9';
                }




                //cout<<eq<<" ";


            }

            if(flag==true)
                a[n-1]='9';

            }
            if(a[0]!='0')
                cout<<a[0];
            for(int i=1;i<n;++i)
                cout<<a[i];
            cout<<"\n";



        }
    }
    return 0;

}
