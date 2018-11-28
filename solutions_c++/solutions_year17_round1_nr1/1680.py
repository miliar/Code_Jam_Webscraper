#include <iostream>
#include <vector>
using namespace std;
vector<string> v;
int R,C;
char llenar(int a, int b)
{
    int aux=b;
    b++;
    while(b<C)
    {
        if(v[a][b]=='?')
            v[a][b]=v[a][b-1];
        else break;
        b++;
    }
    b=aux;
    b=b-1;
    while(b>=0)
    {
        if(v[a][b]=='?')
            v[a][b]=v[a][b+1];
        else break;
        b--;
    }
}
char llenar2(int a, int b)
{
    int aux=a;
    a++;
    while(a<R)
    {
        if(v[a][b]=='?')
            v[a][b]=v[a-1][b];
        else break;
        a++;
    }
    a=aux;
    a=a-1;
    while(a>=0)
    {
        if(v[a][b]=='?')
            v[a][b]=v[a+1][b];
        else break;
        a--;
    }
}
int main()
{
    int cases;
    string s;
    cin>>cases;
    for(int i2=1; i2<=cases; i2++)
    {
        cin>>R>>C;
        for(int i3=0; i3<R; i3++)
        {
            cin>>s;
            v.push_back(s);
        }
        for(int i=0; i<v.size(); i++)
            for(int j=0; j<v[i].size(); j++)
                if(v[i][j]!='?')
                    llenar(i,j);
        for(int i=0; i<v.size(); i++)
            for(int j=0; j<v[i].size(); j++)
                if(v[i][j]!='?')
                    llenar2(i,j);
        cout<<"Case #"<<i2<<":"<<endl;
        for(int i=0; i<v.size(); i++)
            cout<<v[i]<<endl;
        v.clear();
    }       
    return 0;
}