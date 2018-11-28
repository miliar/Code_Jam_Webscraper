#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t,i,tc=1;
    cin>>t;
    while (t--)
    {
        string s;
        cin>>s;
        int n=s.length();
        //cout<<n<<endl;

        if (n==1)
            cout<<"Case #"<<tc<<": "<<s<<endl;
        else
        {

            char A[n],B[n];
            for (i=0;i<n;i++)
            {
                A[i]=s[i];
                B[i]=s[i];
            }
            int noLesserConfirm=0;

            for (i=0;i<n;i++)
            {
                if (i!=0&&A[i]<A[i-1])
                {
                    break;
                }
            }

            if (i==n)
            {
                cout<<"Case #"<<tc<<": ";
                for (int k=0;k<n;k++)

                {
                    if (A[k]!='0')
                    {
                        cout<<A[k];
                    }
                }
                    cout<<endl;
            }

            else
                {

            int p=i;
            while (i!=n)
            {
                A[i]='9';
                i++;
            }
            A[p-1]--;

           int  buster,bl,zeroproof=0;
           while (zeroproof==0)
           {
               buster=0;
            for (i=0;i<n;i++)
            {
                if ((A[i]=='0'||A[i]<A[i-1])&&i!=0)
                {
                    buster=1;
                    bl=i;
                    break;
                }
            }
            if (i==n&&buster==0)
            {
                zeroproof=1;
            }
            if (buster==1)
            {
                A[bl]='9';
                A[bl-1]=A[bl-1]-1;
            }
           }
           cout<<"Case #"<<tc<<": ";
            for (int j=0;j<n;j++)
            {
                if (A[j]!='0')
                cout<<A[j];
            }
            cout<<endl;
        }
        }
        tc++;
    }
    return 0;
}
