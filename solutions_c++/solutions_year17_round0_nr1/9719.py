#include<iostream>
#include<vector>

using namespace std;

int happy(string p,int k){
    int tam=p.length();

    int res=0;
    for(int i=0; i<tam;i++)
    {
     if(p[i]=='-')
     {
         if(i+k<=tam)
        {
              for(int j=i; j<i+k;j++)
            {
            // cout<<"J en "<<j<<" I EN "<<i<<endl;
            if(p[j]=='-')
                p[j]='+';
            else
                p[j]='-';
            }
        // cout<<"STRING "<<p;

       // cout<<"I EN I+K "<<i<<endl;
        res++;
       // cout<<"RESPUESTA VA EN "<<res<<endl;
        }
         else
         {
             return -1;

         }


     }
    }
    string h;
    for(int i=0; i<tam;i++)
    {
        h=h+'+';
    }
    if(p==h)
        return res;



}

int main()
{
    vector <char> arr;
    string panque;
    int cases, k;
    cin>>cases;
    for(int i=0; i<cases;i++)
    {
        int resp;
        cin>>panque;
        cin>>k;
        resp=happy(panque,k);
        cout<<"Case #"<<i+1<<": ";
        if(resp==-1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<resp<<endl;
    }


return 0;
}
