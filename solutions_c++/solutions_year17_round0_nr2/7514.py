#include <bits/stdc++.h>

using namespace std;
int findit(int x)
{

    int y=x;
    int now=10,notn=0;
    while(y!=0)
    {
        int m=y%10;
    if(m<=now)
    {
        now=m;
        y=y/10;
    }
    else
    {
        notn=1;
        break;
    }
    }

    if(notn==1)
    {x--;
    findit(x);
    }
    else
     return x;
}
int main()
{
    //ofstream myfile;
    //myfile.open ("example.txt");
    int t;
    int it=1;
    cin>>t;
    while(t!=0)
    {
        int n;
        cin>>n;
        if(n/10==0)
            cout<<"case #"<<it<<": "<<n<<endl;
            //myfile<<"case #"<<it<<": "<<n<<endl;
        else
            cout<<"case #"<<it<<": "<<findit(n)<<endl;
            //myfile<<"case #"<<it<<": "<<findit(n)<<endl;
        it++;
        t--;
    }
    //myfile.close();
    return 0;
}
