#include <iostream>

using namespace std;

int main()
{
     int val;
     cin>>val;
     for(int x=0;x<val;x++)
    {
        string cakes="";
        bool ispos=1;
        int wid,switches=0;
        cin>>cakes;
        cin>>wid;
        for(int y=0;y<=cakes.length()-wid;y++)
        {
            if(cakes[y]=='-')
            {
                switches++;
                for(int z=0;z<wid;z++)
                {
                    if(cakes[y+z]=='-')
                        cakes[y+z]='+';
                    else
                        cakes[y+z]='-';
                }
            }
        }
        for(int y=cakes.length()-wid;y<cakes.length();y++)
        {
            if(cakes[y]=='-')
            {
            ispos=0;
            }
        }
        cout<<"Case #"<<x+1<<": ";
        if(ispos)
        {
            cout<<switches<<endl;
        }
        else
        cout<<"IMPOSSIBLE"<<endl;
    }
}
