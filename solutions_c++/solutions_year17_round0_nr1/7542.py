#include <bits/stdc++.h>

using namespace std;

int main()
{
    int test, k, len, j;
    string str;
    cin>>test;

    for(int i=1; i<=test; ++i){
        cin>>str>>k;
        bool possible = true;
        int times = 0;
        //cout<<str<<endl<<k<<endl;
        len = str.length();
        for(j=0; j<len; ++j){
            if(str[j]=='-'){
                if(j+k > len){
                    possible = false;
                    break;
                }

            for(int z = j; z< j+k; ++z){
                if(str[z]=='-')
                    str[z] = '+';
                else
                    str[z] = '-';
            }
            times++;
            }
        }
        cout<<"Case #"<<i<<": ";
        if(possible){
           cout<<times;
        }
        else
            cout<<"IMPOSSIBLE";
        cout<<"\n";
    }
    return 0;
}

