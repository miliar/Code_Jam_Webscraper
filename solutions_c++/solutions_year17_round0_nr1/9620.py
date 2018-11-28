#include<iostream>
#include<string>
using namespace std;

int main()
{
    int i,j, t,k, l;
    string str;
    cin >> t;
    for(int d=1; d<=t; d++){
        cin >> str >> k;
        int c=0,b=0;
        l= str.length();
        for(i=0;i<=l-k;i++){
            if(str[i]== '-'){
                int j=i;
                int o=k;
                while(o!=0){
                    if(str[j]=='-')
                        str[j]='+';
                    else
                        str[j]='-';
                    j++;
                    o--;
                }
                c++;
            }
        }
        for(i=0;i<=l;i++){
            if(str[i]=='-'){
                b++;
                break;
            }
        }
        if(b==1)
            cout << "Case #" << d << ": " << "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << d << ": " << c << endl;
        }

    return 0;
}
