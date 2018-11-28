#include<string>
#include<iostream>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    string nueve="99999999999999999999",napadas;
    int t,x,y,a,c;
    cin>>t;
    for(c=1;c<=t;c++)
        {
        cin>>napadas;
        y=napadas.size();
        cout<<"Case #"<<c<<": ";
        if(y==1)
            {
            cout<<napadas<<endl;
            continue;
            }
        for(x=1;x<y;x++)
            if(napadas[x]<napadas[x-1])
                break;
        if(x==y)
            {
            cout<<napadas<<endl;
            continue;
            }
        for(;x>0&&napadas[x-1]>napadas[x];x--)
            napadas[x-1]--;
        cout<<stoll(napadas.substr(0,x+1).append(&nueve[20-(y-x-1)]))<<endl;
        }
    return 0;
}
