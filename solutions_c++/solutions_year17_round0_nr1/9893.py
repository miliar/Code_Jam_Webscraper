#include <iostream>
#include <string>
using namespace std;

string change(string x, int a, int b){
    for(int z=a;z<a+b;z++){
        if(x[z]=='-')
            x[z] = '+';
        else    x[z] = '-';
    }
    return x;
}
int main()
{
    int no;
    cin>>no;
    string st[no];
    int x,k[no],counter[no];
    for(int i=0;i<no;i++){
        cin>>st[i];
        cin>>k[i];
    }
    for(int i=0;i<no;i++){
        counter[i] =0;
        x = st[i].length() - k[i];
        for(int j =0;j<=x;j++){
            if(st[i][j]=='-'){
                (counter[i])++;
                st[i] = change(st[i],j,k[i]);
            }
        }
        for(int j=x+1;j<st[i].length();j++)
            if(st[i][j]=='-')
                counter[i] = -1;
        cout<<"Case #"<<i+1<<": ";
        if(counter[i]==-1)
            cout<<"IMPOSSIBLE\n";
        else    cout<<counter[i]<<endl;
    }
    return 0;
}
