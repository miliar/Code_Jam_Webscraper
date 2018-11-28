#include <iostream>
#include <cstdio>
using namespace std;
string trim(string str){
    int i = 0;
    while(i + 1 < str.size() && str[i] == '0')
        i++;
    return str.substr(i);
}
int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);

    int t;
    cin >> t;
    for(int f=1; f<=t; f++){
        string number;
        cin >> number;
        for(int i=0; i+1<number.size(); i++){
            if(number[i] > number[i+1]){
                int j;
                for(j = 0; j<number.size(); j++)
                    if(number[j] == number[i])
                        break;
                number[j++]--;
                while(j < number.size()){
                    number[j] = '9';
                    j++;
                }
                break;
            }
        }
        cout << "Case #" << f << ": " << trim(number) << endl;
    }
    return 0;
}
