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
    string s[no];
    int x,k[no],counter;
    for(int i=0;i<no;i++){
        cin>>s[i];
        cin>>k[i];
    }
    for(int i=0;i<no;i++){
        counter =0;
        x = s[i].length() - k[i];
        for(int j =0;j<=x;j++){
            if(s[i][j]=='-'){
                counter++;
                s[i] = change(s[i],j,k[i]);
            }
        }
        for(int j=x+1;j<s[i].length();j++)
            if(s[i][j]=='-')
                counter = -1;
        cout<<"Case #"<<i+1<<": ";
        if(counter==-1)
            cout<<"IMPOSSIBLE\n";
        else    cout<<counter<<endl;
    }
    return 0;
}
