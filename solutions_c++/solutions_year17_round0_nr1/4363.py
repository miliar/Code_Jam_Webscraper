#include<bits/stdc++.h>
typedef long long int ll;
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int m=1;m<=t;m++){
        string s;
        int k,cou=0,chack=1;
        cin>>s>>k;
        //you can flip the first K pancakes, but not the first K - 1 pancakes.
        for(int i=0;i<s.length()-k+1;i++){
            if(s[i]=='-'){
                cou++;
                for(int j=i;j<i+k;j++){
                    if(s[j]=='-')
                        s[j]='+';
                    else if(s[j]=='+')
                        s[j]='-';
                }
            }
        }
        for(k=0;k<s.length();k++){
                if(s[k]=='-'){
                    chack=0;
                    break;
                }
        }
        if(chack==1)
            cout<<"Case #"<<m<<": "<<cou<<endl;
        else
            cout<<"Case #"<<m<<": "<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
