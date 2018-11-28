#include <iostream>
#include <cstring>
#include <stdio.h>
#include <string>
#include <fstream>

using namespace std;
int t;
string s,ss;
long long w;
ofstream answer;

int main()
{
    answer.open("answer.txt");
    scanf("%d",&t);
    for (int i=0;i<t;i++){
        cin >> s;
        ss=s;
        w=s.size();
        for (long long j=w-1;j>-1;j--){
            char m='-';
            for (long long k=j+1;k<w;k++){
                if (s[j]>s[k]){
                    m=max(m,s[k]);
                }
            }
            if (m!='-'){
                s[j]=s[j]-1;
                for (long long k=j+1;k<w;k++){
                    s[k]='9';
                }
            }
        }
        for (long long j=0;j<w;j++){
            if (s[j]!='0'){
                break;
            }else{
                s.erase (s.begin()+j);
            }
        }
        answer<<"Case #"<<i+1<<": "<<s << endl;
    }
    answer.close();
    return 0;
}
