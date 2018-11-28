#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    string n;
    for(int i=0;i<t;i++)
    {
        cin>>n;
        int s=n.size();
        int c=0,cp=-1;
        bool x=false;
        int x1;
        for(int j=0;j<s;j++)
        {
            if(n[j-1]>n[j])
            {
                for(int k=j;k<s;k++)
                    n[k]='9';
                n[j-1]--;
                j=0;
            }
        }
        if(n[0]=='0')
            n.erase(0,1);
        cout<<"Case #"<<i+1<<": "<<n<<endl;
    }
    return 0;
}
