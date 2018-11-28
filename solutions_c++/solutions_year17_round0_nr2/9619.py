#include <bits/stdc++.h>
using namespace std;

int main()
{
    unsigned long long int t,i,j,k,ans;
    string strInput;

    freopen ("ans2017-b.out","w",stdout);
	freopen ("B-large.in","r",stdin);

    cin>>t;

    for(k=0;k<t;k++)
    {

        cin>>strInput;
        bool bRepeat=true;

        while(bRepeat)
        {

            bRepeat=false;
            for(i=0;i<strInput.length();i++)
            {
                if(i+1 < strInput.length() && strInput[i] > strInput[i+1])
                {
                    bRepeat=true;
                    strInput[i]--;
                    for(j=i+1;j<strInput.length();j++)
                    {
                        strInput[j]='9';
                    }
                    break;
                }

            }
        }


        ans=0;

        for(i=0;i<strInput.length();i++)
        {
            unsigned long long temp=pow(10,strInput.length() -i -1);
            ans+=(strInput[i]-'0')*temp;
        }

          cout<<"Case #"<<k+1<<": "<<ans<<endl;

    }

    fclose (stdout);
	fclose(stdin);
    return 0;
}

